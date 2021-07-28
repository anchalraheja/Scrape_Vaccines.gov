from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time
url_1 = "https://www.vaccines.gov/search/?zipcode="
url_3 = "&medications=779bfe52-0dd8-4023-a183-457eb100fccc,a84fb9ed-deb4-461c-b785-e17c782ef88b,784db609-dc1f-45a5-bad6-8db02e79d44f&radius=50&availableAppointmentsOnly=false"
pincode = ""

browser = webdriver.Chrome()

def counter(pincode):
	# open link
	url = url_1 + pincode + url_3
	browser.get(url)

	# click search
	time.sleep(5)
	browser.find_element_by_xpath('//button[contains(text(), "Search for Vaccines")]').click()

	# search pincode count
	time.sleep(5)
	count = []

	soup=BeautifulSoup(browser.page_source)
	for link in soup.find_all('a'):
	    if pincode in link.get_text():
	    	count.append(link.get_text())
	    else:
	    	pass
	print (len(count))

	# print data to csv 
	with open("result.csv","a") as file:
		file.write(str(pincode)+ "," +str(len(count)) + "\n")
		file.close()


with open("pincodes.txt","r") as f:
	for x in f:
		pincode = x.rstrip()
		try:
			counter(pincode)
		except Exception as e:
			raise e