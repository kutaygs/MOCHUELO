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
.___  ___.   ______     ______  __    __   __    __   _______  __        ______
|   \/   |  /  __  \   /      ||  |  |  | |  |  |  | |   ____||  |      /  __  |
|  \  /  | |  |  |  | |  ,----'|  |__|  | |  |  |  | |  |__   |  |     |  |  |  |
|  |\/|  | |  |  |  | |  |     |   __   | |  |  |  | |   __|  |  |     |  |  |  |
|  |  |  | |  `--'  | |  `----.|  |  |  | |  `--'  | |  |____ |  `----.|  `--'  |
|__|  |__|  \______/   \______||__|  |__|  \______/  |_______||_______| \______/


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
            animate()
        elif choice4 == "2":
            animate()
        elif choice4 == "3":
            animate()
        elif choice4 == "4":
            animate()
        elif choice4 == "5":
            animate()
        elif choice4 == "9":
            animate()
        elif choice4 == "99":
            animate()
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
