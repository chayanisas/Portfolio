!mamba install bs4==4.10.0 -y
!pip install lxml==4.6.4
!mamba install html5lib==1.1 -y
!pip install requests==2.26.0

from bs4 import BeautifulSoup
import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

# Scrape data from HTML tables
table = soup.find('table')

# Get all rows from the table and get all columns in each row
for row in table.find_all('tr'):
    cols = row.find_all('td')
    color_name = cols[2].string
    color_code = cols[3].string
    print(f"{color_name}--->{color_code}")
