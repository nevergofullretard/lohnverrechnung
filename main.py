import tkinter
import csv
import os
import datetime
import calendar


def startbildschirm():
    destroy_all()
    top.geometry("500x500")
    button_lohn = tkinter.Button(top, text='Lohn berechnen')
    button_lohn.pack()
    button_lohn.bind("<Button-1>", handle_ma_verrechnen)

    button_mitarbeiter = tkinter.Button(top, text='Mitarbeiter anlegen')
    button_mitarbeiter.pack()
    button_mitarbeiter.bind('<Button-1>', handle_mitarbeiter)

    datum = tkinter.Label(top, text=datetime.date.today())
    datum.place(x=430, y=10)

class Brutto_Netto:
    def __init__(self, brutto, sv_dna, lst, gw, e_card):
        self.brutto = brutto
        self.sv_dna = sv_dna
        self.lst = lst
        self.gw = gw
        self.e_card = e_card

    def brutto_netto_berechnen(self):
        netto_ergebnis = self.brutto - self.sv_dna - self.lst - self.gw - self.e_card
        return netto_ergebnis


class Lst:
    def __init__(self, kind_ja_nein, bmg, kinder, brutto):
        self.kind = kind_ja_nein
        self.bmg = bmg
        self.kinder = kinder
        self.brutto = brutto

    def lst_berechnen(self):
        lst_betrag = None
        if self.brutto <= 1066:
            lst_betrag = 0
        elif self.brutto <= 1516:
            lst_betrag = self.bmg * 0.25
        elif self.brutto <= 2599.33:
            lst_betrag = self.bmg * 0.35
        elif self.brutto <= 5016:
            lst_betrag = self.bmg * 0.42
        elif self.brutto <= 7516:
            lst_betrag = self.bmg * 0.48
        elif self.brutto <= 83349.33:
            lst_betrag = self.bmg * 0.5
        elif self.brutto > 83349.33:
            lst_betrag = self.bmg * 0.55


        if self.kind == 'Nein':
            if self.brutto <= 1066:
                lst_betrag = 0
            elif self.brutto <= 1516:
                lst_betrag = lst_betrag - 266.5
            elif self.brutto <= 2599.33:
                lst_betrag = lst_betrag - 418.1
            elif self.brutto <= 5016:
                lst_betrag = lst_betrag - 600.05
            elif self.brutto <= 7516:
                lst_betrag = lst_betrag - 901.01
            elif self.brutto <= 83349.33:
                lst_betrag = lst_betrag - 1051.33
            elif self.brutto > 83349.33:
                lst_betrag = lst_betrag - 5218.8

        if self.kind == 'Ja':
            wie_viele = self.kinder
            if wie_viele == 1:
                if self.brutto <= 1066:
                    lst_betrag = 0
                elif self.brutto <= 1516:
                    lst_betrag = lst_betrag - 307.67
                elif self.brutto <= 2599.33:
                    lst_betrag = lst_betrag - 459.27
                elif self.brutto <= 5016:
                    lst_betrag = lst_betrag - 641.22
                elif self.brutto <= 7516:
                    lst_betrag = lst_betrag - 942.18
                elif self.brutto <= 83349.33:
                    lst_betrag = lst_betrag - 1092.5
                elif self.brutto > 83349.33:
                    lst_betrag = lst_betrag - 5259.97
            if wie_viele == 2:
                if self.brutto <= 1066:
                    lst_betrag = 0
                elif self.brutto <= 1516:
                    lst_betrag = lst_betrag - 322.25
                elif self.brutto<= 2599.33:
                    lst_betrag = lst_betrag - 473.85
                elif self.brutto <= 5016:
                    lst_betrag = lst_betrag - 655.8
                elif self.brutto <= 7516:
                    lst_betrag = lst_betrag - 956.76
                elif self.brutto <= 83349.33:
                    lst_betrag = lst_betrag - 1107.08
                elif self.brutto > 83349.33:
                    lst_betrag = lst_betrag - 5274.55
            if wie_viele == 3:
                if self.brutto <= 1066:
                    lst_betrag = 0
                elif self.brutto <= 1516:
                    lst_betrag = lst_betrag - 340.58
                elif self.brutto <= 2599.33:
                    lst_betrag = lst_betrag - 492.18
                elif self.brutto <= 5016:
                    lst_betrag = lst_betrag - 674.14
                elif self.brutto <= 7516:
                    lst_betrag = lst_betrag - 975.1
                elif self.brutto <= 83349.33:
                    lst_betrag = lst_betrag - 1125.42
                elif self.brutto > 83349.33:
                    lst_betrag = lst_betrag - 5292.88
            if wie_viele == 4:
                if self.brutto <= 1066:
                    lst_betrag = 0
                elif self.brutto <= 1516:
                    lst_betrag = lst_betrag - 358.92
                elif self.brutto <= 2599.33:
                    lst_betrag = lst_betrag - 510.52
                elif self.brutto <= 5016:
                    lst_betrag = lst_betrag - 692.48
                elif self.brutto <= 7516:
                    lst_betrag = lst_betrag - 993.43
                elif self.brutto <= 83349.33:
                    lst_betrag = lst_betrag - 1143.76
                elif self.brutto > 83349.33:
                    lst_betrag = lst_betrag - 5311.22
            if wie_viele == 5:
                if self.brutto <= 1066:
                    lst_betrag = 0
                elif self.brutto <= 1516:
                    lst_betrag = lst_betrag - 377.25
                elif self.brutto <= 2599.33:
                    lst_betrag = lst_betrag - 528.85
                elif self.brutto <= 5016:
                    lst_betrag = lst_betrag - 710.81
                elif self.brutto <= 7516:
                    lst_betrag = lst_betrag - 1011.77
                elif self.brutto <= 83349.33:
                    lst_betrag = lst_betrag - 1162.09
                elif self.brutto > 83349.33:
                    lst_betrag = lst_betrag - 5329.55

        print('das ist die Lohnsteuer:  ' + str(lst_betrag))
        return lst_betrag


class Bmg:
    def __init__(self, brutto, fb, e_card, gw, pp_km, pp_zmb_oder_nicht, sachbezug, ue_steuerfrei):
        self.fb = fb
        self.pp = pp_zmb_oder_nicht
        self.pp_km = pp_km
        self.e_card = e_card
        self.gw = gw
        self.sachbezug = sachbezug
        self.brutto = brutto
        self.ue_steuerfrei = ue_steuerfrei



    def bmg_berechnen(self):

        sv_dna = None

        if self.brutto <= 1342:
            sv_dna = (self.brutto + self.sachbezug) * 0.1512
        elif self.brutto <= 1464:
            sv_dna = (self.brutto + self.sachbezug) * 0.1612
        elif self.brutto <= 1648:
            sv_dna = (self.brutto + self.sachbezug) * 0.1712
        elif self.brutto > 1648:
            sv_dna = (self.brutto + self.sachbezug) * 0.1812
        #hier brauchen wir noch den Betrag für über 4980 brutto im Monat

        pp_betrag = None

        if self.pp == 'zumutbar':
            if self.pp_km > 60:
                pp_betrag = 168
            elif self.pp_km > 40:
                pp_betrag = 113
            elif self.pp_km >= 20:
                pp_betrag = 58
            elif self.pp_km < 20:
                pp_betrag = 0
        elif self.pp == 'nicht zumutbar':
            if self.pp_km > 60:
                pp_betrag = 306
            elif self.pp_km > 40:
                pp_betrag = 214
            elif self.pp_km > 20:
                pp_betrag = 123
            elif self.pp_km >= 2:
                pp_betrag = 31
            elif self.pp_km < 2:
                pp_betrag = 0
        print(pp_betrag)


        print('das ist der Bruttobetrag ' + str(self.brutto))

        # hier noch freilassen für Pendlereuro

        bmg_fuer_lst = self.brutto + self.sachbezug - sv_dna - self.fb - self.e_card - self.gw - pp_betrag - self.ue_steuerfrei
        dic_return_bmg = {'bmg': bmg_fuer_lst, 'pp_km': self.pp_km, 'sachbezug': self.sachbezug, 'fb': self.fb, 'e_card': self.e_card,
                          'gw': self.gw, 'sv_dna': sv_dna, 'pp_betrag': pp_betrag}
        return dic_return_bmg

class Ueberstunden:
    def __init__(self , ue_50, ue_100,ue_teiler_stundenlohn, teiler_std_betrag, grundbezug):
        self.ue_50 = ue_50
        self.ue_100 = ue_100
        self.ue_teiler = ue_teiler_stundenlohn
        self.teiler_std_betrag = teiler_std_betrag
        self.grundbezug = grundbezug

    def ueberstunden(self):

        if self.ue_teiler == 'ÜT':
            gb_teiler_stdlohn = self.grundbezug / self.teiler_std_betrag
        elif self.ue_teiler == 'SL':
            gb_teiler_stdlohn = self.teiler_std_betrag

        ue_g = self.ue_50 * gb_teiler_stdlohn + self.ue_100 * gb_teiler_stdlohn
        ue_z_50 = self.ue_50 * gb_teiler_stdlohn / 2
        ue_z_100 = self.ue_100 * gb_teiler_stdlohn
        ueberstunden_summe = ue_g + ue_z_50 + ue_z_100

        ue_steuerfrei = None
        if self.ue_50 <= 10 and ue_z_50 <= 86:
            ue_steuerfrei = ue_z_50  # noch mal drüberschauen, ob das nicht die function verändert
        elif self.ue_50 > 10 and ue_z_50 <= 86:
            ue_steuerfrei = gb_teiler_stdlohn / 2 * 10
        elif self.ue_50 < 10 and ue_z_50 > 86:
            ue_steuerfrei = 86
        elif self.ue_50 > 10 and ue_z_50 > 86:
            ue_steuerfrei = 86
        if ue_z_100 <= 360:
            ue_steuerfrei += ue_z_100
        elif ue_z_100 > 360:
            ue_steuerfrei += 360
        print('Das ist der steuerfreie Betrag ' + str(ue_steuerfrei))
        print(str(self.grundbezug) + ' ' + str(ueberstunden_summe) + ' ' + str(ue_steuerfrei))

        ergebnis = self.grundbezug + ueberstunden_summe
        dic_return_ue = {'ergebnis': ergebnis, 'brutto': self.grundbezug, 'ue_summe': ueberstunden_summe, 'ue_steuerfrei': ue_steuerfrei,
                         'ue_g': ue_g, 'ue_50': ue_z_50, 'ue_100': ue_z_100}
        return dic_return_ue

def destroy_bestimmtes(*args):
    for element in args:
        for widget in top.winfo_children():
            if widget != element:
                widget.destroy()
            else:
                print('what the hell')

def destroy_all():
    for widget in top.winfo_children():
            if widget != datum:
                widget.destroy()

def handle_ma_verrechnen(event):
    destroy_all()
    top.geometry("500x500")
    ma_vorname_text = tkinter.Label(top, text='Vorname:')
    ma_vorname_text.place(x=10, y=10)
    ma_vorname = tkinter.Entry(top, text='')
    ma_vorname.place(x=150, y=10)
    ma_nachname_text = tkinter.Label(top, text='Nachname')
    ma_nachname_text.place(x=10, y=50)
    ma_nachname = tkinter.Entry(top, text='')
    ma_nachname.place(x=150, y=50)
    ma_verrechnen = tkinter.Button(top, text='Mitarbeiter verrechnen', command=lambda :handle_ma_exists(str(ma_vorname.get()), str(ma_nachname.get())))
    ma_verrechnen.place(x=10, y=80)

    def handle_ma_exists(vorname, nachname):
        destroy_all()
        ma_vorname_label = tkinter.Label(top, text='Vorname:    ' + vorname)
        ma_vorname_label.place(x=10, y=10)
        ma_nachname_label = tkinter.Label(top, text='Nachname:  ' + nachname)
        ma_nachname_label.place(x=10, y=40)

        folder_name = vorname + '_' + nachname

        if os.path.exists(folder_name):
            ma_exists = tkinter.Label(top, text='Dieser Mitarbeiter existiert!')
            ma_exists.place(x=10, y=80)


            month_now = [1,2,3,4,5,6,7,8,9,10,11,12]
            month_num = 0
            year_now = 2018

            month = tkinter.Button(top, text=calendar.month_name[month_now[month_num]], command=lambda :handle_month())
            month.place(x=10, y=130)

            year = tkinter.Label(top, text=year_now)
            year.place(x=120, y=130)

            forward = tkinter.Button(top, text='vor', command=lambda :year_forward())
            forward.place(x=150, y=155)

            backward = tkinter.Button(top, text='zurück', command= lambda :year_backward())
            backward.place(x=100, y=155)

            zu_lohnverrechnung = tkinter.Button(top, text='Fortfahren',
                                       command=lambda: handle_button_lohn(vorname, nachname,month_now[month_num], year_now))
            zu_lohnverrechnung.place(x=10, y=300)

            def handle_month():
                nonlocal month_num, month_now
                month_num += 1
                try:
                    month['text'] = calendar.month_name[month_now[month_num]]
                except IndexError:
                    month_num = 0
                    month['text'] = calendar.month_name[month_now[0]]


            def year_forward():
                nonlocal year_now
                year_now += 1
                year['text'] = year_now

            def year_backward():
                nonlocal year_now
                year_now -= 1
                year['text'] = year_now

        elif not os.path.exists(folder_name):
            top.geometry('700x700')
            listdir = os.listdir(os.getcwd())

            zahl1 = 0
            zeile = 0

            range_listdir = range(len(listdir))
            with open('mitarbeiter_ordner.csv', 'w', newline='') as ma_ordner:
                filewriter = csv.writer(ma_ordner, delimiter=';')
                listdir_only_folders = []
                for folder in listdir:
                    if folder != '__pycache__' and folder != 'all_in_one.py' and folder != '__pycache__' \
                            and folder != '_' and folder != 'mitarbeiter.csv' and folder != 'mitarbeiter_ordner.csv' \
                            and folder != '.idea':
                                listdir_only_folders.append(folder)
                try:
                    while zahl1 < len(listdir_only_folders):
                        filewriter.writerow([listdir_only_folders[zahl1], listdir_only_folders[zahl1+1], listdir_only_folders[zahl1+2]])
                        zahl1 += 3
                except IndexError:
                    if zahl1 == len(listdir_only_folders) -1:
                        filewriter.writerow([listdir_only_folders[-1]])
                    elif zahl1 == len(listdir_only_folders) -2:
                        filewriter.writerow([listdir_only_folders[-1], listdir_only_folders[-2]])






            with open("mitarbeiter_ordner.csv", newline='') as file:
                reader = csv.reader(file, delimiter=';')

                # r and c tell us where to grid the labels
                r = 0
                for col in reader:
                    c = 0
                    for row in col:
                        # i've added some styling
                        label = tkinter.Label(top, width=20, height=2, \
                                              text=row, relief=tkinter.RIDGE)
                        label.grid(row=r, column=c)
                        c += 1
                    r += 1

            ma_not_exists = tkinter.Label(top,
                                          text='Der Mitarbeiter ' + vorname + ' ' + nachname + ' existiert leider nicht,\n '
                                                                                               'oben ist eine Liste der Mitarbeiter.')
            ma_not_exists.grid(row=r+1, column=1)
            neuer_versuch = tkinter.Button(top, text='Neuer Versuch', command=lambda :handle_ma_verrechnen('sepp'))
            neuer_versuch.grid(row=r+2, column=1)


def handle_button_lohn(vorname, nachname, monat, jahr):
    destroy_all()
    print(monat)
    print(jahr)

    ma_vorname_label = tkinter.Label(top, text='Vorname :    ' + vorname)
    ma_vorname_label.place(x=10, y=10)
    ma_nachname_label = tkinter.Label(top, text='Nachname :  ' + nachname)
    ma_nachname_label.place(x=10, y=40)
    ma_monat = tkinter.Label(top, text=calendar.month_name[monat])
    ma_monat.place(x=150, y=10)
    ma_year = tkinter.Label(top, text=jahr)
    ma_year.place(x=150, y=40)
    bruttoText = tkinter.Label(top, text="Brutto:")
    bruttoText.place(x=10, y=80)
    bruttobetrag = tkinter.Entry(top, text='')
    bruttobetrag.place(x=150, y=80)

    ue_50 = tkinter.Entry(top, text='')
    ue_50.place(x=150, y=120)
    ue_50_text = tkinter.Label(top, text='Überstunden 50 %')
    ue_50_text.place(x=10, y=120)

    ue_100 = tkinter.Entry(top, text='')
    ue_100.place(x=150, y=160)
    ue_100_text = tkinter.Label(top, text='Überstunden 100 %')
    ue_100_text.place(x=10, y=160)

    üt_button = tkinter.Button(top, text='Überstundenteiler', command=lambda: üt_function('ÜT'))
    üt_button.place(x =10, y=200)

    sl_button = tkinter.Button(top, text='Stundenlohn', command = lambda:sl_function('SL'))
    sl_button.place(x=175, y=200)

    sl_text = tkinter.Label(top, text='Stundenlohn:')
    sl_text.place_forget()
    sl_betrag = tkinter.Entry(top, text='')
    sl_betrag.place_forget()
    rechnen_button = tkinter.Button(top, text='Berechnen')
    rechnen_button.place_forget()

    üt_text = tkinter.Label(top, text='Überstundenteiler:')
    üt_text.place_forget()
    üt_betrag = tkinter.Entry(top, text='')
    üt_betrag.place_forget()


    dic_üt = {}

    def üt_function(string):
        üt_button.place_forget()
        sl_button.place_forget()
        üt_text.place(x=10, y=200)
        üt_betrag.place(x=150, y=200)
        rechnen_button.place(x=175, y=240)
        rechnen_button.bind("<Button-1>", calculate_ue)
        dic_üt['üt_text']= string
        dic_üt['üt_betrag'] = üt_betrag

    def sl_function(string):
        üt_button.place_forget()
        sl_button.place_forget()
        sl_text.place(x=10, y=200)
        sl_betrag.place(x=150, y=200)
        rechnen_button.place(x=175, y=240)
        rechnen_button.bind("<Button-1>", calculate_ue)
        dic_üt['üt_text']= string
        dic_üt['üt_betrag'] = sl_betrag


    def calculate_ue(event):
        u_50 = float(ue_50.get())
        u_100 = float(ue_100.get())
        brutto = float(bruttobetrag.get())
        teiler_st_betrag = float(dic_üt['üt_betrag'].get())
        ue_class = Ueberstunden(u_50, u_100, dic_üt['üt_text'], teiler_st_betrag, brutto)
        ue_calc = ue_class.ueberstunden()
        print(ue_calc)
        bruttoText.place_forget()
        bruttobetrag.place_forget()
        ue_50.place_forget()
        ue_50_text.place_forget()
        ue_100.place_forget()
        ue_100_text.place_forget()
        sl_text.place_forget()
        sl_betrag.place_forget()
        üt_text.place_forget()
        üt_betrag.place_forget()
        rechnen_button.place_forget()

        brutto_label = tkinter.Label(top, text="Brutto:      " + str(ue_calc['ergebnis']))
        brutto_label.place(x=10, y=80)
        ue_50_label = tkinter.Label(top, text='Überstunden 50 % :     ' + str(ue_calc['ue_50']))
        ue_50_label.place(x=10, y=100)
        ue_100_label = tkinter.Label(top, text='Überstunden 100 % :     ' + str(ue_calc['ue_100']))
        ue_100_label.place(x=10, y=120)

        fb_text = tkinter.Label(top, text='Freibetrag:')
        fb_text.place(x=10, y=160)
        fb_betrag = tkinter.Entry(top, text='')
        fb_betrag.place(x=150, y=160)
        ecard_text = tkinter.Label(top, text='E-Card:')
        ecard_text.place(x=10, y=200)
        ecard_betrag = tkinter.Entry(top, text='')
        ecard_betrag.place(x=150, y=200)
        gw_text = tkinter.Label(top, text='Gewerkschaftsbeitrag:')
        gw_text.place(x=10, y=240)
        gw_betrag = tkinter.Entry(top, text='')
        gw_betrag.place(x=150, y=240)
        sachbezug_text = tkinter.Label(top, text='Sachbezug:')
        sachbezug_text.place(x=10, y=280)
        sachbezug_betrag = tkinter.Entry(top, text='')
        sachbezug_betrag.place(x=150, y=280)
        pp_km_text = tkinter.Label(top, text='Kilometer für PP:')
        pp_km_text.place(x=10, y=320)
        pp_km_betrag = tkinter.Entry(top, text='')
        pp_km_betrag.place(x=150, y= 320)
        pp_zumut = tkinter.Button(top, text='PP zumutbar',  command = lambda:func_pp_zumut('zumutbar'))
        pp_zumut.place(x=15, y=360)
        pp_not_zumut = tkinter.Button(top, text='PP nicht zumutbar', command= lambda: func_pp_not_zumut('nicht zumutbar'))
        pp_not_zumut.place(x=160, y=360)

        bmg_berechnen = tkinter.Button(top, text='BMG berechnen')
        bmg_berechnen.place_forget()

        dic_pp = {}

        def func_pp_zumut(string):
            pp_zumut.place_forget()
            pp_not_zumut.place_forget()
            dic_pp['zmb_oder_nicht'] = string
            bmg_berechnen.place(x=10, y=400)
            bmg_berechnen.bind('<Button-1>', calculate_bmg)

        def func_pp_not_zumut(string):
            pp_not_zumut.place_forget()
            pp_zumut.place_forget()
            dic_pp['zmb_oder_nicht'] = string
            bmg_berechnen.place(x=10, y=400)
            bmg_berechnen.bind('<Button-1>', calculate_bmg)

        def calculate_bmg(event):
            fb = float(fb_betrag.get())
            ecard = float(ecard_betrag.get())
            gw = float(gw_betrag.get())
            pp_km = float(pp_km_betrag.get())
            sachbezug = float(sachbezug_betrag.get())

            bmg_class = Bmg(ue_calc['brutto'], fb, ecard, gw, pp_km,dic_pp['zmb_oder_nicht'], sachbezug, ue_calc['ue_steuerfrei'])
            bmg_calc = bmg_class.bmg_berechnen()
            print(bmg_calc)
            fb_text.place_forget()
            fb_betrag.place_forget()
            ecard_betrag.place_forget()
            ecard_text.place_forget()
            gw_betrag.place_forget()
            gw_text.place_forget()
            sachbezug_betrag.place_forget()
            sachbezug_text.place_forget()
            pp_km_betrag.place_forget()
            pp_km_text.place_forget()
            bmg_berechnen.place_forget()
            sachbezug_label = tkinter.Label(top, text='Sachbezug:   ' + str(bmg_calc['sachbezug']))
            sachbezug_label.place(x=10, y=140)
            fb_label = tkinter.Label(top, text='Freibetrag:     ' + str(bmg_calc['fb']))
            fb_label.place(x=10, y=160)
            ecard_label = tkinter.Label(top, text='E-Card:  ' + str(bmg_calc['e_card']))
            ecard_label.place(x=10, y=180)
            gw_label = tkinter.Label(top, text='Gewerkschaftsbeitrag:   ' + str(bmg_calc['gw']))
            gw_label.place(x=10, y=200)
            sv_dna_label = tkinter.Label(top, text='Sozialversicherung:     ' + str(bmg_calc['sv_dna']))
            sv_dna_label.place(x=10, y=220)
            pp_betrag_label = tkinter.Label(top, text='Pendlerpauschale:    ' + str(bmg_calc['pp_betrag']))
            pp_betrag_label.place(x=10, y=240)
            bmg_label = tkinter.Label(top, text='Lst-Bemessungsgrundlage:   ' + str(bmg_calc['bmg']))
            bmg_label.place(x=10, y=260)
            kind_ja_nein = tkinter.Label(top, text='Haben Sie Kinder?')
            kind_ja_nein.place(x=10, y=300)
            kind_ja = tkinter.Button(top, text='JA', command= lambda:func_kind_ja('Ja'))
            kind_ja.place(x=150, y=300)
            kind_nein = tkinter.Button(top, text='NEIN', command=lambda : func_kind_nein('Nein'))
            kind_nein.place(x=200, y=300)

            lst_berechnen_button = tkinter.Button(top, text='Lohn berechnen')
            lst_berechnen_button.place_forget()

            dic_kind = {}
            dic_kind_anzahl = {}

            def func_kind_ja(string):
                kind_ja.place_forget()
                kind_nein.place_forget()
                kind_ja_nein.place_forget()
                dic_kind['kind'] = string
                kind_anzahl = tkinter.Label(top, text='Wie viele Kinder haben Sie?')
                kind_anzahl.place(x=10, y=300)

                kind_1 = tkinter.Button(top, text='1', command=lambda :func_kind(1))
                kind_1.place(x=200, y=300)
                kind_2 = tkinter.Button(top, text='2', command=lambda: func_kind(2))
                kind_2.place(x=220, y=300)
                kind_3 = tkinter.Button(top, text='3', command=lambda: func_kind(3))
                kind_3.place(x=240, y=300)
                kind_4 = tkinter.Button(top, text='4', command=lambda: func_kind(4))
                kind_4.place(x=260, y=300)
                kind_5 = tkinter.Button(top, text='5', command=lambda: func_kind(5))
                kind_5.place(x=280, y=300)

                def func_kind(string):
                    kind_1.place_forget()
                    kind_2.place_forget()
                    kind_3.place_forget()
                    kind_4.place_forget()
                    kind_5.place_forget()
                    kind_anzahl.place_forget()
                    dic_kind_anzahl['kinder'] = string
                    lst_berechnen_button.place(x=10, y=300)
                    lst_berechnen_button.bind('<Button-1>', calculate_lst)

            def func_kind_nein(string):
                kind_ja.place_forget()
                kind_nein.place_forget()
                kind_ja_nein.place_forget()
                dic_kind['kind'] = string
                lst_berechnen_button.place(x=10, y=300)
                lst_berechnen_button.bind('<Button-1>', calculate_lst)
                dic_kind_anzahl['kinder'] = 0

            def calculate_lst(event):

                lst_berechnen_button.place_forget()
                lst_class = Lst(dic_kind['kind'], bmg_calc['bmg'], dic_kind_anzahl['kinder'],ue_calc['brutto'])
                lst_calc = lst_class.lst_berechnen()

                lst_label = tkinter.Label(top, text='Lohnsteuer-Betrag:     ' + str(lst_calc))
                lst_label.place(x=10, y=340)

                class_brutto_netto =Brutto_Netto(ue_calc['brutto'], bmg_calc['sv_dna'], lst_calc, bmg_calc['gw'],bmg_calc['e_card'])
                brutto_netto_calc = class_brutto_netto.brutto_netto_berechnen()


                ma_path = os.getcwd() + '\\' + vorname + '_' + nachname
                file_name = ma_path + '\\' + 'Lohn_' +nachname+'_'+vorname+'_'+ str(jahr)+'-'+str(monat)+'.csv'

                with open(file_name, 'w', newline='') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=';')
                    filewriter.writerow(['Nachname:', nachname,'', 'Jahr:', jahr,'',''])
                    filewriter.writerow(['Vorname:', vorname,'','Monat:', calendar.month_name[monat],'',''])
                    filewriter.writerow(['Brutto','','','','','',ue_calc['brutto']])
                    filewriter.writerow(['Überstundengrundlohn','','','','','',ue_calc['ue_g']])
                    filewriter.writerow(['Überstunden zu 50 %','','','','','',ue_calc['ue_50']])
                    filewriter.writerow(['Überstunden zu 100 %','','','','','', ue_calc['ue_100']])
                    filewriter.writerow(['Gesamtbrutto','','','','','',ue_calc['ergebnis']])
                    filewriter.writerow(['','' ,'' ,'' ,'' ,'' ,''])
                    filewriter.writerow([' - SV-DNA', 'Brutto', 3450,'','' ,'' ,''])
                    filewriter.writerow(['',' + Sachbezug', 200, 'SV - Prozentsatz','', '',''])
                    filewriter.writerow(['', 'SV - Grundlage', 3650, 18.12,'','' , 902])
                    filewriter.writerow(['','' ,'' ,'' ,'' ,'' ,''])
                    filewriter.writerow([' - Lohnsteuer', 'Brutto', 3450,'','' ,'' ,''])
                    filewriter.writerow(['',' + Sachbezug', 200,'', '', '',''])
                    filewriter.writerow(['',' - UZ - Steuerfrei', 55,'','' ,'' ,''])
                    filewriter.writerow(['',' - FB', 50,'', '', '',''])
                    filewriter.writerow(['',' - E - Card', 30,'','' ,'' ,''])
                    filewriter.writerow(['',' - GW', 33,'', '', '',''])
                    filewriter.writerow(['',' - SV', 902,'','' ,'' ,''])
                    filewriter.writerow(['',' - PP', 123,' Lohnsteuer - Prozentsatz',' - Lohnsteuer - Abzug',' - Pendlereuro',''])
                    filewriter.writerow(['',' BMG', 2500, 42, 300, 5, 950])
                    filewriter.writerow(['','' ,'' ,'' ,'' ,'' ,''])
                    filewriter.writerow([' -GW','','','' ,'' ,'' , 33])
                    filewriter.writerow([' - E-Card','','','' ,'' ,'' , 30])
                    filewriter.writerow(['Gesamtnetto', '','','' ,'' ,'' , 2500])
                top.geometry('920x620')
                with open(file_name, newline='') as file:
                    reader = csv.reader(file, delimiter=';')
                    r = 0
                    for col in reader:
                        c = 0
                        for row in col:
                            label = tkinter.Label(top, width=18, height=1, \
                                                  text=row, relief=tkinter.RIDGE)
                            label.grid(row=r, column=c)
                            c += 1
                        r += 1

                meldung = tkinter.Label(top, text='Der Lohn wurde erfolgreich verrechnet und die Daten gespeichert!')
                meldung.place(x=10, y=530)

                def handle_zum_ornder():
                    os.startfile(ma_path)

                zum_ornder = tkinter.Button(top, text='Zum Ornder', command=lambda :handle_zum_ornder())
                zum_ornder.place(x=10, y=550)

                zum_start = tkinter.Button(top, text='Zurück zum Startbildschirm', command=lambda: startbildschirm())
                zum_start.place(x=10, y=580)


def handle_mitarbeiter(event):
    destroy_all()

    button_mitarbeiter.pack_forget()
    ma_vorname_text = tkinter.Label(top, text='Vorname:')
    ma_vorname_text.place(x=10, y=10)
    ma_vorname = tkinter.Entry(top, text='')
    ma_vorname.place(x=150, y=10)
    ma_nachname_text = tkinter.Label(top, text='Nachname:')
    ma_nachname_text.place(x=10, y=50)
    ma_nachname = tkinter.Entry(top, text='')
    ma_nachname.place(x=150, y=50)


    def handle_ma_anlegen(event):
        top.geometry("700x500")
        ma_anlegen.place_forget()
        ma_vorname_text.place_forget()
        ma_vorname.place_forget()
        ma_nachname_text.place_forget()
        ma_nachname.place_forget()

        vorname = str(ma_vorname.get())
        nachname = str(ma_nachname.get())
        directory = str(vorname + '_' + nachname)

        folder_path = os.getcwd() + '\\' + directory

        if os.path.exists(directory):
            top.geometry('600x200')
            os_error = tkinter.Label(top,
                                     text='Dieser Name existiert bereits, bitte hängen Sie  beim Nachnamen oder Vornamen z.B. ein"_1" an')
            os_error.place(x=10, y=50)

            neuer_versuch = tkinter.Button(top, text='Neuer Versuch')
            neuer_versuch.place(x=10, y=90)
            neuer_versuch.bind('<Button-1>', handle_mitarbeiter)



        if not os.path.exists(directory):
            destroy_all()
            vorname_label = tkinter.Label(top, text='Vorname:   ' + vorname)
            vorname_label.place(x=10, y=40)
            nachname_label = tkinter.Label(top, text='Nachname:  ' + nachname)
            nachname_label.place(x=10, y=65)

            os.makedirs(directory)
            os_succeeded = tkinter.Label(top,
                                         text='Ordnerpfad des Mitarbeiters: ' + folder_path)
            os_succeeded.place(x=10, y=10)

            ma_adresse_text = tkinter.Label(top, text='Adresse:')
            ma_adresse_text.place(x=10, y=90)
            ma_adresse = tkinter.Entry(top, text='')
            ma_adresse.place(x=150, y=90)
            ma_plz_text = tkinter.Label(top, text='PLZ:')
            ma_plz_text.place(x=10, y=130)
            ma_plz = tkinter.Entry(top, text='')
            ma_plz.place(x=150, y= 130)
            ma_ort_text = tkinter.Label(top, text='Ort:')
            ma_ort_text.place(x=10, y=170)
            ma_ort = tkinter.Entry(top, text='')
            ma_ort.place(x=150, y=170)
            ma_telefon_text = tkinter.Label(top, text='Telefon:')
            ma_telefon_text.place(x=10, y=210)
            ma_telefon = tkinter.Entry(top, text='')
            ma_telefon.place(x=150, y=210)
            ma_email_text = tkinter.Label(top, text='E-Mail:')
            ma_email_text.place(x=10, y=250)
            ma_email = tkinter.Entry(top, text='')
            ma_email.place(x=150, y=250)

            personal_data = tkinter.Button(top, text='Persönliche Daten speichern',
                                           command=lambda: handle_button_personal())

            personal_data.place(x=10, y=290)

        def handle_button_personal():
            adresse = str(ma_adresse.get())
            plz = str(ma_plz.get())
            ort = str(ma_ort.get())
            telefon = str(ma_telefon.get())
            email = str(ma_email.get())

            daten_in_ornder = os.path.join(folder_path, 'persönliche_daten_' + directory + '.csv')
            print('Das ist der File-Name: '+ daten_in_ornder)

            with open(daten_in_ornder, 'w', newline='') as personal_csv:
                filewriter = csv.writer(personal_csv, delimiter=';')
                filewriter.writerow(['Vorname:', vorname])
                filewriter.writerow(['Nachname:', nachname])
                filewriter.writerow(['Adresse:', adresse])
                filewriter.writerow(['PlZ:', plz])
                filewriter.writerow(['Ort:', ort])
                filewriter.writerow(['Telefon:', telefon])
                filewriter.writerow(['E-Mail:', email])

            with open('mitarbeiter.csv', 'a', newline='') as mitarbeiter_csv:
                write_file = csv.writer(mitarbeiter_csv, delimiter=';')
                write_file.writerow([vorname,nachname,adresse,plz,ort,telefon,email])

            personal_data.place_forget()
            ma_adresse_text.place_forget()
            ma_adresse.place_forget()
            ma_plz_text.place_forget()
            ma_plz.place_forget()
            ma_ort_text.place_forget()
            ma_ort.place_forget()
            ma_telefon_text.place_forget()
            ma_telefon.place_forget()
            ma_email_text.place_forget()
            ma_email.place_forget()

            ma_erstellt = tkinter.Label(top, text='Der Mitarbeiter wurde erfolgreich erstellt und die Daten gespeichert!')
            ma_erstellt.place(x=10, y=70)

            def handle_zum_ornder():
                os.startfile(folder_path)   # Wichtig! Zeigt, wie man einen Ornder öffnet

            zum_ornder = tkinter.Button(top, text='Zum Ornder', command=lambda: handle_zum_ornder())
            zum_ornder.place(x=10, y=100)

            zum_start = tkinter.Button(top, text='Zurück zum Startbildschirm', command=lambda :startbildschirm())
            zum_start.place(x=10, y=140)



    ma_anlegen = tkinter.Button(top, text='Mitarbeiter anlegen')
    ma_anlegen.place(x=10, y=100)
    ma_anlegen.bind('<Button-1>', handle_ma_anlegen)


top = tkinter.Tk()

top.title("Einfache Lohnverrechnung ")
top.geometry("500x500")

button_lohn = tkinter.Button(top, text= 'Lohn berechnen')
button_lohn.pack()
button_lohn.bind("<Button-1>", handle_ma_verrechnen)

button_mitarbeiter = tkinter.Button(top, text='Mitarbeiter anlegen')
button_mitarbeiter.pack()
button_mitarbeiter.bind('<Button-1>', handle_mitarbeiter)

datum = tkinter.Label(top, text=datetime.date.today())
datum.place(x=430, y=10)

top.mainloop()