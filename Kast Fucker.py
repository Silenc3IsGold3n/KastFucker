import requests
import json
import time

url = "http://api-auth.evasyst.com/api/register"
gmail = "yourgmailbeforetheAt"#so like "test123" from test123@gmail.com
password = "yourgmailpassword" #the password you want to use for the Kast.gg Account
try:
    fp = open('usernames.txt')#Open the usernames.txt file and read through it trying to register an account with each name on the list
    # do stuff here
    for i in range(34857):
        text = fp.readline()
    while text:
        while True:
            try:
                text = text.strip()
                payload = "{ \"login\":\""+text+"\",\"email\":\""+gmail+"+"+text+"@gmail.com\",\"password\":\""+password+"\",\"langKey\":\"EN\"}"
                print(payload)
                headers = {
                  'origin': 'https://w.kast.gg',
                  'referer': 'https://w.kast.gg',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'accept': 'application/json',
                  'accept-language': 'en-US,en;q=0.9',
                  'authority': 'api-auth.evasyst.com',
                  'Content-Type': 'application/json'
                }

                response = requests.request("POST", url, headers=headers, data = payload)
                print(response.text.encode('utf8'))
                r = response.json()
                if "message" in r:
                    print(r["message"])
                    if "orbidde" in r["message"]:
                        time.sleep(300)
                if "error" in r:
                    print(" Error found oop")
                    text = fp.readline()
                else:
                    text = fp.readline()
                    break
            except:
                continue
            
finally:
    fp.close()
