# deprecated

from datetime import datetime
from time import localtime, strftime
import serial

#import paho.mqtt.client as mqtt
#mqttBroker = "192.168.0.196:1883"
#client = mqtt.Client("Temperatura_Zunaj")
#client.connect(mqttBroker)

#client.publish("Temperatura_Zunaj", Zunanja_temperatura)

i = 1
while 0 < 1:
    try:
        ser = serial.Serial('/dev/ttyS0', 9600)
        s = ser.readline(100)
        x = strftime("%Y-%m-%d %H:%M:%S", localtime())
        y = strftime("%d-%m-%Y %H:%M:%S", localtime())
        b = s.decode('utf-8')

        a = (len(b))
        #print (a)
        #print (b)
        d = b[1:][:-10]
        if a < 86:
            (f) = str(str(b[0:][:-72]) + (" ") + str(b[13:]))
            #print (str("f=") + (f))
            (b) = (f)
            #print (str("b=") + (b))


        #c = b[1:][:-5]
        zalogovnik1 = b[1:][:-83]
        zalogovnik2 = b[4:][:-80]
        zalogovnik3 = b[7:][:-77]
        zalogovnik4 = b[10:][:-74]
        zunanja_temp = b[13:][:-68]
        pec_f = b[19:][:-65]
        pec_r = b[22:][:-62]
        bojler_f = b[25:][:-59]
        bojler_r = b[28:][:-56]
        bojler_pumpa = b[31:][:-54]
        kopalnica_set = b[33:][:-51]
        kopalnica_f = b[36:][:-48]
        kopalnica_r = b[39:][:-45]
        kopalnica_pumpa = b[42:][:-43]
        sobe_set = b[44:][:-40]
        sobe_f = b[47:][:-37]
        sobe_r = b[50:][:-34]
        sobe_pumpa = b[53:][:-32]
        dnevna_set = b[55:][:-29]
        dnevna_f = b[58:][:-26]
        dnevna_r = b[61:][:-23]
        dnevna_pumpa = b[64:][:-21]
        izba_set = b[66:][:-18]
        izba_f = b[69:][:-15]
        izba_r = b[72:][:-12]
        izba_pumpa = b[75:][:-10]
        kopalnica = b[77:][:-8]
        sobe = b[78:][:-7]
        dnevna = b[79:][:-6]
        izba = b[80:][:-5]

        if bojler_pumpa == "1":
            bojler_pumpa = "off"
        elif bojler_pumpa == "0":
            bojler_pumpa = "on"

        if kopalnica_pumpa == "1":
            kopalnica_pumpa = "off"
        elif kopalnica_pumpa == "0":
            kopalnica_pumpa = "on"
        if kopalnica == "1":
            kopalnica = "vklopljena _"
        elif kopalnica == "0":
            kopalnica = "izklopljena "

        if sobe_pumpa == "1":
            sobe_pumpa = "off"
        elif sobe_pumpa == "0":
            sobe_pumpa = "on"
        if sobe == "1":
           sobe = "vklopljena _"
        elif sobe == "0":
            sobe = "izklopljena "

        if dnevna_pumpa == "1":
            dnevna_pumpa = "off"
        elif dnevna_pumpa == "0":
            dnevna_pumpa = "on"
        if dnevna == "1":
           dnevna = "vklopljena _"
        elif dnevna == "0":
            dnevna = "izklopljena "

        if izba_pumpa == "1":
            izba_pumpa = "off"
        elif izba_pumpa == "0":
            izba_pumpa = "on"
        if izba == "1":
            izba = "vklopljena _"
        elif izba == "0":
            izba = "izklopljena "


        str_za_datoteko = str(x) + (",") + str(d) + '\n'

        f = open("data.csv", "a")
        f.write(str_za_datoteko)
        f.close()

        trenutna = open('trenutna.txt', 'w')
        trenutna.write(str_za_datoteko)
        trenutna.close()

        # print(str_za_datoteko)
        print(" ")
        print(str(x) + (",") + str(d))
        print(" ")
        print(str(y))
        print(str("zalogovnik __________ ") + str(zalogovnik1) + ("°C, ") +
              str(zalogovnik2) + ("°C, ") + str(zalogovnik3) + ("°C, ") + str(zalogovnik4) + ("°C"))
        print(str("zunanja temperatura _ ") + str(zunanja_temp) + ("°C"))
        print(str("peč ________________________ ") +
              str(pec_f) + ("°C, ") + str(pec_r) + ("°C"))
        print(str("bojler _____________________ ") + str(bojler_f) +
              ("°C, ") + str(bojler_r) + ("°C ") + str(bojler_pumpa))
        print(str("kopalnica ") + str(kopalnica) + "___ " + str(kopalnica_set) + ("/") +
              str(kopalnica_f) + ("°C, ") + str(kopalnica_r) + ("°C ") + str(kopalnica_pumpa))
        print(str("sobe ") + str(sobe) + "________ " + str(sobe_set) + ("/") +
              str(sobe_f) + ("°C, ") + str(sobe_r) + ("°C ") + str(sobe_pumpa))
        print(str("dnevna ") + str(dnevna) + "______ " + str(dnevna_set) + ("/") +
              str(dnevna_f) + ("°C, ") + str(dnevna_r) + ("°C ") + str(dnevna_pumpa))
        print(str("izba ") + str(izba) + "________ " + str(izba_set) + ("/") +
              str(izba_f) + ("°C, ") + str(izba_r) + ("°C ") + str(izba_pumpa))

        #str_za_send = chr(2) + ("SETsobe+1") + chr(13)
        # ser.write(str_za_send.encode('utf-8'))
        #print("poslano " + str_za_send + "\n")

#MQTT
#client.publish("Temperatura_Zunaj", Zunanja_temperatura)
#client.connect("192.168.0.196")
#client.loop_start()

#client.publish("/kurilnica/zunanja temperatura", zunanja_temp)


    except KeyboardInterrupt as err:
        predznak = -1
        while predznak < 0:
            beseda = str(input("Vpiši komando: "))
            predznak = beseda.find("+")
            vrsta = "+"
            if predznak < 0:
                predznak = beseda.find("-")
                vrsta = "-"

        vrednost = int(beseda[predznak+1:])
        while vrednost < 1 or vrednost > 9:
            if vrednost < 1:
                vrednost = 1
            elif vrednost > 9:
                vrednost = 9

        soba = beseda[:predznak]

        validSobe = ["kopa", "sobe", "dnev", "izba", "p.ko", "p.so", "p.dn", "p.iz"]
        prostorCode = soba[:4]
        if (prostorCode in validSobe):
            posljiStr = chr(2) + "SET" + prostorCode + vrsta + str(vrednost) + chr(13)
            ser.write(posljiStr.encode('utf-8'))
            print("poslano: " + posljiStr)
            #print(posljiStr)
            #print("poslano: ")
        else:
            print("Vpisal si napačno komando!")

        #posljiStr = chr(2) + "SET" + prostorCode + vrsta + str(vrednost) + chr(13)
        #ser.write(posljiStr.encode('utf-8'))
        #print(posljiStr)