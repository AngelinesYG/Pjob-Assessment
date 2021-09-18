from bs4 import BeautifulSoup
import requests
import json


def scraper(form_name):
    base_url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html'
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
                t_row[th] = td.text.replace('\n', '').strip()
                t_row['link'] = tr.td.a['href']
            t_row_data.append(t_row)
        if t_row == {}:
            break
        i += 25

    years = []
    result = {}

    for row in t_row_data[1:]:
      if row != {} and row['Product Number'].lower() == form_name.lower():
        years.append(row['Revision Date'])

    for row in t_row_data[1:]:
      if row != {} and row['Product Number'].lower() == form_name.lower():
        years.append(row['Revision Date'])
        result['form_number'] = row['Product Number']
        result['form_title'] = row['Title']
        break

    result['min_year'] = min(years)
    result['max_year'] = max(years)

    return result

form_names = input("Enter the form you want to search for >>> ").split(",")
final_data = []
for form_name in form_names:
    final_data.append(scraper(form_name.strip()))

print(json.dumps(final_data, indent=4))