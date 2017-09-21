#persistence is native to python, no lib imports needed!



#the .open function takes 2 args: filename to create/open, the mode which determines
# what actions can be carried out on the file
#file path can be absolute, otherwise it must be in the current dir.

''' t Modes
‘r’ – Read mode which is used when the file is only being read
‘w’ – Write mode which is used to edit and write new information to the file
    (any existing files with the same name will be erased when this mode is activated)
‘a’ – Appending mode, which is used to add new data to the end of the file; that is new
    information is automatically amended to the end
‘r+’ – Special read and write mode, which is used to handle both actions when working with a file
'''

myFile = open("test_OpenFile.txt", "w")

sampleTextStr = "This data is being written to the text file"

#to write data to the file, pass the variable containing the data to the write() function
myFile.write(sampleTextStr)

myFile.close()

myFile = open("test_OpenFile.txt", "a")
moreTextStr = "\nOpened the file again and appended this info."
myFile.write(moreTextStr)
myFile.close()

#read the file and print each line of the file to console/terminal
#additionally store all words of each line into a list
wordList = []
with open("test_OpenFile.txt") as file:
    print("Lines from file:\n")
    for line in file:
        lineWords = line.split()
        wordList.append(lineWords)
        print(line)

print("Words List =",wordList)

