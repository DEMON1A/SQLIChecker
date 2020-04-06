'''
LOL Really I Hate Myself It Was A Shit Code
I Will Clean It And Add List Check Later LOL
Have Fun Bruh!
'''
import re
import requests
import urllib.request
import urllib.error
from bs4 import BeautifulSoup

def Banner():
  ban = "\t\t\t\t\t\t\t<< SQLI Checker >>\n"
  print(ban)

def Start():
    # Ask For Target Site
    Target = input("Enter Url: ")
    Payload = "'" # Just A Singel Code To Check IF There is A SQL ERROR

    Session = requests.Session()
    Request = Session.get(Target + Payload)
    Soup = BeautifulSoup(Request.content,'html.parser')

    # Npw USE RE To Check The Content
    if len(Soup.find_all(text = re.compile('SQL syntax'))) > 0:
        try:
            print("{0} >> Infected".format(Target)
        except urllib.error.URLError :
            print("Sorry Wrong URL!")
        except urllib.error.HTTPError :
            print("Page Not Responding!!!")

    if len(Soup.find_all(text = re.compile('SQL syntax'))) == 0:
        try:
            print("{0} >> Not Infected".format(Target)
        except urllib.error.URLError :
            print("Sorry Wrong URL!")
        except urllib.error.HTTPError :
            print("Page Not Responding!!!")

    if len(Soup.find_all(text = re.compile('SQL syntax'))) < 0:
        try:
            print("{0} >> Not Infected".format(Target)
        except urllib.error.URLError :
            print("Sorry Wrong URL!")
        except urllib.error.HTTPError :
            print("Page Not Responding!!!")
                  
Banner()
Start()
