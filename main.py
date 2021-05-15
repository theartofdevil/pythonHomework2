import re
import os

file = open('char1.txt', 'r')

data = file.read()
str1 = ""
for i in data.split("\n"):
    str2 = re.sub('[^A-Za-z ]+', '', i)
    str1 += str2
    str1 += '\n'
# closing the file
file.close()

myText = open(r'char1.txt','w')
myText.write(str1)
myText.close()

#To print edited file

file = open('char1.txt', 'r')
data = file.read()
for i in data.split("\n"):
    print(i)
file.close()