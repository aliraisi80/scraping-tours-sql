import requests
import selectorlib
import time

from send_email import send_email

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

def scrape(url):
   """ Scrape the page source from the URL"""
   reaponse = requests.get(url, headers=HEADERS)
   source = reaponse.text
   return source

def extract(source):
   extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
   value = extractor.extract(source)["tours"]
   return value

def store(extracted):
   with open("deta.txt","a") as file:
      file.write(extracted + "\n")

def read(extracted):
   with open("deta.txt","r") as file:
      return  file.read()


if __name__ == "__main__":
   while True:
      scraped = scrape(URL)
      extracted = extract(scraped)
      print(extracted)
      if extracted != "No upcoming tours":
         if extracted not in read("deta.txt"):
            store(extracted)
            send_email(message="Subgect: Test',\n  Hey, you found new music event!")
      time.sleep(10)
