!pip install pandas==1.3.3
!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y
!pip install lxml==4.6.4
!pip install plotly==5.3.1

import pandas as pd
import requests
from bs4 import BeautifulSoup

#Using Webscraping to Extract Stock Data Example
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data  = requests.get(url).text
soup = BeautifulSoup(data, 'html5lib')

# Turn html table into Pandas DataFrame
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
for row in soup.find("tbody").find_all('tr'):  #isolate the body of the table and loop through each row and find all the column values for each row
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)

# Another way of turning html table into DataFrame using read_html
read_html_pandas_data = pd.read_html(url) # or read_html_pandas_data = pd.read_html(str(soup))
netflix_dataframe = read_html_pandas_data[0] #take the first table since there is only one table on the webpage
netflix_dataframe.head()
