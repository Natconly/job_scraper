#import needed libraries
import requests
from bs4 import BeautifulSoup

#reference the source page
source = "https://www.indeed.com"
page = requests.get(source)

#creating a variable that is the contents of the page, parsed
soup = BeautifulSoup(page.content, "html.parser")

#finding the id in HMTL of the results
results = soup.find(id="jobsearch-main")

#prompt to ask for search criteria
user_input = input("Enter a keyword for the job search: ").lower()

#the search portion itself
job_search = results.find_all(
    "h2", string=lambda text: user_input in text.lower()
)

job_search_elements = [
    h2_element.parent.parent for h2_element in job_search
]

if len(job_search_elements) == 0:
    print("No results, try another keyword")
else:
    for job_element in job_search_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        links = job_element.find_all("a")
        for link in links:
            link_url = link["href"]
            print(f"Apply here: {link_url}\n")
        print()