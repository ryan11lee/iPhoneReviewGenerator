#%%
import requests
import os
import glob
from bs4 import BeautifulSoup


def get_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    body = soup.find("div",{"class":"c-entry-content"})

    justText = []
    p = body.find_all("p")
    for tag in p:
        #print(tag.get_text())
        justText.append(tag.get_text().replace("\t", "").replace("\r", "").replace("\n", ""))

    with open("%s" %url.split("/").pop() + ".txt", "w+", encoding='utf-8') as file:
        for item in justText:
            file.write(item)


url = "https://www.theverge.com/22684421/apple-iphone-13-mini-review"
url2 = "https://www.theverge.com/21522988/iphone-12-review"
url3 = "https://www.theverge.com/2019/9/17/20869456/apple-iphone-11-review-camera-price-budget-battery-screen-size-features"
url4 = "https://www.theverge.com/2018/9/18/17871816/apple-iphone-xs-max-review-camera-processor-battery-price"
url5 = "https://www.theverge.com/2017/10/31/16579748/apple-iphone-x-review"
url6 = "https://www.theverge.com/2017/9/19/16323570/apple-new-iphone-8-review-plus-2017"


reviewList = [url, url2, url3, url4, url5, url6]

try:
    os.mkdir("text")
except FileExistsError:
    pass
    
os.chdir("text")

for url in reviewList:
    get_text(url)

    
filenames = glob.glob('*.txt')

print(filenames)

with open("../output_file.txt", "w") as outfile:
    for f in filenames:
        print(f)
        with open(f) as infile:
            contents = infile.read()
            outfile.write(contents)
