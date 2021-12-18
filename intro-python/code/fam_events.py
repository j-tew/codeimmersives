from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
url = "https://www.discoverdenton.com/events/?view=list&sort=date"
page = browser.get(url)

events = browser.find_elements_by_partial_link_text("Golden")

print(events)
sleep(10)
browser.close()