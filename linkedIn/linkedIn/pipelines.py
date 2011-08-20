# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import json


class LinkedinPipeline(object):
    def __init__(self):
    	self.file = open('items.jl','wb')
    
    def process_item(self, item, spider):
        #return item
        
        #line = json.dumps(dict(item)) + "\n"
        
        exampleLine = "name ## headlineTitle ## location ## industry ## overviewCurrent ## overviewEducation ## connections ## "
        exampleLine = exampleLine + "additionalAwards ## contactFor ## "
        self.file.write(exampleLine + "\n\n")
        
        thing = dict(item)
        
        
        
        #####################################################################################################
        name 				= json.dumps(thing['name'])
        headlineTitle 		= json.dumps(thing['headlineTitle'])
        location 			= json.dumps(thing['location'])
        industry 			= json.dumps(thing['industry'])
        
        overviewCurrent 	= json.dumps(thing['overviewCurrent'])
        overviewEducation 	= json.dumps(thing['overviewEducation'])
        
        connections			= json.dumps(thing['connections'])
        
        additionalAwards	= json.dumps(thing['additionalAwards'])
        contactFor			= json.dumps(thing['contactFor'])
        
        #####################################################################################################
        line = name + " ## " + headlineTitle + " ## " + location + " ## " + industry + " ## " 
        line = line + overviewCurrent + " ## "+overviewEducation+" ## "+connections+" ## "
        
        line = line + additionalAwards + " ## " + contactFor + " ## "
        #####################################################################################################
        
        self.file.write(line)
        
        
        #for x,y in dict(item).iteritems():
        #	print json.dumps(x) + "\t\t\t = " +json.dumps(y)
        
        #for x,y in dict(item).iteritems():
        #	print json.dumps(x) +": "
        #	for z in y:
        #		print "\t"+json.dumps(z)
        		
       	
        
        
        #self.file.write(line)
        return item
