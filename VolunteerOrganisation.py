import requests
from bs4 import BeautifulSoup

pages_to_read = 2
start_page = 0  # pagination has home page as 0
current_page = start_page
count = 0  # added fo sanity check
page_url = "https://europa.eu/youth/volunteering/organisation_en"
while current_page < pages_to_read + start_page:
    organisation_page = requests.get(page_url)
    page_contents = BeautifulSoup(organisation_page.content, 'lxml')
    posts = page_contents.find_all('div', class_="content")
    for post in posts:
        count += 1
        print("Name:" + post.h5.text)
        p_tags = post.find_all('p')
        if p_tags[0].text == "Topics":
            print("Topic: " + p_tags[1].text)
        print("Location: " + p_tags[-4].text)
        if post.find(class_="eyp-external-link") is not None:
            print("site: " + p_tags[-3].text)
        print("PIC: " + p_tags[-2].text)
        print("OID: " + p_tags[-1].text)
    current_page += 1
    page_url = "https://europa.eu" + page_contents.find(class_="next").a.get("href")
print(count)  # should be 20 times the number of pages to read
