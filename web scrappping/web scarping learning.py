import requests 
from bs4 import BeautifulSoup 
import csv 
  
URL = "https://www.amazon.in/dp/B07DJD1RTM?pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e&pf_rd_r=Q6XJCYBJQV350N5NXY7Z"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 

print(soup.prettify())
