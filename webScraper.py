#%%
import requests
import os
from bs4 import BeautifulSoup


def get_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    body = soup.find("div",{"class":"c-entry-content"})

    justText = []
    p = body.find_all("p")
    for tag in p:
        print(tag.get_text())
        justText.append(tag.get_text().replace("\t", "").replace("\r", "").replace("\n", ""))

    with open("%s" %url.split("/")[4] + ".txt", "w+" ) as file:
        for item in justText:
            file.write(item)


url = "https://www.theverge.com/22684421/apple-iphone-13-mini-review"
url2 = "https://www.theverge.com/21522988/iphone-12-review"


try:
    os.mkdir("text")
except FileExistsError:
    pass
    
os.chdir("text")

for u in [url,url2]:
    get_text(u)