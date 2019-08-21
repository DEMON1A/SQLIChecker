import re
import requests
import urllib.request
import urllib.error
from bs4 import BeautifulSoup

print("""
                                     _______________________________________________
                                    |          =============================        |
                                    |         +  SQLChecker By Mohamed Dief  +      |
                                    |          =============================        |
                                    |                                               |
                                    |[+]Github: github.com/DEMON1A                  |
                                    |[+]Facebook: facebook.com/mohamed.dief.1029    |
                                    |[+]Twitter: twitter.com/Demon77098812          |
                                    |[+]Email: mdaif1332@gmail.com                  |
                                    =================================================

""")


Target = input("[*]Enter Target Url: ")
PayLoad = "'"

res = requests.get(Target + PayLoad)

print(" ")
print("[*]Start Check The Url!")
print(" ")

Soup = BeautifulSoup(res.content,'html.parser')


if len(Soup.find_all(text = re.compile('SQL syntax'))) > 0:
    try:
        print(" ")
        print("++++++++++++")
        print("[+]Infected")
        print("[*]Done")
        print("++++++++++++")
    except urllib.error.URLError :
        print("[!]The Url Is Wrong")
    except urllib.error.HTTPError :
        print("[!]The Page Is Not Responding")

if len(Soup.find_all(text = re.compile('SQL syntax'))) == 0:
    try:
        print(" ")
        print("++++++++++++++++")
        print("[!]Not Infected")
        print("[*]Done")
        print("++++++++++++++++")
    except urllib.error.URLError :
        print("[!]The Url Is Wrong")
    except urllib.error.HTTPError :
        print("[!]The Page Is Not Responding")

if len(Soup.find_all(text = re.compile('SQL syntax'))) < 0:
    try:
        print(" ")
        print("++++++++++++++++")
        print("[!]Not Infected")
        print("[*]Done")
        print("++++++++++++++++")
    except urllib.error.URLError :
        print("[!]The Url Is Wrong")
    except urllib.error.HTTPError :
        print("[!]The Page Is Not Responding")

print("[+]For More Tools Visit My Github Account")


