# Author: Edison Suen

import requests as r
from bs4 import BeautifulSoup
from prettytable import PrettyTable

base_url = ("http://www.coursediggers.com/data/{}.json".format(i) for i in range(1,10376))

def get_data(base_url):
    for i in base_url:
        page = r.get(i)
        if (page.status_code == r.codes.ok):
            data = page.json()
            if(data['metadata']['dataSource']['id'] == 3 or data['metadata']['dataSource']['id'] == 4):
                course_name = data['name']
                try:
                    median_grade = data['data'][0][0]
                    fail_percent = data['data'][0][1]
                except:
                    median_grade = "N/A"
                    fail_percent = "N/A"

                table.add_row([course_name,median_grade,fail_percent])

    return table


table = PrettyTable(["Name","Median","Fail Percentage"])
get_data(base_url)
table_txt = table.get_string(sortby="Name")
with open('data.txt','w') as file:
    file.write(table_txt)