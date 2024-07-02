import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://sicss.io/people"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    print(dir(soup))
    # Find all elements that contain the names of people (adjust the selector as needed)
    people_elements = soup.select('.body')  # Example selector, adjust based on actual HTML structure
    print(people_elements)
    # Extract and print the names
    for person in people_elements:
        name = person.get_text(strip=True)
        print(name)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
