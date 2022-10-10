import pandas as pd
from .project_data import *

def startup():
    df= pd.read_csv('/Users/edgarohanyan/Desktop/Shant/17.01/sample_1903-2.csv')
    data=df.iloc[:,[0,1,7,9]]
    data
    df_to_array = data[0:].to_numpy()
    df_to_array
    for array in df_to_array:
        url={}
        url["domain"]=array[0]
        url["dns"]=array[1]
        url["emails"]=array[2]
        url["phone"]=array[3]
        urls.append(url)


    c.execute("""DROP TABLE domains""")
    c.execute("""DROP TABLE dates""")
    c.execute("""DROP TABLE urls""")



    c.execute("""CREATE TABLE domains (
                domain_id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain  TEXT
            )""")
    c.execute("""CREATE TABLE dates (
                date_id INTEGER PRIMARY KEY AUTOINCREMENT,
                date  TEXT,
                history_log TEXT,
                domain_id,
                CONSTRAINT dd_domain
                FOREIGN KEY (domain_id)
                REFERENCES domains(domain_id)

            )""")
    c.execute("""CREATE TABLE urls(
                url_id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain TEXT,
                dns TEXT,
                emails,
                phone,
                cookies TEXT,
                trackers TEXT,
                SSL TEXT,
                SSL_EXPIRED TEXT,
                cms TEXT,
                redirect TEXT,
                httpredirect,
                Imprint,
                Policy,
                googleAnalitics TEXT,
                anonymizeIP TEXT,
                scrapped TEXT,
                date_id,
                CONSTRAINT du_dates
                FOREIGN KEY (date_id)
                REFERENCES dates(date_id)
                )""")

    c.execute("INSERT INTO domains(domain) VALUES('.DE')")

    today = datetime.today()
    d4 = today.strftime("%Y/%m/%d %H:%M:%S")
    d=c.execute("SELECT domain_id FROM domains WHERE domain='.DE' ")
    c.execute("INSERT INTO dates(date, domain_id) VALUES('{}','{}')".format(d4,d.fetchone()[0]))
    d=c.execute("SELECT date_id FROM dates WHERE date='{}' ".format(d4))
    date_id=d.fetchone()[0]
    for url in urls:
        c.execute("INSERT INTO urls(domain,dns,emails,phone, date_id) Values(:domain,:dns,:emails,:phone,:date_id)",{"domain":url['domain'],"dns":url['dns'],"emails":url['emails'],"phone":url['phone'],"date_id":date_id})
