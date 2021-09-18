# print('hello, world')
from bs4 import BeautifulSoup
import requests
import json


def download_pdfs(form_name, year_range):
    base_url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html'
    # data = []
    i = 0
    t_row_data = []

    while True:
        payload = { 
            "value": form_name,
            "criteria": 'formNumber',
            'sortColumn': 'sortOrder',
            'indexOfFirstRow': i,
            'isDescending': 'false',
            'resultsPerPage': 25, 
        }


        r = requests.get(base_url, params=payload)
        c = r.content
        soup = BeautifulSoup(c, 'lxml')
        table = soup.find("table", class_= "picklist-dataTable")
        table_data = table.find_all('tr')

        headings = []
        for td in table_data[0].find_all("th"):
            headings.append(td.b.text.replace('\n', ' ').strip())


        for tr in table.find_all("tr"):
            t_row = {}
            for td, th in zip(tr.find_all("td"), headings): 
                # print(tr.td.a)
                t_row[th] = td.text.replace('\n', '').strip()
                t_row['link'] = tr.td.a['href']
            t_row_data.append(t_row)
        if t_row == {}:
          break
        i += 25

    for row in t_row_data:
        if row != {} and row['Product Number'].lower() == form_name.lower():
          for row['Revision Date'] in year_range:
              response = requests.get(row['link'])
              with open(form_name+'-'+str(row['Revision Date'])+'.pdf', 'wb') as file:
                  file.write(response.content)

form_name = input("Enter the form you want to search for >>> ").strip()
years= input("Enter the year range >>> ").split("-")
no_of_years = int(years[1].strip())-int(years[0].strip())

year_range = [int(years[0]) + i for i in range(no_of_years+1)]

download_pdfs(form_name, year_range)