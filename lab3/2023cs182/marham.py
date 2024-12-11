from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup
import re
def get_first_profession(profession):
    # Return the part before the first comma, or the whole string if no comma exists
    return profession.split(',')[0].strip()

def extract_numbers(s):
    numbers = re.findall(r'\d+', s)
    return int(''.join(numbers)) if numbers else None

def get_characters_only(input_string):
    # Use list comprehension to filter only alphabetic characters
    characters_only = ''.join([char for char in input_string if char.isalpha() or char.isspace()])
    return characters_only
# Fix the path to Chrome WebDriver
service = Service(executable_path=r'C:\\Users\\ADMIN\\Desktop\\dsalab\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Initialize lists to store product details
prices = []
professions = []
degrees = []
consults = []
reviews = []
firstnames = []
secondnames = []
experiences = []

# Navigate to the base URL

urls_df = pd.read_csv('URLS.csv')

# Loop through each URL and the number of pages to scrape
for index, row in urls_df.iterrows():
    base_url = row['url']
    total_pages = row['total_pages']
# Loop through the specified number of pages
    for page in range(1, total_pages + 1):
    # Navigate to the URL
      driver.get(f"{base_url}?page={page}")
    
 

    # Extract page source and parse it using BeautifulSoup
      soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Loop through each product entry and extract details
      for a in soup.findAll('div', attrs={'class': 'container bg-white mt-10 pb-10'}):
        for b in a.findAll('div', attrs={'class': 'row shadow-card'}):
            # Initialize temporary variables
            price = "NA"
            profession = "NA"
            degree = "NA"
            consul = "NA"
            review = "NA"
            firstname = "NA"
            secondname = "NA"
            experience = "NA"

            try:
                # Extract information
                profession_elem = b.find('p', attrs={'class': 'mb-0 text-sm'})
                degree_elem = b.find('p', attrs={'class': 'text-sm'})
                experience_elem = b.find('p', attrs={'class': 'text-bold text-sm'})
                price_elem = b.find('p', attrs={'class': 'mb-0 price text-sm text-bold'})
                consul_elem = b.find('p', attrs={'class': 'mb-0 text-bold text-blue text-sm'})
                name_elem = b.find('a', attrs={'class': 'text-blue'})
                review_elem = b.find('p', attrs={'class': 'text-bold text-sm text-golden'})
                
                # Assign values if elements are found
                if profession_elem:
                    oldprofession = profession_elem.text.strip()
                    profession=get_first_profession(oldprofession)
                if degree_elem:
                    olddegree = degree_elem.text.strip()
                    degree=get_first_profession(olddegree)
                if experience_elem:
                    experience = experience_elem.text.strip()
                if price_elem:
                    price = price_elem.text.strip()
                if consul_elem:
                    consul = consul_elem.text.strip()
                if name_elem:
                    title = name_elem.text.strip()
                    parts = title.split()
                    firstname = parts[-2]# Join all but the last word 
                    secondname = parts[-1]
                if review_elem:
                    review = review_elem.text.strip()

            except Exception as e:
                print(f"Error processing entry: {e}")

            # Append all values to their respective lists
            nrep=extract_numbers(price)
            prices.append(nrep if nrep else 0)
            newp=get_characters_only(profession)
            professions.append(newp if newp else "NA")
            newd=get_characters_only(degree)
            degrees.append(newd if newd else "NA")
            newc=get_characters_only(consul) 
            consults.append(newc if newc else "NA")
            newr=extract_numbers(review)
            reviews.append(newr if newr else 0)
            fname=get_characters_only(firstname) 
            firstnames.append(fname) 
            sname=get_characters_only(secondname)
            secondnames.append(sname)
            newe=extract_numbers(experience)
            experiences.append(newe if newe else 0)

      print(f"Processed page {page}")

# Create a DataFrame with the extracted data
df = pd.DataFrame({
    'FirstName': firstnames,
    'SecondName': secondnames,
    'Price': prices,
    'Profession': professions,
    'Experience': experiences,
    'Consult': consults,
    'Review': reviews
})

# Save the data to a CSV file
df.to_csv('data.csv', index=False, encoding='utf-8')

# Close the driver
driver.quit()
