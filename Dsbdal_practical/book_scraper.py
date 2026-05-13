import requests
from bs4 import BeautifulSoup

# The Books to Scrape URL
url = "https://books.toscrape.com/"

print(f"Fetching data from {url}...\n")
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all book articles on the page
books = soup.find_all("article", class_="product_pod")

print("-" * 50)

for i, book in enumerate(books[:10], 1):  # Just taking the first 10 for display
    # Extract the title (from the 'title' attribute of the <a> tag inside <h3>)
    title = book.find("h3").find("a")["title"]
    
    # Extract the price
    price = book.find("p", class_="price_color").text
    
    # Extract the rating (it's stored as a class name like "star-rating Three")
    rating_element = book.find("p", class_="star-rating")
    rating = rating_element["class"][1] if rating_element else "None"
    
    # Extract stock status
    stock = book.find("p", class_="instock availability").text.strip()
    
    print(f"Book #{i}")
    print(f"Title : {title}")
    print(f"Price : {price}")
    print(f"Rating: {rating} out of Five")
    print(f"Stock : {stock}")
    print("-" * 50)
