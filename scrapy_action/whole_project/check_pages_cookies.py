from .project_data import *

from selenium.webdriver.chrome.options import Options
from selenium import webdriver


from scrapy.utils.project import get_project_settings



def checkPagesandCookies(url, index):
    print('\n--', url, 'checkPagesandCookies---IN \n')
    siteUtl = "http://www." + url
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)
    driver.get(siteUtl)
    Impressum = checkImprintPage(driver, "Impressum", index)
    Imprint = checkImprintPage(driver, "Imprint", index)
    Privacy_Policy = checkPolicyPage(driver, "Privacy Policy", index)
    Datenschutzerklärung = checkPolicyPage(driver, "Datenschutzerklärung", index)

    # cookies=getCookies(driver, index, url) func dont return anything
    getCookies(index, url)
    # check_Pages(url)
    print('\n--', url, 'checkPagesandCookies\n')
    # print(f"\n\n\n\n -----------quit get cookies-----------\n\n\n\n\n")
    # # getTrackers(driver, index, url)
    # if (Impressum == True or Imprint == True):
    #     c.execute("UPDATE urls SET Imprint = 'True' WHERE domain = '{}' and date_id={}".format(url, date_id))
    # else:
    #     c.execute("UPDATE urls SET Imprint = 'False' WHERE domain = '{}' and date_id={}".format(url, date_id))
    # if (Privacy_Policy == True or Datenschutzerklärung == True):
    #     c.execute("UPDATE urls SET Policy = 'True' WHERE domain = '{}' and date_id={}".format(url, date_id))
    #
    # else:
    #     c.execute("UPDATE urls SET Policy = 'False' WHERE domain = '{}' and date_id={}".format(url, date_id))
    # driver.quit()
    print('\n--', url, 'checkPagesandCookies---OUT \n')

def check_Pages(url):
    from scrapy.crawler import CrawlerProcess
    from ..spiders.check_word_spider import CheckWords
    process = CrawlerProcess()
    process.crawl(CheckWords, url=url)
    process.start()

def getCookies(index, url):
    from scrapy.crawler import CrawlerProcess
    from ..spiders.get_cookies_spider import GetCookies

    # getCookiesObject = GetCookies()
    # getCookiesObject.start_urls = [f"https://{url}/"]

    process = CrawlerProcess(get_project_settings())

    process.crawl(GetCookies, url=url)
    process.start()

    # googleAnalitics = False;
    # anonymizeIP = False
    # cookieslist = driver.get_cookies()
    # cookies = ""
    # for cookie in cookieslist:
    #     if ("__utma" in cookie.values()):
    #         googleAnalitics = True;
    #         anonymizeIP = True;
    #     cookies += cookie['name'] + ";"
    # c.execute(
    #     "UPDATE urls SET googleAnalitics = '{}' WHERE domain = '{}' and date_id={}".format(str(googleAnalitics), url,
    #                                                                                        date_id))
    # c.execute(
    #     "UPDATE urls SET anonymizeIP = '{}' WHERE domain = '{}' and date_id={}".format(str(anonymizeIP), url, date_id))
    # c.execute("UPDATE urls SET cookies = '{}' WHERE domain = '{}' and date_id={}".format(cookies, url, date_id))

def checkImprintPage(driver, word, index):
    html_source = driver.page_source
    if word in html_source:
        return (True)
    else:
        return (False)


def checkPolicyPage(driver, word, index):
    html_source = driver.page_source
    if word in html_source:
        return (True)
    else:
        return (False)



# -----------
#    conn.commit()

# def getTrackers(driver, index, url):
#     html_source = driver.page_source
#     trackers=[tracker for tracker in set(domainNames) if(tracker in html_source)]
#     c.execute("UPDATE urls SET trackers = '{}' WHERE domain = '{}' and date_id={}".format(",".join(trackers),url,date_id))



