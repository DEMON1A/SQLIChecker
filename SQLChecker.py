import urllib.request
import urllib.error

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


print(" ")
print("[*]Started Checking The Url!")
print(" ")

try:
    res = urllib.request.urlopen(Target + PayLoad).read().decode('utf8')
    print(" ")
    print("++++++++++++")
    if 'sql syntax' in res.lower():
        print("[+]Infected")
    else:
        print("[!]Not Infected")
    print("[*]Done")
    print("++++++++++++")
except urllib.error.URLError :
    print("[!]The Url Is Wrong")
except urllib.error.HTTPError :
    print("[!]The Page Is Not Responding")

print("[+]For More Tools Visit My Github Account")


