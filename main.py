headers = {
    'Accept-Language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

import requests
from bs4 import BeautifulSoup
import smtplib

adminID = input("Enter your Gmail ID: ")
adminPA = input("Enter your Gmail PASSWORD: ")

url = input("Enter the URL of the product.\n")
buy_price = int(input("Enter the Buying Price: "))
userID = input("Enter your Mail ID: ")
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
price = (soup.find('span', class_='a-size-medium a-color-price priceBlockBuyingPriceString').string).split()

price = price[0].split(',')
total = ''
for p in price:
    total += p
new_price = (float(total[1:]))

if buy_price > new_price:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        result = connection.login(adminID, adminPA)
        message = f'Price Alert!! New Price = {new_price}.'
        connection.sendmail(adminID, userID, f"Subject:Amazon Price Alert!\n\n{message}\n{url}")