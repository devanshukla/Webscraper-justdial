import requests
from bs4 import BeautifulSoup

#finding all products available in justdial lucknow section

def products_and_services(url,headers):
    try:
    	response = requests.get(url, headers=headers).content
    except requests.exceptions.RequestException as e:
        print(e)
        exit()
    data=BeautifulSoup(response,"html.parser")
    parent=data.find("body").find("ul",class_="wrapper link-list")
    text=list(parent.descendants)
    for i in range(2, len(text), 2):
    	print(text[i], end=" ")

#find specific element

def specific_element(url,headers):
    	try:
    		response = requests.get(url, headers=headers).content
    	except requests.exceptions.RequestException as e:
    		print(e)
    		exit()
    	data=BeautifulSoup(response,"html.parser")
    	element=data.find("body").find("div",class_="tbsbx1")
    	text=list(element.descendants)
    	print(text)
    	
#getting phone number

def get_phone_number(url,headers):
		try:
			response = requests.get(url, headers=headers).content
		except requests.exceptions.RequestException as e :
			print(e)
			exit()
		data=BeautifulSoup(response,"html.parser")
		element=data.find('p', {'class':'contact-info'}).span.a.string
		print(element)



url="https://www.justdial.com/Lucknow/all-hotkeys/show-more"

#for accessing the contents of justdial
headers = {
'authority': 'scrapeme.live',
'dnt': '1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

products_and_services(url,headers)
specific_element(url,headers)
get_phone_number(url,headers)