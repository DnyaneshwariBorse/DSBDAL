import requests
from bs4 import BeautifulSoup

# The WebScraper test site URL
url = "https://webscraper.io/test-sites/e-commerce/static"

print(f"Fetching data from {url}...\n")
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the product cards on the page
# On this site, products are wrapped in a div with class "thumbnail"
products = soup.find_all("div", class_="thumbnail")

print("-" * 50)

for i, product in enumerate(products, 1):
    # Extract the product name
    name = product.find("a", class_="title").text.strip()
    
    # Extract the price
    price = product.find("h4", class_="price").text.strip()
    
    # Extract the description
    description = product.find("p", class_="description").text.strip()
    
    # Extract the review count
    reviews = product.find("p", class_="review-count").text.strip()
    
    print(f"Product #{i}")
    print(f"Name   : {name}")
    print(f"Price  : {price}")
    print(f"Desc   : {description}")
    print(f"Reviews: {reviews}")
    print("-" * 50)
