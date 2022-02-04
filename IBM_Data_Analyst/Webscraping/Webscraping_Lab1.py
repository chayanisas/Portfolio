!mamba install bs4==4.10.0 -y
!pip install lxml==4.6.4
!mamba install html5lib==1.1 -y
!pip install requests==2.26.0

from bs4 import BeautifulSoup
import requests

# Download the contents of the webpage in text format
url = "http://www.ibm.com"
data  = requests.get(url).text

# Create a BeautifulSoup object using the variable 'data'
soup = BeautifulSoup(data,"html.parser")

# Scrape all links on the webpage
for link in soup.find_all('a',href=True):
    print(link.get('href'))

# Scrape all image tags on the webpage
for link in soup.find_all('img'):
    print(link)
    print(link.get('src'))
