import scrapy
from scrapy_splash import SplashRequest

from ..whole_project.project_data import *


googleAnalitics = False
anonymizeIP = False


# class GetCookies(scrapy.Spider):
#     name = "get_cookies"
#     my_urls = [f"https://www.{url['domain']}/" for url in urls]
#     start_urls = ['https://www.chip.de/', 'https://www.mobile.de/', 'https://www.zdf.de/', 'https://www.otto.de/', 'https://www.heise.de/', 'https://www.dkb.de/', 'https://www.real.de/', 'https://www.thomann.de/', 'https://www.postbank.de/']
#     # start_urls = my_urls
#
#     count = 0
#     def parse(self, response, **kwargs):
#         self.count += 1
#         print(f"\n -- {self.count} response: {response} --\n")
#         print(f" -- URLS -- {self.my_urls}")


class WordsCookies(scrapy.Spider):
    name = "words_cookies"
    # start_urls = ['https://www.spiegel.de/', 'https://www.chip.de/', 'https://www.mobile.de/', 'https://www.zdf.de/',
    #               'https://www.otto.de/', 'https://www.heise.de/']
    start_urls = [f"https://www.{url['domain']}" for url in urls]
    url_count = 0
    # googleAnalitics = False
    # anonymizeIP = False

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
            f.write(f"\n -- URL Count: {self.url_count} -- {response.url}\n")
            f.write(
                "UPDATE urls SET googleAnalitics = '{}' WHERE domain = '{}' and date_id={}\n".format(str(googleAnalitics),
                                                                                                   response, date_id))
            f.write(
                "UPDATE urls SET anonymizeIP = '{}' WHERE domain = '{}' and date_id={}\n".format(str(anonymizeIP),
            response,date_id))
            f.write(
                "UPDATE urls SET cookies = '{}' WHERE domain = '{}' and date_id={}\n".format(cookies, response, date_id))

        print("UPDATE urls SET googleAnalitics = '{}' WHERE domain = '{}' and date_id={}".format(str(googleAnalitics),
            response,date_id))
        print("UPDATE urls SET anonymizeIP = '{}' WHERE domain = '{}' and date_id={}".format(str(anonymizeIP),
            response,date_id))
        print("UPDATE urls SET cookies = '{}' WHERE domain = '{}' and date_id={}".format(cookies, response, date_id))

        body = response.body

        Impressum = self.check_word(body, "Impressum".encode(encoding='UTF-8'))
        Imprint = self.check_word(body, "Imprint".encode(encoding='UTF-8'))
        Privacy_Policy = self.check_word(body, "Privacy Policy".encode(encoding='UTF-8'))
        Datenschutzerklärung = self.check_word(body, "Datenschutzerklärung".encode(encoding='UTF-8'))

        with open('data.txt', 'a') as f:
            if (Impressum == True or Imprint == True):
                f.write(
                    "UPDATE urls SET Imprint = 'True' WHERE domain = '{}' and date_id={}\n".format(response.url, date_id))
            else:
                f.write("UPDATE urls SET Imprint = 'False' WHERE domain = '{}' and date_id={}\n".format(response.url,
                                                                                                    date_id))
            if (Privacy_Policy == True or Datenschutzerklärung == True):
                f.write(
                    "UPDATE urls SET Policy = 'True' WHERE domain = '{}' and date_id={}\n".format(response.url, date_id))
            else:
                f.write(
                    "UPDATE urls SET Policy = 'False' WHERE domain = '{}' and date_id={}\n".format(response.url, date_id))

        if (Impressum == True or Imprint == True):
            print("UPDATE urls SET Imprint = 'True' WHERE domain = '{}' and date_id={}".format(response.url, date_id))
        else:
            print("UPDATE urls SET Imprint = 'False' WHERE domain = '{}' and date_id={}".format(response.url, date_id))
        if (Privacy_Policy == True or Datenschutzerklärung == True):
            print("UPDATE urls SET Policy = 'True' WHERE domain = '{}' and date_id={}".format(response.url, date_id))
        else:
            print("UPDATE urls SET Policy = 'False' WHERE domain = '{}' and date_id={}".format(response.url, date_id))
        print(f"\n")

    def check_word(self, body, word):
        # print(f"\n -- Check Word -- \n")
        html_source = body
        if word in html_source:
            return (True)
        else:
            return (False)