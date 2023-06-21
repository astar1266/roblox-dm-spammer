import requests
import threading
payload = {"conversationId":123,"message":"yo"}

header = {
'cookie':"",
'X-Csrf-Token':""
}

def do_request():
 while True:
    r = requests.post("https://chat.roblox.com/v2/send-message", json=payload, headers=header)
    print(r.text)
    
threads = []

for i in range(50):
  t = threading.Thread(target=do_request)
  t.daemon = True
  threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()