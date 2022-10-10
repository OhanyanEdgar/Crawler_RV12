from tkinter import *
from tkinter import ttk

from .button_functions import runHistory
from .button_functions import runSearchByDomain
from .button_functions import runSearchByFilter

from .project_data import *
from .actions import runActions
def window():
    my_window = Tk()
    w = my_window.winfo_screenwidth()
    h = my_window.winfo_screenheight()
    my_window.geometry("%dx%d+0+0" % (w, h))
    var = StringVar()
    sidebar = Frame(my_window, width=round(w / 10), height=h, bg="LightSteelBlue3", highlightbackground="#010100",
                    highlightthickness=2, relief="groove", bd=3)
    sidebar.pack(side=LEFT, fill=Y)
    AddDomainButton = Frame(sidebar, bg="LightSteelBlue3")
    AddDomainButton.pack(fill=X)
    Button(AddDomainButton, width=15, text="Add Domain", font=('Times', '14'), relief="raised").pack(side=LEFT, padx=20,
                                                                                                     pady=(50, 10))
    # ------------------Last Activity Button
    LastActivityButton = Frame(sidebar, bg="LightSteelBlue3")
    LastActivityButton.pack(fill=X)
    Button(LastActivityButton, width=15, text="Last Activity Log", command=lambda: runHistory(var),
           font=('Times', '14'), relief="raised").pack(side=LEFT, padx=20, pady=10)
    # ------------------Last Activity Button

    # ------------------Search By Domain Search Textarea
    searchVar = StringVar()
    searchBar = Frame(sidebar, bg="LightSteelBlue3")
    searchBar.pack(fill=X)
    # searchEntry = Entry(searchBar, width=14,font=('Times', '14'),textvariable = searchVar).pack(side=LEFT,
    # padx=20,pady=(20,5))
    Entry(searchBar, width=14, font=('Times', '14'), textvariable=searchVar).pack(side=LEFT, padx=20, pady=(20, 5))
    # ------------------Search By Domain Search Textarea

    # ------------------Search By Domain Button
    SearchByDomainButton = Frame(sidebar, bg="LightSteelBlue3")
    SearchByDomainButton.pack(fill=X)
    Button(SearchByDomainButton, width=15, text="Search By Domain", command=lambda: runSearchByDomain(var),
           font=('Times', '14'), relief="raised").pack(side=LEFT, padx=20, pady=(0, 20))
    # ------------------Search By Domain Button

    # ------------------Search By Filter Radio-Buttons
    v = StringVar()
    filterRadio = Frame(sidebar, bg="LightSteelBlue3")
    filterRadio.pack(fill=X)
    Radiobutton(filterRadio, bg="LightSteelBlue3", text='redirectionViolation', variable=v,
                value="redirectionViolation").pack(anchor=E, side=LEFT, padx=20, pady=(30, 0))
    filterRadio1 = Frame(sidebar, bg="LightSteelBlue3")
    filterRadio1.pack(fill=X)
    Radiobutton(filterRadio1, bg="LightSteelBlue3", text='httpredirection', variable=v, value="httpredirection").pack(
        anchor=E, side=LEFT, padx=20, pady=0)
    filterRadio2 = Frame(sidebar, bg="LightSteelBlue3")
    filterRadio2.pack(fill=X)
    Radiobutton(filterRadio2, bg="LightSteelBlue3", text='cookieViolation', variable=v, value="cookieViolation").pack(
        anchor=E, side=LEFT, padx=20, pady=0)
    filterRadio3 = Frame(sidebar, bg="LightSteelBlue3")
    filterRadio3.pack(fill=X)
    Radiobutton(filterRadio3, bg="LightSteelBlue3", text='trackerViolation', variable=v, value="trackerViolation").pack(
        anchor=E, side=LEFT, padx=20, pady=0)
    filterRadio4 = Frame(sidebar, bg="LightSteelBlue3")
    filterRadio4.pack(fill=X)
    Radiobutton(filterRadio4, bg="LightSteelBlue3", text='googleAnaliticsViolation', variable=v,
                value='googleAnaliticsViolation').pack(anchor=E, side=LEFT, padx=20, pady=0)
    filterRadio5 = Frame(sidebar, bg="LightSteelBlue3")
    filterRadio5.pack(fill=X)
    Radiobutton(filterRadio5, bg="LightSteelBlue3", text='anonymizeIPVioaltion', variable=v,
                value="anonymizeIPVioaltion").pack(anchor=E, side=LEFT, padx=20, pady=0)
    filterRadio6 = Frame(sidebar, bg="LightSteelBlue3")
    filterRadio6.pack(fill=X)
    Radiobutton(filterRadio6, bg="LightSteelBlue3", text='ImprintVioaltion', variable=v, value="ImprintVioaltion").pack(
        anchor=E, side=LEFT, padx=20, pady=0)
    filterRadio8 = Frame(sidebar, bg="LightSteelBlue3")
    filterRadio8.pack(fill=X)
    Radiobutton(filterRadio8, bg="LightSteelBlue3", text='PolicyVioaltion', variable=v, value="PolicyVioaltion").pack(
        anchor=E, side=LEFT, padx=20, pady=0)
    filterRadio9 = Frame(sidebar, bg="LightSteelBlue3")
    filterRadio9.pack(fill=X)
    Radiobutton(filterRadio9, bg="LightSteelBlue3", text='SSLVioaltion', variable=v, value="SSLVioaltion").pack(
        anchor=E, side=LEFT, padx=20, pady=0)
    # ------------------Search By Filter Radio-Buttons

    # ------------------Search By Filter Button
    SearchByFilterButton = Frame(sidebar, bg="LightSteelBlue3")
    SearchByFilterButton.pack(fill=X)
    # Button(SearchByFilterButton,width=15, text="Search By Filter",command=lambda:runSearchByFilter(var), font=('Times', '14'),relief="raised").pack(side=LEFT, padx=20,pady=(10,20))
    # ------------------Search By Filter Button

    # ------------------GUI style
    mainview = Frame(my_window, width=round(w - w / 10), bg="#EFEEEB", highlightbackground="#010100",
                     highlightthickness=1)
    mainview.pack(fill=BOTH, expand=True)
    frame1 = Frame(mainview, bg="#EFEEEB")
    frame1.pack(fill=X)
    # photo = PhotoImage(file = r"/Users/shantjoulfayan/Desktop/start.png")
    style = ttk.Style(frame1)
    style.layout('text.Horizontal.TProgressbar',
                 [('Horizontal.Progressbar.trough',
                   {'children': [('Horizontal.Progressbar.pbar',
                                  {'side': 'left'})],
                    }),
                  ('Horizontal.Progressbar.label', {'sticky': ''})])
    # , lightcolor=None, bordercolo=None, darkcolor=None
    style.configure('text.Horizontal.TProgressbar', text='0 %', background='green')

    progressBar = ttk.Progressbar(frame1, style='text.Horizontal.TProgressbar', maximum=len(urls))
    progressBar.pack(fill=X, padx=(10, 50), pady=50)
    Button(frame1, text="Start", font=('Times', '16'), command=lambda: runActions(var, style, progressBar, my_window),
           relief="raised").pack(side=LEFT, padx=(50, 0), pady=50)

    frame2 = Frame(mainview, bg="#EFEEEB")
    frame2.pack(fill=X)
    Label(frame2, text='Output:', fg='black', bg="#EFEEEB", font=('Times', '20')).pack(side=LEFT, padx=50)

    outputview = Frame(mainview, width=w - w / 10, bg="#EFEEEB")
    outputview.pack(fill=BOTH, expand=True)
    output = Message(outputview, font=('Times', '16'), anchor=NW, padx=10, pady=10, textvariable=var, relief="ridge",
                     bd=3)
    output.pack(fill=BOTH, pady=30, padx=50, expand=True)
    my_window.mainloop()
    # ------------------GUI style
