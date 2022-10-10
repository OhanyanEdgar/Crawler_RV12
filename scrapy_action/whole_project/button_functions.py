from .project_data import *
from .gui import *
#   runHistory works with LastActivityButton
def runHistory(var):
    date =c.execute("SELECT date FROM dates WHERE date_id = {}".format(date_id)).fetchone()[0]
    log =c.execute("SELECT history_log FROM dates WHERE date_id = {}".format(date_id)).fetchone()[0]
    s = '''
    Date: {date}
    {log}
    '''.format(
        date=date,
        log=log,
    )
    var.set(s)

#   runSearchByDomain works with SearchByDomainButton
def runSearchByDomain(var):
    #   searchVar error was already here and app works fine with this error
    data = c.execute(
        "SELECT * FROM urls WHERE domain = '{}' and date_id={}".format(searchVar.get(), date_id)).fetchone()
    s = '''
    url_id={url_id}
    domain={domain}
    dns={dns}
    emails={emails}
    phone={phone}
    cookies={cookies}
    trackers={trackers}
    SSL={SSL}
    SSL_EXPIRED={SSL_EXPIRED}
    cms={cms}
    redirect={redirect}
    httpredirect={httpredirect}
    Imprint={Imprint}
    Policy={Policy}
    googleAnalitics={googleAnalitics}
    anonymizeIP={anonymizeIP}
    date_id={date_id}
    '''.format(
        url_id=data[0],
        domain=data[1],
        dns=data[2],
        emails=data[3],
        phone=data[4],
        cookies=data[5],
        trackers=data[6],
        SSL=data[7],
        SSL_EXPIRED=data[8],
        cms=data[9],
        redirect=data[10],
        httpredirect=data[11],
        Imprint=data[12],
        Policy=data[13],
        googleAnalitics=data[14],
        anonymizeIP=data[15],
        date_id=data[16]
    )
    var.set(s)

#   runSearchByFilterworks with SearchByFilterButton
#   Commented for now..?
def runSearchByFilter(var):
    data = []
    value = v.get() # v error was already here and app works fine with this error
    if (value == "redirectionViolation"):
        data = c.execute(
            "SELECT domain FROM urls WHERE redirectionViolation = 'True' and date_id={}".format(date_id)).fetchall()
    elif (value == "httpredirection"):
        data = [c.execute(
            "SELECT domain FROM urls WHERE httpredirection = 'True' and date_id={}".format(date_id)).fetchall()]
    elif (value == "cookieViolation"):
        data = [c.execute("SELECT domain FROM urls WHERE cookies != '' and date_id={}".format(date_id)).fetchall()]
    elif (value == "trackerViolation"):
        data = [c.execute("SELECT domain FROM urls WHERE trackers != '' and date_id={}".format(date_id)).fetchall()]
    elif (value == "googleAnaliticsViolation"):
        data = [c.execute(
            "SELECT domain FROM urls WHERE googleAnalitics = 'True' and date_id={}".format(date_id)).fetchall()]
    elif (value == "anonymizeIPVioaltion"):
        data = [
            c.execute("SELECT domain FROM urls WHERE anonymizeIP = 'True' and date_id={}".format(date_id)).fetchall()]
    elif (value == "ImprintVioaltion"):
        data = [c.execute("SELECT domain FROM urls WHERE Imprint = 'False' and date_id={}".format(date_id)).fetchall()]
    elif (value == "PolicyVioaltion"):
        data = [c.execute("SELECT domain FROM urls WHERE Policy = 'False' and date_id={}".format(date_id)).fetchall()]
    elif (value == "SSLVioaltion"):
        data = [
            c.execute("SELECT domain FROM urls WHERE SSL_EXPIRED = 'True' and date_id={}".format(date_id)).fetchall()]
    else:
        data = [];

    s = '''
    {data}
    '''.format(
        data=data
    )
    var.set(s)
