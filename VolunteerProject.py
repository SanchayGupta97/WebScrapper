import requests
from bs4 import BeautifulSoup

pages_to_read = 2
start_page = 0 #pagination has home page as 0
current_page = start_page
count = 0  # added fo sanity check

while current_page < pages_to_read+start_page:
    project_page_url = requests.get("https://europa.eu/youth/volunteering/project_en?page=" + str(current_page))
    project_page = BeautifulSoup(project_page_url.content, 'lxml')
    posts = project_page.find_all('div', class_="content")
    for post in posts:
        count += 1
        print("Name:" + post.h4.text)
        print("Organisation: " + post.find(class_='eyp-organisation-icon').a.text)
        print("Location: " + post.find(class_='eyp-location-icon').text)
        print("Dates: " + post.find(class_='eyp-calendar-icon').text.strip())
        print("Posted: " + post.find(class_='esc-standard-date').text + "\n")
    current_page += 1
print(count)  # should be 9 times the number of pages to read
