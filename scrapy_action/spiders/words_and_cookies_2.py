import scrapy
from scrapy_splash import SplashRequest

from ..whole_project.project_data import *


googleAnalitics = False
anonymizeIP = False

class WordsCookies_2(scrapy.Spider):
    name = "words_cookies_2"

    start_urls = [f"https://www.{url['domain']}" for url in urls]
    url_count = 0


    def start_requests(self):
        lua_request = """
                    function main(splash)
                        splash:init_cookies(splash.args.cookies)
                        assert(splash:go(splash.args.url))
                        splash:wait(1)
                        return {
                            html = splash:html(),
                            cookies = splash:get_cookies()
                        }
                    end
                    """

        for url in self.start_urls:

            yield SplashRequest(
                url,
                self.parse,
                endpoint='execute',
                # endpoint = 'render.html',
                args={'lua_source': lua_request}
            )

    def parse(self, response):
        print(f"\n -- Get Cookies -- {response}\n")
        self.url_count += 1
        get_cookies = response.cookiejar
        global googleAnalitics
        global anonymizeIP
        cookies = ""
        count = 0
        for cookie in get_cookies:
            count += 1
            if ("__utma" in cookie.value):
                googleAnalitics = True;
                anonymizeIP = True;
            cookies += cookie.name + ";"
            # print(f"\n -----Loop-2--- \n")
        print(f"\n ----{count}--{response}--- \n")

        with open('data.txt', 'a') as f:
            f.write(f"\n -- URL Count: {self.url_count} -- {response.url}\n -- -- Cookies -- --\n")
            f.write(
                "UPDATE urls SET googleAnalitics = '{}' WHERE domain = '{}' and date_id={}\n".format(str(googleAnalitics),
                                                                                                   response, date_id))
            f.write(
                "UPDATE urls SET anonymizeIP = '{}' WHERE domain = '{}' and date_id={}\n".format(str(anonymizeIP),
            response,date_id))
            f.write(
                "UPDATE urls SET cookies = '{}' WHERE domain = '{}' and date_id={}\n".format(cookies, response, date_id))

        body = response.body

        Impressum = self.check_word(body, "Impressum".encode(encoding='UTF-8'))
        Imprint = self.check_word(body, "Imprint".encode(encoding='UTF-8'))
        Privacy_Policy = self.check_word(body, "Privacy Policy".encode(encoding='UTF-8'))
        Datenschutzerklärung = self.check_word(body, "Datenschutzerklärung".encode(encoding='UTF-8'))


        with open('data.txt', 'a') as f:
            f.write(f"\n -- URL Count: {self.url_count} -- {response.url}\n -- -- Words -- --\n")
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
