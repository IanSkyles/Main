import re, urllib, csv
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen
from collections import deque


#reads the inital text file to extract all nodes to visit first.
def getInitialLinks():
    urlsFile = open("urls.txt", 'r')
    fileContents = urlsFile.readlines()
    urlsToVisit = [s.rstrip('\n') for s in fileContents]
    #print (urlsToVisit)
    return urlsToVisit

##class HighestLinkNumber:
##    def __init__(self, value, link):
##        self.value = value
##        self.link = []
##        self.link.append(link)
##    def __init__(self):
##        self.value = 0
##        self.link = ""
##    def setValue(self, theValue, theLink):
##        if theValue > self.value:
##            self.value = theValue
##            self.link = theLink
##        elif theValue == self.value:
##            self.link.append(theLink)
##    def setValueOnTrue(self, theValue):
##        if theValue >= self.value:
##            return True
##        else: return False
##            
##    def getValue(self):
##        return self.value

## Algorithm for breadth first search.
##BFS(Node start) {
##  initialize queue q and enqueue start
##  mark start as visited
##  while(q is not empty) {
##    next = q.dequeue() // and “process”
##    for each node u adjacent to next
##     if(u is not marked)
##       mark u and enqueue onto q
##  }


#input: list of urls to crawl, nodes to crawl
#output: ?
def bfsWebsiteCrawl(initialUrls, numNodesToCrawl):
##    #queueOfUrls = deque(initialUrls) #keep track of node to visit next
##    queueOfUrls =deque([])
##    for x in initialUrls:
##        wrap_list = [x]
##        queueOfUrls.append(x) 
##    print(queueOfUrls)
    visitedUrls = set(initialUrls) #keep track of which nodes we have visited
    highestLinkCount = 0
    linkWithHighestCount = ""
    print (visitedUrls)
    while initialUrls and numNodesToCrawl > 0:
        print(str(highestLinkCount))
        numNodesToCrawl = numNodesToCrawl - 1
        node = startingUrls.popleft()
        print (node)
        textOfUrl, links, urlLinkCount = callUrl(node)
        if(urlLinkCount > highestLinkCount):
            print (str(urlLinkCount) + ">" + str(highestLinkCount))
            highestLinkCount = urlLinkCount
            print(str(highestLinkCount))
            linkWithHigestCount = node
        
        if urlLinkCount == 0:
            print ("No Links or site 404/403")
        else:
            print (links)
            for link in links:
                if link not in visitedUrls:
                    initialUrls.append(link)
                    visitedUrls.add(link)
        print("Url with higest link count = " + linkWithHighestCount)
        print("Higest Link Count = " + str(highestLinkCount))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()        
##        
##        print (type(urlLinkCount))
##        print (type(highestLinkCount))
##        print (str(urlLinkCount) + " > " + str(highestLinkCount))
##        print ((urlLinkCount > highestLinkCount))
##        if ((urlLinkCount > highestLinkCount) == True):
##                highestLinkCount = urlLinkCount
##                linkWithHighestCount = node
        
                
        
    

#input = a url to get the text and links of
#returns text of the url, http/https links of url, link count of url
def callUrl(url):
    req  = Request(url)
    urlText = ""
    urlLinkCount = 0
    urlLinks = [""]
    try:
        response = urlopen(req)
        print ("Succesfully crawling website")
        urlText = getText(response)
        urlLinkCount, urlLinks = get_http_and_https_LinksFromText(urlText)
        
    except HTTPError as e:
        if hasattr(e, '403'):
            print('403 error')
        elif hasattr(e, '404'):
            print('404 error')
        else:
            print('Error code: ', e.code)
    print (urlLinkCount)
    return urlText, urlLinks, urlLinkCount


#returns the text from a response 
def getText(theResponse):
    responseText = theResponse.read()
    responseText = str(responseText)
    return responseText

#gets all the http and https links from the text
#returns linkCount and all the links
def get_http_and_https_LinksFromText(theText):
    #print(theText)
    httpLinks  = []
    httpLinkCount = 0
    match = (re.findall('<a[^>]*href="(.*?)"', theText))
    for link in match:
        if "http" in link:
            print (link)
            print ()
            httpLinks.append(link)
            httpLinkCount += 1
    return httpLinkCount, httpLinks
    

##def visitUrl(url):
##    #page = urllib.request.urlopen(url)
##    print(url)
##    req = Request(url)
##    print (req)
##    try:
##        response = urlopen(req) #if this fails go to except
##        linksVisited.append(url)
##        responseText = response.read()
##        responseText = str(responseText)
##        match = (re.findall('<a[^>]*href="(.*?)"', responseText))
##        print (len(match))
##        httpLinks = []        
##        for link in match:
##            print (link)
##            if "http" in link:
##                print ("yes")
##                httpLinks.append(link)
##            else:
##                print("no")
##            print ()
##        httpLinksList.append(httpLinks)
##        print (httpLinksList[0])
##    except HTTPError as e:
##        if hasattr(e, '403'):
##            print('403 error')
##        elif hasattr(e, '404'):
##            print('404 error')
##        else:
##            print('Error code: ', e.code)
##    except URLError as e:
##        print('We failed to reach a server.')
##        print('Reason: ', e.reason)
##    print ("HERE")


#visitUrl(urlsToVisit[0])
##f = HighestLinkNumber()
##print(f.getValue())
##f.setValue(5, "noob")
##print(f.getValue())
##f.setValue(4, "noob")
##print(f.getValue())
##f.setValue(5, "noob")
####print(f.getValue())
##def test():
##    msg = 'afdssav'
##    myq = deque([msg])
##    myq.append('asdf')
####    print(myq.popleft())
##test()

startingUrls = deque(getInitialLinks())
print (startingUrls)
##print(queueOfUrls)
##for url in startingUrls:
##    callUrl(url)
#callUrl(startingUrls[1])   2
bfsWebsiteCrawl(startingUrls,6)
