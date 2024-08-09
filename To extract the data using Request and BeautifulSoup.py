import requests,openpyxl
from bs4 import BeautifulSoup
response = requests.get("https://www.commonsensemedia.org/movie-reviews")
soup = BeautifulSoup(response.text,'html.parser')
#overall = soup.find_all("body" ,class_="path-reviews")
for shows in soup.find_all("ul" ,class_="row"):
    print(shows.text)
print("Links")
for url in soup.find_all("a", class_="btn btn--neutral"):
    print(url.attrs['href'])
