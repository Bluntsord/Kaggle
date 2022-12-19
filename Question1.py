import requests
from bs4 import BeautifulSoup

# Make the request to the website
URL = "https://www.lazada.com.ph/catalog/?q=logitech+g560"
page = requests.get(URL)

# Parse the HTML content
soup = BeautifulSoup(page.content, 'html.parser')

# Find the product divs
product_divs = soup.find_all('div', class_='c2prKC')

# Iterate over the product divs and extract the data
for div in product_divs:
    # Extract the title
    title = div.find('p', class_='c16H9d').text
    print(f"Title: {title}")

    # Extract the price
    price = div.find('span', class_='c13VH6').text
    print(f"Price: {price}")

    # Extract the rating
    rating = div.find('span', class_='c3XbGJ').text
    print(f"Rating: {rating}")

    # Print a separator
    print("-" * 20)