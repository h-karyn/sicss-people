import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://sicss.io/people"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    print(dir(soup))

    people_elements = soup.select('.body') 
    print(people_elements)

    for person in people_elements:
        name = person.get_text(strip=True)
        print(name)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
