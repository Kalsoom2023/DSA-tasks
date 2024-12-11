from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Fix the path to Chrome WebDriver
service = Service(executable_path=r'C:\\Users\\ADMIN\\Desktop\\dsalab\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Initialize lists to store product details
CourseCode = []
Title = []
Description = []
CLO1 = []
CLO2 = []
CLO3 = []
CLO4 = []
TextBook1 = []
TextBook2 = []
Instructor = []
Semester = []


# Navigate to the base URL
driver.get("https://eduko.spikotech.com")
  # Change this based on the number of pages you want to scrape

# Loop through the specified number of pages

    # Extract page source and parse it using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Loop through each product entry and extract details

links = []
for data in soup.findAll("div", attrs={"class": "card-body text-center"}):
        link = data.find("a")
        if link:
            links.append(link["href"])

        info = data.findAll("h7")
        Instructor.append(info[0].text)
        Semester.append(info[1].text)

for link in links:
        driver.get(web + link)

        content1 = driver.page_source
        soup1 = BeautifulSoup(content1, "html.parser")

        code = soup1.find("div", attrs={"id": "CourseCode"})
        if code is not None:
            CourseCode.append(code.text)

        course = soup1.find("h5", attrs={"id": "CourseName"})
        if course is not None:
            Title.append(course.text)

        desc = soup1.find("p", attrs={"id": "CourseDescription"})
        if desc is not None:
            Description.append(desc.text)

        clo = soup1.find("ul", attrs={"id": "CourseClos"})
        if clo is not None:
            item = clo.find_all("li")
            cloList = (
                [it.text.strip() for it in item] if item else ["CLO not found."] * 4
            )
            CLO1.append(cloList[0] if len(cloList) > 0 else "No CLO Found")
            CLO2.append(cloList[1] if len(cloList) > 1 else "No CLO Found")
            CLO3.append(cloList[2] if len(cloList) > 2 else "No CLO Found")
            CLO4.append(cloList[3] if len(cloList) > 3 else "No CLO Found")

        books = soup1.find("ul", attrs={"id": "CourseBooks"})
        if books:
            bookItems = books.find_all("li") if books else None
            bookList = (
                [item.text.strip().replace("\t", " ") for item in bookItems]
                if bookItems
                else ["Text Book not found."] * 2
            )
            TextBook1.append(
                bookList[0] if len(bookList) > 0 else "Text Book not found."
            )
            TextBook2.append(
                bookList[1] if len(bookList) > 1 else "Text Book not found."
            )

df = pd.DataFrame(
        {
            "CourseCode": CourseCode,
            "Title": Title,
            "Description": Description,
            "CLO1": CLO1,
            "CLO2": CLO2,
            "ClO3": CLO3,
            "CLO4": CLO4,
            "TextBook1": TextBook1,
            "TextBook2": TextBook2,
            "Instructor": Instructor,
            "Semester": Semester,
        }
    )
          
# Create a DataFrame with the extracted data

# Save the data to a CSV file
df.to_csv('eduko.csv', index=False, encoding='utf-8')

# Close the driver
driver.quit()
