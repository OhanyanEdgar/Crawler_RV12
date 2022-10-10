import scrapy

from ..whole_project.project_data import *


class CheckWords(scrapy.Spider):
    name = "check_words"
    urls = [f"https://www.{url['domain']}" for url in urls]

    start_urls = urls
    count = 0

    # def start_requests(self):
    #     url = self.url
    #     yield scrapy.Request(url, self.parse)



    def parse(self, response):
        body = response.body

        Impressum = self.check_word(body, "Impressum".encode(encoding='UTF-8'))
        Imprint = self.check_word(body, "Imprint".encode(encoding='UTF-8'))
        Privacy_Policy = self.check_word(body, "Privacy Policy".encode(encoding='UTF-8'))
        Datenschutzerklärung = self.check_word(body, "Datenschutzerklärung".encode(encoding='UTF-8'))

        self.count += 1
        print(f"\n ----{self.count}--{response}--- \n")
        if (Impressum == True or Imprint == True):
            print("UPDATE urls SET Imprint = 'True' WHERE domain = '{}' and date_id={}".format(response.url, date_id))
        else:
            print("UPDATE urls SET Imprint = 'False' WHERE domain = '{}' and date_id={}".format(response.url, date_id))
        if (Privacy_Policy == True or Datenschutzerklärung == True):
            print("UPDATE urls SET Policy = 'True' WHERE domain = '{}' and date_id={}".format(response.url, date_id))
        else:
            print("UPDATE urls SET Policy = 'False' WHERE domain = '{}' and date_id={}".format(response.url, date_id))
        print(f"\n")

        with open('words.txt', 'a') as f:
            f.write(f"\n -- URL Count: {self.count} -- {response.url}\n")
            if (Impressum == True or Imprint == True):
                f.write(
                    "UPDATE urls SET Imprint = 'True' WHERE domain = '{}' and date_id={}\n".format(response.url,
                                                                                                   date_id))
            else:
                f.write("UPDATE urls SET Imprint = 'False' WHERE domain = '{}' and date_id={}\n".format(response.url,
                                                                                                        date_id))
            if (Privacy_Policy == True or Datenschutzerklärung == True):
                f.write(
                    "UPDATE urls SET Policy = 'True' WHERE domain = '{}' and date_id={}\n".format(response.url,
                                                                                                  date_id))
            else:
                f.write(
                    "UPDATE urls SET Policy = 'False' WHERE domain = '{}' and date_id={}\n".format(response.url,
                                                                                                   date_id))

    def check_word(self, body, word):
        html_source = body
        if word in html_source:
            return (True)
        else:
            return (False)
