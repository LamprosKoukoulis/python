from bs4 import BeautifulSoup
import requests
page_link =input('Input the url: ')
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
textContent = []
for i in range(len(page_link.read()):
    par = par + page_content.find_all("br")[i].text
    nl=nl +page_content.find_all("p")[i].text
print (par,"The <br> tags in thiw page\n")
print (nl,"The <p> tags in thiw page\n")           
    

