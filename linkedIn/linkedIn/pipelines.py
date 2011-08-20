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
        
        line = json.dumps(dict(item)) + "\n"
        
        dictything = dict(item)
        print json.dumps(dict(item))
        what = dictything['name']
        print what
        print json.dumps(what)
        
        print 'asdf'
        
        for x,y in dict(item).iteritems():
        	print json.dumps(x) + "\t\t\t = " +json.dumps(y)
        
        for x,y in dict(item).iteritems():
        	print json.dumps(x) +": "
        	for z in y:
        		print "\t"+json.dumps(z)
        
        self.file.write(line)
        return item
