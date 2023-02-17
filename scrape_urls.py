from bs4 import BeautifulSoup
import requests
   
#bad
bad = ["/user/login", "/", "/cart", "/home", "/maps"]
hrefs = []

# lists
urls=[]
   
# function created
def scrape(site):
       
    # getting the request from url
    r = requests.get(site)
       
    # converting the text
    s = BeautifulSoup(r.text,"html.parser")
    #get all links   
    for tag in s.find_all("a"):
        
        #print(f"tag: {tag}")
        #get href value  
        #href = i.attrs['href']
        url = tag.get('href')
        if url is None:
            continue
        if url.startswith("https") == False:
            url = base+url
        print(f"url {url}")
        if url not in urls:
            urls.append(url)
            scrape(url)

   
# main function
if __name__ =="__main__":
   
    # website to be scraped
    site_scrape="https://redatlasbook.com/maps"
    base = "https://redatlasbook.com"
    # calling function
    scrape(site_scrape)
    print (urls)