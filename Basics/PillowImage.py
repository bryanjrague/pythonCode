import requests
from io import BytesIO
from PIL import Image
#this script retrieves an image and uses python packages to download the image file bytes and save it to
# file after logging some image properties.

#identify the url which the image exists at
targetURL = "https://images4.alphacoders.com/109/10944.jpg"
resp1 = requests.get(targetURL)
print("URL of image:",resp1.url)
print("Status Code:",resp1.status_code)

# this line turns the resp1 content into bytes, then opens it as an image
img = Image.open(BytesIO(resp1.content))
imgSavePath = "./image" + img.format

print("Image size:",img.size)
print("Image format:",img.format)
print("Image mode:",img.mode)

try:
    img.save(imgSavePath,img.format)
    print("Successfully saved img")
except IOError:
    print("Issue saving image...")

