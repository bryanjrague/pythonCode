'''
This script requests input on search text for images and how many images to retrieve.
Images are saved under the dir ./ScrappedImages/<searchTermsLowerCase>/
The script repeats requesting, downloading, and saving images indefinitely.
Force stop the script to exit.
'''

from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import re
import os

def start_search():

    search = input("Image search text: ")
    max_downloads = int(input("Number of images to find: "))

    save_dir = "./ScrappedImages/" + search.replace(" ", "_").lower()
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    params = {"q": search}
    resp = requests.get("http://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(resp.text, "html.parser")
    links = soup.find_all("a", {"class": "thumb"})

    downloads = 0

    for item in links:
        if downloads < max_downloads:
            try:
                img_obj = requests.get(item.attrs["href"]) # get image source file link
                img_title = item.attrs["href"].split("/")[-1] #set the title to the text appearing after the last / char in the link

                img_title = re.sub('[!@#$=?.<>]', '', img_title)  #remove chars icompatible with file names

                try:
                    img = Image.open(
                        BytesIO(img_obj.content)
                    )  # open the image content in bytes, then open the bytes as an Image
                    # save the image found in it's original format
                    img.save(save_dir + "/"+ img_title, img.format)
                    print("saved image: ", img_title)
                except:
                    print("Error attempting to download image file:",img_title)
                downloads += 1
            except:
                print("Error attempting GET request against", item.attrs["href"])
        else:
            break

    print("Done downloading",max_downloads,"images from search criteria:",search)
    start_search()

start_search()