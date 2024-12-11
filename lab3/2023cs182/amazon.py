from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from bs4 import BeautifulSoup
# Fix the path to Chrome WebDriver
service = Service(executable_path=r'C:\\Users\\ADMIN\\Desktop\\dsalab\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Initialize lists to store product details
prices = []
professions = []
degrees = []
availables = []
consults = []
reviews=[]
firstnames=[]
secondnames=[]
experiences=[]
# Navigate to the base URL
base_url = "https://www.marham.pk/doctors/lahore/gender-male"
total_pages = 5 # Change this based on the number of pages you want to scrape

# Loop through the specified number of pages
for page in range(1, total_pages + 1):
    # Navigate to the URL
    driver.get(f"{base_url}?page={page}")
    
    # Wait for the page to load
    time.sleep(3)  # Adjust as necessary for your connection speed

    # Extract page source and parse it using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Loop through each product entry and extract details
    for a in soup.findAll('div', attrs={'class': 'container bg-white mt-10 pb-10'}):
        for b in a.findAll('div',attrs={'class':'row shadow-card'}):
         profession = b.find('p', attrs={'class': 'mb-0 text-sm'})
         degree = b.find('p', attrs={'class': 'text-sm'})
         experience = b.find('p', attrs={'class': 'text-bold text-sm'})
         price = b.find('p', attrs={'class': 'mb-0 price text-sm text-bold'})
         consul=b.find('p',attrs={'class':'mb-0 text-bold text-blue text-sm'})
         name=b.find('a',attrs={'class':'text-blue'})
         review=b.find('p',attrs={'class':'text-bold text-sm text-golden'})
         title=name.text
         parts = title.split()
         firstname = ' '.join(parts[:-1])  # Join all but the last word
         secondname = parts[-1]     
         print(f"Found {len(a)} products on page {page}.")
        # Check if the elements exist before accessing text
         if price:
          reviews.append(review.text)  if review else "NA"
          prices.append(price.text) if price else 0
          professions.append(profession.text) if profession else "NA"
          degrees.append(degree.text) if degree else "NA"
          firstnames.append(firstname) 
          secondnames.append(secondname)
          consults.append(consul.text) if consul else "NA"
          experiences.append(experience.text) if experience else 0
# Create a DataFrame with the extracted data
df = pd.DataFrame({'FirstName': firstnames, 'SecondName':secondnames,'Price': prices, 'Profession':professions,'experience': experiences,'Consuls':consults,'Review':reviews})

# Save the data to a CSV file
df.to_csv('data3.csv', index=False, encoding='utf-8')

# Close the driver
driver.quit()
