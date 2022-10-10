from .project_data import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .check_pages_cookies import checkPagesandCookies
from .check_redirect import domain_redirect
from .check_SSL import getSSL

# def runActions(var, style, progressBar, my_window):
#     var.set("")
#     percentage = 0
#     progressBar['value'] = 0
#     style.configure('text.Horizontal.TProgressbar',
#                     text='{:g} %'.format(0))
#     listActions = [domain_redirect, checkPagesandCookies, getSSL]
#     index = 0
#     print(f"\n\n\n ---- URLS --{len(urls)}-- {urls}------\n\n\n\n")
#     for url in urls:
#         print(f"\n\n ------Actions.py loop --- {url['domain']} ------\n\n\n\n\n")
#         for action in listActions:
#             # message=action(url['domain'], index)
#             action(url['domain'], index)
#         percentage = round(((index + 1) / len(urls)) * 100)
#         progressBar['value'] = index + 1
#         style.configure('text.Horizontal.TProgressbar',
#                         text='{:g} %'.format(percentage))
#         my_window.update()
#         index += 1
#     conn.commit()
#     displayLog(var)

def runActions(var, style, progressBar, my_window):
    from scrapy.crawler import CrawlerProcess
    from ..spiders.get_cookies_spider import GetCookies
    from ..spiders.check_word_spider import CheckWords
    from ..spiders.words_and_cookies import WordsCookies
    from ..spiders.words_and_cookies_2 import WordsCookies_2
    from scrapy.utils.project import get_project_settings

    with open('data.txt', 'w') as f:
        f.write('\n')

    tox = 'tox'

    process = CrawlerProcess(get_project_settings())
    # process.crawl(GetCookies, var=var, style=style, progressBar=progressBar, my_window=my_window, string=tox)
    # process.crawl(CheckWords, var=var, style=style, progressBar=progressBar, my_window=my_window, string=tox)
    # process.crawl(WordsCookies, var=var, style=style, progressBar=progressBar, my_window=my_window, string=tox)
    process.crawl(WordsCookies_2, var=var, style=style, progressBar=progressBar, my_window=my_window, string=tox)

    process.start()
    print(f"\n\n -- actions str -- {tox} -- \n")
    with open('/Users/edgarohanyan/Desktop/Shant/17.01/final/scrapy_action/data.txt', 'r') as f:
        data = f.read()
        send_email("edgarohanyan1994@gmail.com", "My Test Email", data)


    #  --------------------------

    # from twisted.internet import reactor
    # from scrapy.crawler import CrawlerRunner
    # from scrapy.utils.log import configure_logging
    # from ..spiders.get_cookies_spider import GetCookies
    # from ..spiders.check_word_spider import CheckWords
    #
    # configure_logging()
    # runner = CrawlerRunner()
    # runner.crawl(GetCookies)
    # runner.crawl(CheckWords)
    # d = runner.join()
    # d.addBoth(lambda _: reactor.stop())

    #  -----------------------

    # from twisted.internet import reactor, defer
    # from scrapy.crawler import CrawlerRunner
    # from scrapy.utils.log import configure_logging
    # from ..spiders.get_cookies_spider import GetCookies
    # from ..spiders.check_word_spider import CheckWords
    #
    # configure_logging()
    # runner = CrawlerRunner()
    #
    # @defer.inlineCallbacks
    # def crawl():
    #     yield runner.crawl(CheckWords)
    #     yield runner.crawl(GetCookies)
    #
    #     reactor.stop()
    #
    # crawl()
    # reactor.run()


def displayLog(var):
    scannedNumber = len(urls)
    redirectionViolation = c.execute("SELECT COUNT(*) FROM urls WHERE redirect = 'True'").fetchone()[0]
    httpredirection = c.execute("SELECT COUNT(*) FROM urls WHERE httpredirect = 'False'").fetchone()[0]
    cookieViolation = c.execute("SELECT COUNT(*) FROM urls WHERE cookies != ''").fetchone()[0]
    trackerViolation = c.execute("SELECT COUNT(*) FROM urls WHERE trackers != ''").fetchone()[0]
    googleAnaliticsViolation = c.execute("SELECT COUNT(*) FROM urls WHERE googleAnalitics = 'True'").fetchone()[0]
    anonymizeIPVioaltion = c.execute("SELECT COUNT(*) FROM urls WHERE anonymizeIP = 'True'").fetchone()[0]
    ImprintVioaltion = c.execute("SELECT COUNT(*) FROM urls WHERE Imprint = 'False'").fetchone()[0]
    PolicyVioaltion = c.execute("SELECT COUNT(*) FROM urls WHERE Policy = 'False'").fetchone()[0]
    SSLVioaltion = c.execute("SELECT COUNT(*) FROM urls WHERE SSL_EXPIRED = 'True'").fetchone()[0]
    s = '''
    Scanned: {scannedNumber}
    redirectionViolation:  {redirectionViolation}
    httpredirection:  {httpredirection}
    cookieViolation:  {cookieViolation}
    trackerViolation:  {trackerViolation}
    googleAnaliticsViolation:  {googleAnaliticsViolation}
    anonymizeIPVioaltion:  {anonymizeIPVioaltion}
    ImprintVioaltion:  {ImprintVioaltion}
    PolicyVioaltion:  {PolicyVioaltion}
    SSLVioaltion:  {SSLVioaltion}


    '''.format(
        scannedNumber=scannedNumber,
        redirectionViolation=redirectionViolation,
        httpredirection=httpredirection,
        cookieViolation=cookieViolation,
        trackerViolation=trackerViolation,
        googleAnaliticsViolation=googleAnaliticsViolation,
        anonymizeIPVioaltion=anonymizeIPVioaltion,
        ImprintVioaltion=ImprintVioaltion,
        PolicyVioaltion=PolicyVioaltion,
        SSLVioaltion=SSLVioaltion
    )
    c.execute("UPDATE dates SET history_log = '{}' WHERE date_id={}".format(s, date_id))
    var.set(s)


def send_email(recipient, subject, body):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "pythonapp01@gmail.com"
    password = "low.secure.mail18"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient

    msg['Subject'] = subject
    body = MIMEText(body)
    msg.attach(body)

    server = smtplib.SMTP_SSL(smtp_server, port)

    server.login(sender_email, password)
    server.sendmail(sender_email, recipient, msg.as_string())
    server.quit()