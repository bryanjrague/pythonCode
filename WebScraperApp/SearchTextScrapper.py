from bs4 import BeautifulSoup #library which can parse HTML and XML into an object with properties
import requests

#build up our request to send as a HTTP GET request
search = input("Enter search term: ")
params = {"q": search}
#return the response of the request
resp = requests.get("http://www.bing.com/search", params=params)

#turn the response into a soup object from the text of the response busing the html.parser
soup = BeautifulSoup(resp.text, "html.parser")
print(soup.prettify()) #print the full soup object contents

#we can then find contents within the soup and do interesting things with it.
#using the soup object find method, can look for content
allLinks = soup.find_all("a") # returns a list of all HTML elements found with the <a> tag (links
#print the links found
print(" --- LINKS ---")
for link in allLinks:
    print(link.get('href')) # get/print the 'href' property of every html link element in the page.

#get all the images in the result and print their source
allImgs = soup.find_all("img")
print(" --- IMAGES ---")
for img in allImgs:
    print(img.get("src"))

#retrieve the text and link data for results of a search against bing
print(" --- TEXT AND LINKS OF LIST ITEMS ---")
orderLists = soup.find("ol", {"id": "b_results"}) # can look for particular attributes of a given element in the source
links = orderLists.find_all("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print("Text: ", item_text)
        print("Link: ", item_href)
        print("Parent: ", item.find("a").parent) # print the parent element containing the current element
        print("Summary: ", item.find("a").parent.parent.find("p").text) # can move up and down the soup heirarchy as needed

        children = item.children
        for child in children:
            print("Child: ", child)
    print(" ")

