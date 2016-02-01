##import re
##filevar = open("declaration.txt", 'r')
##
##matches = 0
##endInY = 0
##ar = 0
##four = 0
###listOfVowels = ['a','e','i','o', 'u', 'y']
##for line in filevar:
##    x = re.findall("\wy\W", line)
##    if(x != None):
##        endInY += len(x)
##    #x = re.findall("\sa.*r\W", line)
##    x = re.findall(r'\ba\w*r\W', line)
##    #print(x)
##    if(x != None):
##        ar += len(x)
##    #x = re.findall("\w.[aeiou][aeiou].[\s\w]", line)
##    x = re.findall(r'\b\w[aeiou]{2}\w\b', line)
##    if(x != None):
##        four += len(x)
##        
##
##print (endInY) #72
##print (ar) #4
##print (four) #14
##
####Let's write the code that reads the file line by line and returns
####– All words ending in y (72)
####– All words starting with a and ending in r (4)
####– All four-letter words where the middle two letters are vowels
import re, urllib, urllib.request

urlsFile = open("urls.txt", 'r')#open file for reading

x = urlsFile.readlines()
#print (x)  #urls still have new line characters here.
#for y in x: #PROBLEM - doesnt save new urls
#    print(y.rstrip('\n'))


stripped_new_lines_out_of_urls = [s.rstrip('\n') for s in x] #works to strip new line characte
print (stripped_new_lines_out_of_urls)

for url in stripped_new_lines_out_of_urls:
    page = urllib.request.urlopen('https://www.google.com/') # url # 'http://www.tacoma.uw.edu/institute-technology/institutetechnology'
    pageText = page.read()
    #print (pageText)    
    pageText = str(pageText)
    
    match = (re.findall('<a[^>]*href="(.*?)"', pageText))
    print (len(match))
    print(match)
    for line in match:
        if "http" in line:
            print (line)
    match = (re.findall('<a[^>]*href ="(.*?)"', pageText))    
    print (len(match))
    match = (re.findall('<a[^>]*href = "(.*?)"', pageText))
    print (len(match))
    
    match = (re.findall('<a[^>]*href= "(.*?)"', pageText))
    print (len(match))
    #print (match.group(1))
    #print (re.findall(r'\bhref="http:\w*</a>\W', pageText)) #re.findall(r'\b<a href = "http:\w*</a>\W', pageText

