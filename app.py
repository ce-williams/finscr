import requests
from bs4 import BeautifulSoup
# ////////////////////////////////////
# ////This app requires python3///////
# ////////////////////////////////////

# P > 200 SMA, RSI(14)=40 (ovs)
r = requests.get('https://finviz.com/screener.ashx?v=111&f=ta_rsi_os40,ta_sma200_pa&ft=4')
soup = BeautifulSoup(r.text, 'lxml')

# ////////////////////////////////////
# ///////////ALL CURRENCIES///////////
# ////////////////////////////////////
data = []
table = soup.find('table', bgcolor="#d3d3d3")

for row in table.find_all('tr', limit=100):
    try:
        symbol = row.find('a', class_='screener-link-primary').text
        price = row.find("span").text
        # time_1h = row.find('td', {'data-timespan': '1h'}).text
    except AttributeError:
        continue
    data.append((symbol, price))

# for item in data:
#     print(data)


print(data)