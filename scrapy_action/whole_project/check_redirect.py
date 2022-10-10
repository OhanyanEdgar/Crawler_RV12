
import requests
from .project_data import *

# these 2 functions are used to check the redirection.

def redirect_test(domTest, index):
    req = requests.head(domTest, allow_redirects=False, headers=user_agent)
    return (False if req.status_code == 200 or req.status_code == 301 else True)


def domain_redirect(url, index):
    print('\n--', url, 'redirect_test---IN \n')
    protocol_list = ['http://www.', 'https://www.']
    result = []
    redirect = False
    http_redirect = False
    for protocol in protocol_list:
        domTest = protocol + url
        result.append(redirect_test(domTest, index))

    if False in result:
        redirect = False
    if result[1] == False:
        http_redirect = True

    c.execute("UPDATE urls SET redirect = '{}' WHERE domain = '{}' and date_id={}".format(str(redirect), url, date_id))
    c.execute("UPDATE urls SET httpredirect = '{}' WHERE domain = '{}' and date_id={}".format(str(http_redirect), url,
                                                                                              date_id))
    print('\n--', url, 'redirect_test---OUT \n')
