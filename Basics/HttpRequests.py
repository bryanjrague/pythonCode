# the requests package is one which supports HTTP requests, there are others which may be better suited for other
# request tasks and processing
import requests

#get is a function for retrieving response data via HTTP
targetDomain = "google"
response = requests.get("http://"+targetDomain+".com") # this gets the html of the target path
print("URL: ",response.url)
print("Status: ", response.status_code) #status code gets the HTTP status of the response object

print("Page HTML Text:\n",response.text) # prints all the html text for the page

#can then do interesting things with the html, such as simply writing it to a file.
f = open("./"+str(targetDomain)+".html","w+")
f.write(response.url)
f.write(str(response.status_code))
f.write(response.text)
f.close()

# we can then do interesting things with web pages by implementing GET requests when retrieving web page data
# in this case, we are copying the google search URL parameters when a search is being done
getParams = "#q=spaceship"
print("Running google search:","https://",targetDomain,getParams)
r2 = requests.get("https://"+targetDomain+".com", getParams) # send a HTTP request including a search parameter

#we can also do HTTP POST actions using the requests package
my_data = {"name": "B-monay", "email": "example@example.com"}
print("Running POST to website")
#post to a url which is expecting input and save the response given by the webpage to afile
r3 = requests.post("http://www.w3schools.com/php/welcome.php", data=my_data)
print("Status of target post URL is:",r3.status_code)
f2 = open("./myFile.html", "w+")
f2.write(r3.text)
f2.close()
print("saved Post response to file")