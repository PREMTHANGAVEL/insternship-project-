import requests 
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

response = requests.get(URL)
if response.status_code != 200:
    print("Could not download a page. Status:",response.status_code)
    exit()
    
soup=BeautifulSoup(response.text,"html.parser")

headlines = []
for tag in soup.find_all("h1"):
    text = tag.get_text(strip=True)
    if text:
        headlines.append(text)


with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, h in enumerate(headlines, start=1):
        f.write(f"{i}. {h}\n")

print("Done — saved", len(headlines), "headlines to headlines.txt")