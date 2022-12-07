import requests
import xml.etree.ElementTree as et
import time

def postWebhook(message: str, embed: str, name: str):
    file = open("webhook.txt", "r")
    url = file.readline()
    data = {
        "content": message,
        "embeds": [
            {"title": "Article","url": embed}
        ],
        "username": name
    }
    req = requests.post(url=url, json=data)
    print(req.status_code, req.content)

def main(old):
    url = "https://www.minecraft.net/en-us/feeds/community-content/rss.xml"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    req = requests.get(url=url, headers=headers)
    print(req.status_code)
    if req.status_code == 200:
        root = et.fromstring(req.content)
        i = list(root.iter('item'))
        for x in i:
            print(x[0].text, old)
            
            if (str.find(x[0].text, "Pre-Release") != -1):
                if old != x[0].text:
                    postWebhook(f"New Pre-Release: {x[0].text}", str(x[1].text), "New Pre-Release Available!")
                    return str(x[0].text)
                else:
                    return str(x[0].text)
            elif (str.find(x[0].text, "Release Candidate") != -1):
                if old != x[0].text:
                    postWebhook(f"New Release Candidate: {x[0].text}", str(x[1].text), "New Release Candidate Available!")
                    return str(x[0].text)
                else:
                    return str(x[0].text)
            elif (str.find(x[0].text, "Release") != -1):
                if old != x[0].text:
                    postWebhook(f"New Release: {x[0].text}", str(x[1].text), "New Release Available!")
                    return str(x[0].text)
                else:
                    return str(x[0].text)
            elif str.find(x[0].text, "Snapshot") != -1:
                if old != x[0].text:
                    postWebhook(f"New Snapshot: {x[0].text}", str(x[1].text), "New Snapshot Available!")
                    return str(x[0].text)
                else:
                    return str(x[0].text)

old1 = ""
while True:
    bruh = main(old1)
    old1 = bruh
    time.sleep(10)