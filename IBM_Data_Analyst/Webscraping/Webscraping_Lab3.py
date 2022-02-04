#Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas

!mamba install bs4==4.10.0 -y
!pip install lxml==4.6.4
!mamba install html5lib==1.1 -y
!pip install requests==2.26.0

from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://en.wikipedia.org/wiki/World_population"
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

tables = soup.find_all('table')

# check to see how many tables in the tables list
len(tables)

# identify the 10 most densely populated countries table
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)
print(tables[table_index].prettify())

# Create DataFrame
population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

# Get data from html table into DataFrame
for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data
