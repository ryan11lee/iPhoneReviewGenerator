#%%
import requests
import os
from bs4 import BeautifulSoup


#%% 
url = "https://www.theverge.com/22684421/apple-iphone-13-mini-review"

page = requests.get(url)


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())
#%%
body = soup.find("div",{"class":"c-entry-content"})

justText = []
p = body.find_all("p")
for tag in p:
    print(tag.get_text())
    justText.append(tag.get_text())
#%%

print(os.getcwd())
os.mkdir("text")
os.chdir("text")

#%%
with open("%s" %url.split("/")[4] + ".txt", "w+" ) as file:
    for item in justText:
        file.write(item)
# %%
