'''
Webscraping practice, understanding HTML parametes, ways to parsing data, and save data

NOTE: With webscraping, websites are constantly being updated and patched, so as of today 17 JUN 2023 this code works. At some point in the future it may not. 
'''
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

holidayhomes = [] # create an empty list to store data collected 

for x in range(1,3): # initiate for loop for pagination, in this case ther are only 2 pages at the time

    url = f"https://www.simplyowners.net/holiday-cottages-dordogne-france/page-{x}/" # URL we want to web crawl with the variable 'x' representing the page number 

    r = requests.get(url) # send a GET request

    soup = BeautifulSoup(r.content, 'html.parser') # Parse html dat that we recieve from GET request

    content = soup.find_all('div', class_='bg-white rounded shadow') # Carve out main content we want to extract information from

    for property in content: # Initiate for loop to look for and extract all instances on the web page with the data I chose to Extract below
        link = property.find('a') # look for property link in the 'a' tag stroed in the content variable
        details = property.find('div', class_='propdetails') # Extract property details from div tag stored under the content variable
        traits = details.text.strip() # Strip out all white space and new lines '\n' from propdetails and store the output in the variable traits
        price = property.find('div', class_='price').text # Extract price information from the class 'price' located under the div tag stored in the content variable
        if link:
            href = 'https://www.simplyowners.net' + link.get('href') # Multiple 'a' tags are present so, look for href under the 'a' tag and store it in a variable called href.

        property_info = { # Store all extracted information in a dictionary
            'price':price,
            'link':href,
            'details':traits,}
        
        holidayhomes.append(property_info) # append extracted information from dictionary to the empty list holidayhomes

    print('Holiday Homes Found: ',len(holidayhomes)) # print the number of homes found on each page
    time.sleep(2) # wait 2 seconds in between requests

df = pd.DataFrame(holidayhomes) # Store the created list of holidaty homes in a dataframe
with open('French_Holiday_Homes.csv', 'w', newline='', encoding='utf-8') as file: # Open / create the file French_Holiday_Homes.csv and automatically close the file once writing is complete. the encoding='utf-8' parameter is added to handle any encoding issues that may occur while writing to the CSV file.
    df.to_csv(file, index=False) # save the dataframe 'df' to a csv file and exclude the default panda column of index

print(df) # print dataframe output
