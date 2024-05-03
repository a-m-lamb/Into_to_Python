from selenium import webdriver 
import time

from gmail import gmail_authenticate, send_message 


def build_dictionary(url):
    title = driver.title
    description = driver.find_element("xpath", "//meta[@name='description']").get_attribute("content")

    content = {
        "title": title, 
        "description": description,
        "url": url
    }

    return content


driver = webdriver.Chrome()
driver.get('https://news.google.com/search?q=programming')

time.sleep(2)
driver.maximize_window()

list = []
content = []

for x in range (1, 4):

    element = driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/main/div[2]/c-wiz/c-wiz['+str(x)+']/c-wiz/article/div[1]/div[1]/a' )
    url = element.get_attribute("href")
    list.append(url)


for url in list:
    driver.get(url)
    time.sleep(2)

    c = build_dictionary(url)
    content.append(c)



print(content)

count = 1
msg = "Hey Adriana!\n\nYou should check out these articles today.\n\n"


for c in content: 
    msg += str(count)+") " + c.get("title") + ":" + c.get("description") + "\n\n" + c.get("url") + "\n\n"
    count+=1

service = gmail_authenticate()

send_message(service, "adriana.michelle.long@gmail.com", "DAILY TECH ARTICLE", msg)

