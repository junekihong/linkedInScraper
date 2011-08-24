# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import json


class LinkedinPipeline(object):
    def __init__(self):
    	self.file = open('items.txt','wb')
    
    def process_item(self, item, spider):
        #return item
        
        #line = json.dumps(dict(item)) + "\n"
        
        
        thing = dict(item)
        
        #####################################################################################################
        name 				= json.dumps(thing['name'])
        headlineTitle 		= json.dumps(thing['headlineTitle'])
        location 			= json.dumps(thing['location'])
        industry 			= json.dumps(thing['industry'])
        
        overviewCurrent 	= json.dumps(thing['overviewCurrent'])
        overviewEducation 	= json.dumps(thing['overviewEducation'])
        
        connections			= json.dumps(thing['connections'])
        
        experienceHead1		= json.dumps(thing['experienceHead1'])
        expTimeStart1		= json.dumps(thing['expTimeStart1'])
        expTimeEnd1			= json.dumps(thing['expTimeEnd1'])
        expTimeDuration1	= json.dumps(thing['expTimeDuration1'])
        
        experienceHead2		= json.dumps(thing['experienceHead2'])
        expTimeStart2		= json.dumps(thing['expTimeStart2'])
        expTimeEnd2			= json.dumps(thing['expTimeEnd2'])
        expTimeDuration2	= json.dumps(thing['expTimeDuration2'])
        
        experienceHead3		= json.dumps(thing['experienceHead3'])
        expTimeStart3		= json.dumps(thing['expTimeStart3'])
        expTimeEnd3			= json.dumps(thing['expTimeEnd3'])
        expTimeDuration3	= json.dumps(thing['expTimeDuration3'])
        
        experienceHead4		= json.dumps(thing['experienceHead4'])
        expTimeStart4		= json.dumps(thing['expTimeStart4'])
        expTimeEnd4			= json.dumps(thing['expTimeEnd4'])
        expTimeDuration4	= json.dumps(thing['expTimeDuration4'])
        
        experienceHead5		= json.dumps(thing['experienceHead5'])
        expTimeStart5		= json.dumps(thing['expTimeStart5'])
        expTimeEnd5			= json.dumps(thing['expTimeEnd5'])
        expTimeDuration5	= json.dumps(thing['expTimeDuration5'])
        
        
        
        educationSchool1	= json.dumps(thing['educationSchoolName1'])
        educationDegree1	= json.dumps(thing['educationDegree1'])
        educationMajor1		= json.dumps(thing['educationMajor1'])
        eduTimeStart1		= json.dumps(thing['eduTimeStart1'])
        
        educationSchool2	= json.dumps(thing['educationSchoolName2'])
        educationDegree2	= json.dumps(thing['educationDegree2'])
        educationMajor2		= json.dumps(thing['educationMajor2'])
        eduTimeStart2		= json.dumps(thing['eduTimeStart2'])
        
        educationSchool3	= json.dumps(thing['educationSchoolName3'])
        educationDegree3	= json.dumps(thing['educationDegree3'])
        educationMajor3		= json.dumps(thing['educationMajor3'])
        eduTimeStart3		= json.dumps(thing['eduTimeStart3'])
        
        
        #additionalAwards	= json.dumps(thing['additionalAwards'])
        #contactFor			= json.dumps(thing['contactFor'])
        
        #####################################################################################################
        delimiter = " # "
        
        
        
        line = name + delimiter + headlineTitle + delimiter + location + delimiter + industry + delimiter
        line = line + overviewCurrent + delimiter + overviewEducation + delimiter + connections + delimiter
        
        line = line + experienceHead1 + delimiter
        line = line + expTimeStart1 + delimiter
        line = line + expTimeEnd1 + delimiter
        line = line + expTimeDuration1 + delimiter
        
        line = line + experienceHead2 + delimiter
        line = line + expTimeStart2 + delimiter
        line = line + expTimeEnd2 + delimiter
        line = line + expTimeDuration2 + delimiter
        
        line = line + experienceHead3 + delimiter
        line = line + expTimeStart3 + delimiter
        line = line + expTimeEnd3 + delimiter
        line = line + expTimeDuration3 + delimiter
        
        line = line + experienceHead4 + delimiter
        line = line + expTimeStart4 + delimiter
        line = line + expTimeEnd4 + delimiter
        line = line + expTimeDuration4 + delimiter
        
        line = line + experienceHead5 + delimiter
        line = line + expTimeStart5 + delimiter
        line = line + expTimeEnd5 + delimiter
        line = line + expTimeDuration5 + delimiter
        
        
        
        line = line + educationSchool1 + delimiter + educationDegree1 + delimiter + educationMajor1 + delimiter + eduTimeStart1 + delimiter
        
        line = line + educationSchool2 + delimiter + educationDegree2 + delimiter + educationMajor2 + delimiter + eduTimeStart2 + delimiter
        
        line = line + educationSchool3 + delimiter + educationDegree3 + delimiter + educationMajor3 + delimiter + eduTimeStart3 + delimiter
        
        
        #line = line + additionalAwards + " ## "
        
        line = line + '\n'
        #####################################################################################################
        
        exampleLine = "Name" + delimiter + "Headline Title" + delimiter + "Location" + delimiter + "Industry" + delimiter + "Overview Current" + delimiter + "Overview Education" + delimiter + "Connections" + delimiter + "Experience Title 1" + delimiter + "Time Began 1" + delimiter + "Time Ended 1" + delimiter + "Duration 1" + delimiter + "Experience Title 2" + delimiter + "Time Began 2" + delimiter + "Time Ended 2" + delimiter + "Duration 2" + delimiter + "Experience Title 3" + delimiter + "Time Began 3" + delimiter + "Time Ended 3" + delimiter + "Duration 3" + delimiter + "Experience Title 4" + delimiter + "Time Began 4" + delimiter + "Time Ended 4" + delimiter + "Duration 4" + delimiter + "Experience Title 5" + delimiter + "Time Began 5" + delimiter + "Time Ended 5" + delimiter + "Duration 5" + delimiter 
        
        #self.file.write(exampleLine)
        
        self.file.write(line)
        
        
        #for x,y in dict(item).iteritems():
        #	print json.dumps(x) + "\t\t\t = " +json.dumps(y)
        
        #for x,y in dict(item).iteritems():
        #	print json.dumps(x) +": "
        #	for z in y:
        #		print "\t"+json.dumps(z)
        		
       	
        
        
        #self.file.write(line)
        return item
