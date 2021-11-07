from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=DSLR%20%20Camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

response = requests.get(url)
htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')

title =[]
prices =[]
images =[]

for d in soup.find_all('div',attrs={'class':''}):
   title = d.find('div',attrs={'class':'_4rR01T'})
   #print(title.string)

   price = d.find('div',attrs={'class':'_30jeq3_1_WHN1'})
   #print(title.string)

   image = d.find('img',attrs={'class':'_30jeq3_1_WHN1'})
   #print(image.get('src'))

title.append(title.string)
prices.append(price.string)
images.append(image.get('src'))

print(title)
print(prices)
print(images)