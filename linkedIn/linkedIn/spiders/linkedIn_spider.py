from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from linkedIn.items import linkedInItem

import random

sampling = True

def striplist(l):
	return ([x.strip().replace('\t',"") for x in l])				



class linkedInSpider(BaseSpider):
	name = "linkedin.com"
	allowed_domains = ["linkedin.com"]
	start_urls = [
		#"http://www.linkedin.com/pub/rokalight-a-roka-holding-b-v-company/36/530/5b5"
		"http://www.linkedin.com/pub/chandrashekar-a-s/22/677/79a"
		#"http://www.linkedin.com/directory/people/as.html"


		#"http://www.linkedin.com/directory/people/a.html",
        #"http://www.linkedin.com/directory/people/b.html",
        #"http://www.linkedin.com/directory/people/c.html",
        #"http://www.linkedin.com/directory/people/d.html",
        #"http://www.linkedin.com/directory/people/e.html",
        #"http://www.linkedin.com/directory/people/f.html",
        #"http://www.linkedin.com/directory/people/g.html",
        #"http://www.linkedin.com/directory/people/h.html",
        #"http://www.linkedin.com/directory/people/i.html",
        #"http://www.linkedin.com/directory/people/j.html",
        #"http://www.linkedin.com/directory/people/k.html",
        #"http://www.linkedin.com/directory/people/l.html",
        #"http://www.linkedin.com/directory/people/m.html",
        #"http://www.linkedin.com/directory/people/n.html",
        #"http://www.linkedin.com/directory/people/o.html",
        #"http://www.linkedin.com/directory/people/p.html",
        #"http://www.linkedin.com/directory/people/q.html",
        #"http://www.linkedin.com/directory/people/r.html",
        #"http://www.linkedin.com/directory/people/s.html",
        #"http://www.linkedin.com/directory/people/t.html",
        #"http://www.linkedin.com/directory/people/u.html",
        #"http://www.linkedin.com/directory/people/v.html",
        #"http://www.linkedin.com/directory/people/w.html",
        #"http://www.linkedin.com/directory/people/x.html",
        #"http://www.linkedin.com/directory/people/y.html",
        #"http://www.linkedin.com/directory/people/z.html"
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)	   	
		
		if not hxs.select('//body[@class="guest directory"]'): #if it is not a directory (its a regular page)
			item = linkedInItem()		
			item['name'] = striplist(hxs.select('//h1/span/span/text()').extract())
			item['headlineTitle'] = striplist(hxs.select('//p[@class="headline-title title"]/text()').extract())
			item['location'] = striplist(hxs.select('//dd/span/text()').extract())
			item['industry'] = striplist(hxs.select('//dd[@class="industry"]/text()').extract())		
			
			item['overviewCurrent'] = striplist(hxs.select('//dd[@class="summary-current"]/ul[@class="current"]/li/text()').extract())
			item['overviewPast'] = striplist(hxs.select('//dd[@class="summary-past"]/ul[@class="past"]/li/text()').extract())
			item['overviewEducation'] = striplist(hxs.select('//dd[@class="summary-education"]/ul/li/text()').extract())
			
			yield item
		else: #if it is a directory
			for url in hxs.select('//ul[@class="directory"]/li/a/@href').extract(): #take all of the subdirectories that show up and request them
				if sampling:
					if random.random() < 0.1: 										#since we are taking a sample, we'll randomly keep a few directories and profiles, and throw out the rest.
						yield Request('http://www.linkedin.com'+url, callback=self.parse)
				else :
					yield Request('http://www.linkedin.com'+url, callback=self.parse)
				
				
				
