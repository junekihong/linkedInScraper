from sys import argv

#README: in order to run this script, just type into the command line: python parser.py theFileYouWantToParse.html


script, inputFile = argv

#we go ahead and open up the input file and store it as a string
currentFile = open(inputFile)
fileString = currentFile.read()


# taken from http://wiki.python.org/moin/EscapingHtml
#######################################
def unescape(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    # this has to be last:
    s = s.replace("&amp;", "&")
    return s    
########################################




def searchAndCut(fileString, startMarker, endMarker):
    startIndex = fileString.find(startMarker)
    if startIndex == -1:
        return "N/A"
      
    startIndex+= len(startMarker)
    endIndex = fileString[startIndex:].find(endMarker) 
        
    if endIndex == -1:
       return "N/A"
                
    endIndex+= startIndex
    returnString = fileString[startIndex:endIndex].strip()            
    return unescape(returnString)
    
            
def searchAndFind(fileString, startMarker):
    startIndex = fileString.find(startMarker)
    if startIndex == -1:
        return "N/A"
    startIndex += len(startMarker)
    
    returnString = fileString[startIndex:].strip()
    return unescape(returnString)
    
    


def getFirstName(fileString):
    return searchAndCut(fileString, "<span class=\"given-name\">", "</span>")

def getLastName(fileString):
    return searchAndCut(fileString, "<span class=\"family-name\">", "</span>")

def getHeadline(fileString):
    return searchAndCut(fileString, "<p class=\"headline-title title\" style=\"display:block\">", "</p>")

def getLocation(fileString):
    return searchAndCut(fileString, "<span class=\"locality\">","</span>")

def getIndustry(fileString):
    return searchAndCut(fileString, "<dd class=\"industry\">","</dd>")


#the next few are a bit harder ... because there can be more than one listed. (multiple schools, multiple jobs, etc)


def getCurrent(fileString):
    current = []
    data = searchAndCut(fileString, "<ul class=\"current\">", "</ul>")
    
    if data == "N/A":
        return data
    
    startIndex = data.find("<li>")
    
    while startIndex != -1:
        endIndex = data.find("</li>")
        unprocessed = unescape(data[startIndex:endIndex]).replace("\n","")
        position = searchAndCut(unprocessed,"<li>","<span class=\"at\">").strip()
        company = unprocessed[unprocessed.find("</span>")+ len("</span>"):].strip()
        
        current.append(position+" at "+company)
        endIndex+= len("</li>")
        data = data[endIndex:]
        startIndex = data.find("<li>")
        
    return current
    
    
def getPast(fileString):
    past = []
    data = searchAndCut(fileString, "<ul class=\"past\">", "</ul>")
    
    if data == "N/A":
        return data
    
    startIndex = data.find("<li>")
    
    while startIndex != -1:
        endIndex = data.find("</li>")
        unprocessed = unescape(data[startIndex:endIndex]).replace("\n","")
        position = searchAndCut(unprocessed,"<li>","<span class=\"at\">").strip()
        company = unprocessed[unprocessed.find("</span>")+ len("</span>"):].strip()
        
        past.append(position+" at "+company)
        endIndex += len("</li>")
        data = data[endIndex:]
        startIndex = data.find("<li>")
        
    return past
    
    
def getEducation(fileString):
    education = []
    data = searchAndCut(fileString, "<dd class=\"summary-education\" style=\"display:block\">", "</dd>")
    data = searchAndCut(data, "<ul>", "</ul>")
    
    if data == "N/A":
        return data
        
    startIndex = data.find("<li>")
    
    while startIndex != -1:
        startIndex+= len("<li>")
        endIndex = data.find("</li>")
        if endIndex == -1:
            return education
        school = data[startIndex:endIndex].replace("\n","").strip()
        endIndex += len("</li>")
        education.append(unescape(school))
        data = data[endIndex:]
        startIndex = data.find("<li>")
    return education
    
def getRecommendations(fileString):
    data = searchAndCut(fileString, "Recommendations", "</dd>")
    data = searchAndCut(data, "<strong>","</strong>")
    return data
    
def getConnections(fileString):
    data = searchAndCut(fileString, "Connections","</dd>")
    data = searchAndCut(data,"<strong>","</strong>")
    return data

def getWebsites(fileString):
    websites = []
    data = searchAndCut(fileString,"<dd class=\"websites\">","</dd>")
    if data == "N/A":
        return data
    startIndex = data.find("<li>")
    
    while startIndex != -1:
        startIndex+= len("<li>")
        endIndex = data.find("</li>")
        if endIndex == -1:
            return websites
        website = data[startIndex:endIndex].replace("\n","").strip()
        website = searchAndCut(website,"<a href=\"/redirect?url=","&urlhash=nAvp").replace("%2E",".").replace("%3A",":").replace("%2F","/")
        endIndex += len("</li>")
        websites.append(unescape(website))
        data = data[endIndex:]
        startIndex = data.find("<li>")
    return websites

print 
print "First Name: %s" % (getFirstName(fileString))
print "Last Name: %s" % (getLastName(fileString))
print "Headline: %s" % (getHeadline(fileString))
print "Location: %s" % (getLocation(fileString))
print "Industry: %s" % (getIndustry(fileString))
print
print "Current: %s" % (getCurrent(fileString))
print "Past: %s" % (getPast(fileString))
print "Education: %s" % (getEducation(fileString))
print "Recommendations: %s" % (getRecommendations(fileString))
print "Connections: %s" %(getConnections(fileString))
print "Websites: %s" %(getWebsites(fileString))
