from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup
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
reviews = []
availables = []
firstnames = []
secondnames = []
experiences = []

# Navigate to the base URL
base_url = "https://oladoc.com/pakistan/karachi/general-physician"
total_pages = 5  # Change this based on the number of pages you want to scrape

# Loop through the specified number of pages
for page in range(1, total_pages + 1):
    # Navigate to the URL
    driver.get(f"{base_url}/{page}")
    
    # Wait for the page to load
   

    # Extract page source and parse it using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Loop through each product entry and extract details
    for b in soup.findAll('div', attrs={'class': 'card-body p-lg-4 doctor-listing-card"'}):
            # Initialize default values
            profession_text = "NA"
            review_text = "NA"
            experience_text = "NA"
            price_text = "NA"
            available_text = "NA"
            firstname = "NA"
            secondname = "NA"

            try:
                profession = b.find('p', attrs={'class': 'mb-1 od-text-dark-muted text-truncate-dots text-truncate-dots-2'})
                experience = b.find('span', attrs={'class': 'od-wte'})
                price = b.find('span', attrs={'class': 'doctor-fee'})
                name = b.find('a', attrs={'class': 'doctor-name nearme mb-1 mt-1'})
                reviews = b.find('span', attrs={'class': 'd-inline-block font-weight-normal'})
                available = b.find('span', attrs={'class': 'text-truncate d-block mb-1 font-weight-medium'})

                if profession:
                    oldprofession = profession_elem.text.strip()
                    profession=get_first_profession(oldprofession)
                if degree:
                    olddegree = degree_elem.text.strip()
                    degree=get_first_profession(olddegree)
                if experience:
                    experience = experience_elem.text.strip()
                if price:
                    price = price_elem.text.strip()
                if consul_elem:
                    consul = consul_elem.text.strip()
                if name:
                    title = name_elem.text.strip()
                    parts = title.split()
                    firstname = parts[-2]# Join all but the last word 
                    secondname = parts[-1]
                if review:
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
            experiences.append(newe if newe else "NA")


            
         

            # Append data to lists
           

    print(f"Processed page {page}")

# Create a DataFrame with the extracted data
df = pd.DataFrame({
    'FirstName': firstnames,
    'SecondName': secondnames,
    'Price': prices,
    'Experience': experiences,
    'Profession': professions,
    'Reviews': reviews,
    'Consul': availables
})

# Save the data to a CSV file
df.to_csv('oladocdata.csv', index=False, encoding='utf-8')

# Close the driver
driver.quit()
