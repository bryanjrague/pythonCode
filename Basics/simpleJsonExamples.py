#applications often need a way to save the status and then reload it and continue at a later time.
#Python has the ability to work with JSON using simplejson package

#we can rename imported libraries for ease-of-use within the python code
import simplejson as json #this lets us refer to simplejson functions as 'json'
import os

#repeat creating/loading and incrementing age data a few times
for i in range(3): # loops as long as x is not 3, so three timesa
    #check if a file exists or not using the os class
    if os.path.isfile("./ages.json") and os.stat('./ages.json').st_size != 0: #returns true if the file exists and has contents
        old_file = open("./ages.json", "r+")
        #load the file contents and convert it to a json object via the loads() function
        data = json.loads(old_file.read())
        print("Current age is",data["age"], "-- Now adding a year ")
        data["age"] = data["age"] + 1
        print("New age is",data["age"])
    else: # we need to create the age json file
        old_file = open("./ages.json", "w")
        #create the data as a python dictionary object
        data = {"name": "Bryan", "age": 30}
        print("No file found, setting default file data.")

    #now that we have a file and data defined whether or not it previously existed,
    # write the new file in json formatted text.
    #the seek function moves the curson to the integer character position provided
    old_file.seek(0)
    old_file.write(json.dumps(data))
    old_file.close() #close the file when you're done with it.