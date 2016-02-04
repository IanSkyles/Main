import re, urllib, csv
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen
from collections import deque


#reads the inital text file to extract all nodes to visit first.
def getInitialLinks(filename):
    urlsFile = open(filename, 'r')
    fileContents = urlsFile.readlines()
    urlsToVisit = [s.rstrip('\n') for s in fileContents]
    return urlsToVisit

def testgetInitialLinks():
    print (getInitialLinks("urls2.txt") == [])
    allseenlinks = {}
    allseenwords = {}
    if(getInitialLinks("urls2.txt") != ['']):
        bfsWebsiteCrawl(getInitialLinks, 1, allseenlinks, allseenwords)
    print (getInitialLinks("urls.txt") ==
           ['http://einstein.biz/',
            'http://www.cosc.canterbury.ac.nz/mukundan/dsal/MSort.html',
            'https://www.google.com/'])
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


#input: list of urls to crawl, nodes to crawl, allseenlinks which is a dictionary of links and # of occurneces for the link
#output: ?
def bfsWebsiteCrawl(BFStheseURLs, numNodesToCrawl,
                    allseenlinks, allseenwords, crawlspace):
    
    #visitedUrls = set(initialUrls) #keep track of which nodes we have visited
    highestLinkCount = 0
    linkWithHighestCount = "Not Yet Determined"
    countCrawled = 0
    while BFStheseURLs and countCrawled != numNodesToCrawl:
        countCrawled = countCrawled + 1
##        node = startingUrls.popleft()
        node = BFStheseURLs.popleft()
        print(node)
        textOfUrl, links = callUrl(node) 
        if links == [""]:
            print ("No Links or site 404/403")
        else:
            crawlspace[node] = links #keep track of crawlspace
            for link in links:
                getallwords(link, allseenwords) #update (or make new entry) for the word count
                if link not in allseenlinks:
                    BFStheseURLs.append(link)
                    allseenlinks[link] = allseenlinks.get(link,0) + 1
##        print("Url with higest link count = " + linkWithHighestCount)
##        print("Higest Link Count = " + str(highestLinkCount))
##        print (str(countCrawled) + " = count crawled")
##        print("Count found based on initial = " + str(countFoundBasedOnInitial))
##        print()
##        print()
##        print()

#input = a url to get the text and links of
#returns text of the url, http/https links of url, link count of url
def callUrl(url):
    req  = Request(url)
    print(url)
    urlText = ""
    urlLinks = [""]
    try:
        response = urlopen(req)
        print ("Succesfully crawling website")
        urlText = getText(response)
        urlLinks = get_http_and_https_LinksFromText(urlText)
        
    except HTTPError as e:
        if hasattr(e, '403'):
            print('403 error')
        elif hasattr(e, '404'):
            print('404 error')
        else:
            print('Error code: ', e.code)
    return urlText, urlLinks


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
    #match = (re.findall('<a[^>]*href="(.*?)"', theText))
    match = (re.findall(r'https*://\w*.\w*.\w+[a-zA-z/.]*', theText))
    for link in match:
        if "http" in link:
##            print (link)
##            print ()
            httpLinks.append(link)
    return httpLinks

def initializeLinkSeenCounter(linkcounts, startingUrls, allseenwords):
    for x in startingUrls:
        linkcounts[x] = linkcounts.get(x,0) + 1

##def filterTheseWords(word)
##    return word == "http" or word == "https" or word == "www" or word == "com":
##dumb idea ^ - just remove all of these from the dictionary before printing word cloud - more efficent.
def getallwords(link, allseenwords):
    for word in (re.findall(r"[\w']+", link)):
        allseenwords[word] = allseenwords.get(word,0) + 1

def testgetallwords():
    allseenwords = {}
    getallwords("http://www.cosc.canterbury.ac.nz/mukundan/dsal/MSort.html",allseenwords)
    print(allseenwords)
    allseenwords = {}
    getallwords("https://www.google.com/",allseenwords)
    print(allseenwords)
    allseenwords = {}
    getallwords("http://einstein.biz/",allseenwords)
    print(allseenwords)
    allseenwords = {}
def testgetallwordsMultiple():
    allseenwords = {}
    getallwords("http://www.cosc.canterbury.ac.nz/mukundan/dsal/MSort.html",allseenwords)
    print(allseenwords)
    getallwords("https://www.google.com/",allseenwords)
    getallwords("https://www.google.com/",allseenwords)
    print(allseenwords)
    getallwords("http://einstein.biz/",allseenwords)
    getallwords("http://einstein.biz/",allseenwords)
    getallwords("http://einstein.biz/",allseenwords)
    getallwords("http://einstein.biz/",allseenwords)
    print(allseenwords)


###testing
##testgetInitialLinks()
##testgetallwords()
##testgetallwordsMultiple()

def getTop15Words(allseenwords):
    if (len(allseenwords) > 15):
        sortwords = sorted(allseenwords.values()) # ascending order
        for i in range(0, -16, -1): #from 0 to -16
            print(sortwords[i])

#startingUrls is a queue that will be used for bfs.
startingUrls = deque(getInitialLinks("urls.txt"))
if(startingUrls != ['']):
    #print ("The starting urls are \n" + str(startingUrls) +"\n\n\n")
    #all of this could be done in dict of dict of dict but,
    #this is less complicated and easier to read 
    crawlspace = {} #tracks the 
    allseenwords = {} #tracks every seen word - (String word, Int times seen)
    linkcounts = {} #tracks every seen link - (String url, int times seen)
    initializeLinkSeenCounter(linkcounts,startingUrls, allseenwords)
    bfsWebsiteCrawl(startingUrls, 15, linkcounts, allseenwords, crawlspace)
    print()
    print(max(allseenwords, key=allseenwords.get)) #prints the key with max value
    print(getTop15Words(allseenwords))
else: print("Empty .txt file")


##print(queueOfUrls)
##for url in startingUrls:
##    callUrl(url)
#callUrl(startingUrls[1])   2
