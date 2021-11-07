from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=DSLR%20%20Camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

response = requests.get(url)
#print(response.status_code)
#print(response.content)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')
#print(soup.prettify())

#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.title.parent.name)
#print(soup.p)
#print(soup.a)
#print(soup.find_all('a'))
#print(soup.find(id="next-apge-link-tag"))
#print(soup.find_all('a'))

#for link in soup.find_all('a'):
    #print(link.get('href'))

#for image in soup.find_all('img'):
    #print(link.get('src'))

#product = soup.find_all('div', class_='_13oc-S')
#print(product.string)

#product = soup.find_all('div', attrs={'class':'_13oc-S'})
#print(product)
