import requests
from bs4 import BeautifulSoup
import csv

SERVER_URL = "http://172.20.241.29/mittausdata.php"
CSV_FILE =  "sensor_data.csv"

response = requests.get(SERVER_URL)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

header = [th.text.strip() for th in rows[0].find_all('th')]

data = []
for row in rows[1:]:
    cols = [td.text.strip() for td in row.find_all('td')]
    data.append(cols)

with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter = ';')
    writer.writerow(header)
    writer.writerows(data)

print(f"CSV file '{CSV_FILE}' saved successfully!")


