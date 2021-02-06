import os, sys, time

def clear():
    os.system("clear")
def ulang():
    os.system("python ArieSR91.py")
clear()

print ('''
╭─────────────────────────╮    ╭───────╮    ╭─────────────────────────╮
│ ┬    ACCESS DENIED   ╭──┴────┤ LOGIN ├────┴──╮ ENTER THE PASSWORD ┬ │
│ ╰────────────────────╯    ╭──┴───┬───┴──╮    ╰────────────────────╯ │
╰───────────────────────────╯   ┬  │  ┬   ╰───────────────────────────╯
                                ╰──┴──╯
''')
username = input("                      [@] Username: ")
password = input("                      [*] Password: ")
if password == "******":
    print("")
else:
    print("\n                        Password Wrong")
    lagi = input("                        try again [Y/n]: ")
    if lagi == "y":
         ulang()
    else:
         sys.exit()
clear()


print ("╭─────────────────────────╮   ╭─────────╮   ╭─────────────────────────╮")
print ("│ ┬    LOGIN SUCCESS   ╭──┴───┤ SUCCESS ├───┴──╮     @"+username,"     ┬ │")
print ("│ ╰────────────────────╯   ╭──┴─────────┴──╮   ╰────────────────────╯ │")
print ("╰─────────────┬────────────╯  ╔═       ═╗  ╰─────────────┬────────────╯")

print ('''              ╰─────┬─────────╢ WELCOME ╟─────────┬──────╯
╭───────────────────┴────╮    ╚═       ═╝   ╭─────┴───────────────────╮
│     ┬  ACCESS GRANTED  ┴  ╭─────────────╮ ┴     INDONESIA     ┬     │
│     ╰─────────────────────┤ Hello World ├─────────────────────╯     │
╰─────────────╮         ╭───┴─────────────┴───╮         ╭─────────────╯
╭─────────────┴─────────╯  ArieSR91 tools V1  ╰─────────┴─────────────╮
│---------------------------------------------------------------------│
│         ╔═══╦═════════════╦═════════════╦═════════════╦═══╗         │
│   ╔════╦╝   ║       ╔═════╣ List script ╠═════╗       ║   ╚╦════╗   │
│     ╠═ ║ ═╣ ║                                         ║ ╠═ ║ ═╣     │
│     ╠══╩══╣ ║        [01] Install user91 tools        ║ ╠══╩══╣     │
│     ║       ║        [02] Spam_SCW-V1                 ║       ║     │
│     ╠════╣  ║        [03] Spam_SCW-V2                 ║  ╠════╣     │
│          │  ║        [04] Spam_SCW-V3                 ║  │          │
│          │  ║        [05] Spam_SCW-V4                 ║  │          │
│          │  ║        [06] Spam_WhatsApps              ║  │          │
│     ╠════╣  ║        [07] Trojans Attack              ║  ╠════╣     │
│     ║       ║        [08] DDoS Hammer Attack          ║       ║     │
│     ╠══╦══╣ ║        [09] Bug Hunter                  ║ ╠══╦══╣     │
│     ╠═ ║ ═╣ ║        [10] Deface Website              ║ ╠═ ║ ═╣     │
│   ╚════╩╗   ║        [00] Exit                        ║   ╔╩════╝   │
│         ╚═══╩═════════════════════════════════════════╩═══╝         │
│                                                                     │
│---------------------------------------------------------------------│
│                    ╭─────────────────────────                       │''')
pilih = input("╰────────────────────╯   Masukkan pilihan: ")
if pilih == "01":
   os.system("pkg update && pkg upgrade && pkg install python && pkg install python2 && pkg install wget && pkg install curl && pkg install git && pkg install ruby && pip install lolcat && pkg install php && pkg install neofetch && pkg install nano && pkg install perl && pkg install nodejs && pkg install micro && pkg install joe && pkg install vim && pkg install jupp && pkg install zile && pkg install figlet && pkg install toilet && pkg install fish && pkg install cowsay && gem install ruby && pip install bs4 && python -m pip install requests && pip install requests && pip install mechanize && pip2 install --upgrade pip && pip2 install mechanize && pip2 install requests && pip2 install lolcat")
if pilih == "02":
   os.system("python user91-spamV1.py")
if pilih == "03":
   os.system("python user91-spamV2.py")
if pilih == "04":
   os.system("python2 user91-spamV3.py")
if pilih == "05":
   os.system("python user91-spamV4.py")
if pilih == "06":
   os.system("python2 user91-spamWA.py")
if pilih == "07":
   os.system("python2 trojans.py")
if pilih == "08":
   os.system("python hammer.py")
if pilih == "09":
   os.system("php rhawk.php")
if pilih == "10":
   os.system("python deface.py")
if pilih == "00":
   sys.exit()
