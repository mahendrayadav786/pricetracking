import requests
from bs4 import BeautifulSoup
import smtplib
URL = "https://www.amazon.in/Alchemist-Paulo-Coelho/dp/8172234988/?_encoding=UTF8&pd_rd_w=VtN1y&pf_rd_p=e60c70f0-0541-4ba5-b6fc-ada95198a5fe&pf_rd_r=BBFB77GD2ZW7SKA1RVKP&pd_rd_r=9c35f843-7145-4e67-b727-d685194f1124&pd_rd_wg=BMepJ&ref_=pd_gw_crs_zg_bs_976389031"
my_headers ={

"Accept-Language":"en-US,en-GB;q=0.9,en;q=0.8",

"User-Agent" :"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"

 }


response = requests.get(URL, headers= my_headers)
data= response.text

soup= BeautifulSoup(data, "lxml")

price= soup.find(id="buyNewSection").get_text()
price_without_currency= price.split("₹")[1]
actual_price = float(price_without_currency)
title = soup.find(id="productTitle").get_text().strip()
price= soup.find(id="buyNewSection").get_text().split("₹")[1]
BUY_PRICE = 200
YOUR_EMAIL = "my8437448151@gmail.com"
YOUR_PASSWORD = "My8437448151@"
EMAIL = "myadav8151@yahoo.com"
if actual_price < BUY_PRICE:


     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
         connection.starttls()
         result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
         connection.sendmail(
             from_addr=YOUR_EMAIL,
             to_addrs= EMAIL ,
             msg=f"Subject:Amazon Price Alert!\n\n{title} is now {price}\n{URL}"
         )


