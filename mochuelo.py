import sys
import argparse
import os
import socket
import sys
import json
import random
import threading
import base64
import time
from sys import argv
from getpass import getpass
from xml.dom import minidom
from time import gmtime, strftime, sleep

def yesOrNo():
    return (raw_input("Devam et Y / N: ") in yes)

mochuelologo = """

.___  ___.   ______     ______  __    __   __    __  _______  __        ______
|   \/   |  /  __  \   /      ||  |  |  | |  |  |  ||   ____||  |      /  __  |
|  \  /  | |  |  |  | |  ,----'|  |__|  | |  |  |  ||  |__   |  |     |  |  |  |
|  |\/|  | |  |  |  | |  |     |   __   | |  |  |  ||   __|  |  |     |  |  |  |
|  |  |  | |  `--'  | |  `----.|  |  |  | |  `--'  ||  |____ |  `----.|  `--'  |
|__|  |__|  \______/   \______||__|  |__|  \______/ |_______||_______| \______/


"""

class mochuelo:
    def __init__(self):
        print (mochuelologo + '''
             }-----{+} Made with LOVE by kutaygs =) {+}-----{
            }--------{+} kutayyavuz03@hotmail.com {+}--------{
         }-----{+} Program python dilinde yapilmistir. {+}-----{


  ''' '''
             {1}--Giris
             {9}-Cikis\n
             ''')
        choice = raw_input("mochuelo~# ")
        if choice == "1":
            wirelessTestingMenu()
        elif choice == "9":
            sys.exit()
        else:
            print("Hatali Giris")
            self.__init__()
        self.completed()

    def completed(self):
        print("Tamamlandi, geri donmek icin tiklayiniz")
        self.__init__()

done = 'false'

def Insta():
    print("   Instagram kullanici adi:")
    choice5 = raw_input("mochuelo~# ")
    print (choice5) + (" Bot Basladi")
    INSTAanimate()

def dos():
    print("   IP Adresi Girin")
    choice6 = raw_input("mochuelo~# ")
    print (choice6) + (" Saldiri Basladi")
    DOSanimate()

def polis():
    print("   Bulundugunuz Sehiri Yazin")
    choice7 = raw_input("mochuelo~# ")
    print (choice7) + (" Icin Arama Baslatildi")
    Panimate()

def tel():
    print("   Telefon Numarasi Girin")
    choice8 = raw_input("mochuelo~# ")
    print (choice8) + (" Icin Dinleme Baslatildi")
    TELanimate()

def face():
    print("   Facebook Mail Girin")
    choice8 = raw_input("mochuelo~# ")
    print (choice8) + (" Icin Bruteforca Baslatildi")
    FACEanimate()

def animate():
    while done == 'false':
        sys.stdout.write('\rYukleniyor, lutfen bekleyiniz... |')
        time.sleep(0.1)
        sys.stdout.write('\rYukleniyor, lutfen bekleyiniz... /')
        time.sleep(0.1)
        sys.stdout.write('\rYukleniyor, lutfen bekleyiniz... -')
        time.sleep(0.1)
        sys.stdout.write('\rYukleniyor, lutfen bekleyiniz... \\')
        time.sleep(0.1)
    sys.stdout.write('\r ')



def DOSanimate():
    while done == 'false':
        sys.stdout.write('\rSaldiriyor... |')
        time.sleep(0.1)
        sys.stdout.write('\rSaldiriyor... /')
        time.sleep(0.1)
        sys.stdout.write('\rSaldiriyor... -')
        time.sleep(0.1)
        sys.stdout.write('\rSaldiriyor... \\')
        time.sleep(0.1)
    sys.stdout.write('\r ')


def INSTAanimate():
    while done == 'false':
        sys.stdout.write('\rBot calisiyor... |')
        time.sleep(0.1)
        sys.stdout.write('\rBot calisiyor... /')
        time.sleep(0.1)
        sys.stdout.write('\rBot calisiyor... -')
        time.sleep(0.1)
        sys.stdout.write('\rBot calisiyor... \\')
        time.sleep(0.1)
    sys.stdout.write('\r ')


def Panimate():
    while done == 'false':
        sys.stdout.write('\rPolis Telsizi Araniyor... |')
        time.sleep(0.1)
        sys.stdout.write('\rPolis Telsizi Araniyor... /')
        time.sleep(0.1)
        sys.stdout.write('\rPolis Telsizi Araniyor... -')
        time.sleep(0.1)
        sys.stdout.write('\rPolis Telsizi Araniyor... \\')
        time.sleep(0.1)
    sys.stdout.write('\r ')


def TELanimate():
    while done == 'false':
        sys.stdout.write('\rTelefon Dinleniyor... |')
        time.sleep(0.1)
        sys.stdout.write('\rTelefon Dinleniyor... /')
        time.sleep(0.1)
        sys.stdout.write('\rTelefon Dinleniyor... -')
        time.sleep(0.1)
        sys.stdout.write('\rTelefon Dinleniyor... \\')
        time.sleep(0.1)
    sys.stdout.write('\r ')


def FACEanimate():
    while done == 'false':
        sys.stdout.write('\rBruteforce Calisiyor... |')
        time.sleep(0.1)
        sys.stdout.write('\rBruteforce Calisiyor... /')
        time.sleep(0.1)
        sys.stdout.write('\rBruteforce Calisiyor... -')
        time.sleep(0.1)
        sys.stdout.write('\rBruteforce Calisiyor... \\')
        time.sleep(0.1)
    sys.stdout.write('\r ')



    def admin():
        while done == 'false':
            sys.stdout.write('\rAdmin sayfasi yukleniyor... |')
            time.sleep(0.1)
            sys.stdout.write('\rAdmin sayfasi yukleniyor... /')
            time.sleep(0.1)
            sys.stdout.write('\rAdmin sayfasi yukleniyor... -')
            time.sleep(0.1)
            sys.stdout.write('\rAdmin sayfasi yukleniyor... \\')
            time.sleep(0.1)
        sys.stdout.write('\r ')


class wirelessTestingMenu:
    def __init__(self):
        print (mochuelologo)
        print("   {1}--Polis Dinle")
        print("   {2}--DDOS At")
        print("   {3}--Instagram Bot")
        print("   {4}--Telefon Dinle")
        print("   {5}--Facebook Sifre Bulucu")
        print("   {9}-Ana Menuye Git\n")
        choice4 = raw_input("mochuelo~# ")
        if choice4 == "1":
            polis()
        elif choice4 == "2":
            dos()
        elif choice4 == "3":
            Insta()
        elif choice4 == "4":
            tel()
        elif choice4 == "5":
            face()
        elif choice4 == "9":
            animate()
        elif choice4 == "99":
            admin()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        print("Tamamlandi, geri donmek icin tiklayiniz")
        self.__init__()

if __name__ == "__main__":
    try:
        mochuelo()
    except KeyboardInterrupt:
        print(
        """
Yukleniyor, lutfen bekleyiniz...
<Eger 3 dakika icinde acilmazsa silip bir daha yukleyin...>\r"""
            ),
        time.sleep(9999)
