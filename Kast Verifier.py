import requests
import json
import time

url = "https://api-auth.evasyst.com/api/activateandlogin"
password = "yourpassword"
try:
    fp = open('verificationcodes.txt')

    #for i in range(13605):
    text = fp.readline()
    while text:
        while True:
            try:
                code = text.split(':')[1].strip()
                payload = "{\"key\":\""+code+"\",\"password\":\""+password+"\"}"
                print(payload)
                headers = {
                  'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
                  'Accept': 'application/json',
                  'sec-ch-ua-mobile': '?0',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
                  'Content-Type': 'application/json',
                  'Sec-Fetch-Site': 'cross-site',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Dest': 'empty',
                  'dnt': '1',
                  'sec-gpc': '1'
                }

                response = requests.request("POST", url, headers=headers, data = payload)
                r = response.json()
                print(response.text.encode('utf8'))
                if "message" in r:
                    print(r["message"])
                    if "orbidde" in r["message"]:
                        time.sleep(300)
                    if "User not found" in r["message"]:
                        text = fp.readline()
                        continue
                if "error" in r:
                    print(" Error found oop")
                    text = fp.readline()
                else:
                    fo = open('verified.txt', 'a')
                    fo.write(text.split(':')[0].strip()+ "\n")
                    fo.close()
                    text = fp.readline()
                    break
            except:
                continue
finally:
    fp.close()
