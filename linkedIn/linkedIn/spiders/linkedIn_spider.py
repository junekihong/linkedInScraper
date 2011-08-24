from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from linkedIn.items import linkedInItem

import random

randomSampling = False

def striplist(l):
	return ([x.strip().replace('\t',"") for x in l])				



class linkedInSpider(BaseSpider):
	name = "linkedin.com"
	allowed_domains = ["linkedin.com"]
	start_urls = [
		#"http://www.linkedin.com/pub/rokalight-a-roka-holding-b-v-company/36/530/5b5"
		"http://www.linkedin.com/pub/chandrashekar-a-s/22/677/79a",
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
			if not randomSampling or random.random() < 0.1:
				item = linkedInItem()		
				item['name'] 					= striplist(hxs.select('//h1/span/span/text()').extract())
				item['headlineTitle'] 			= striplist(hxs.select('//p[@class="headline-title title"]/text()').extract())
				item['location'] 				= striplist(hxs.select('//dd/span/text()').extract())
				item['industry'] 				= striplist(hxs.select('//dd[@class="industry"]/text()').extract())		
			
				item['overviewCurrent'] 		= striplist(hxs.select('//dd[@class="summary-current"]/ul[@class="current"]/li/text()').extract())
				item['overviewPast'] 			= striplist(hxs.select('//dd[@class="summary-past"]/ul[@class="past"]/li/text()').extract())
				item['overviewEducation'] 		= striplist(hxs.select('//dd[@class="summary-education"]/ul/li/text()').extract())
			
				#item['recommendations'] 		= striplist(hxs.select('').extract())
				item['connections'] 			= striplist(hxs.select('//dd[@class="overview-connections"]/p/strong/text()').extract())
				#item['websites'] 				= striplist(hxs.select('').extract())
			
				item['descriptionSummary']		= striplist(hxs.select('//p[@class=" description summary"]/text()').extract())
				item['summarySpecialties']		= striplist(hxs.select('//div[@id="profile-specialties"]/p/text()').extract())
			
			
				#------------------------------------------------------------------------------------------------------------------
				# Work Experience: title
				#------------------------------------------------------------------------------------------------------------------
			
				experienceHeads					= striplist(hxs.select('//h3[@class="position-title anet"]/span[@class="title"]/text()').extract())
			
				if not experienceHeads:
					item['experienceHead1']		= []
				else:
					item['experienceHead1']		= experienceHeads.pop(0)
				if not experienceHeads:
					item['experienceHead2']	 	= []
				else:
					item['experienceHead2']		= experienceHeads.pop(0)	
				if not experienceHeads:
					item['experienceHead3']		= []
				else:
					item['experienceHead3']		= experienceHeads.pop(0)
				if not experienceHeads:
					item['experienceHead4']		= []
				else:
					item['experienceHead4']		= experienceHeads.pop(0)
				if not experienceHeads:
					item['experienceHead5']		= []
				else:
					item['experienceHead5']		= experienceHeads.pop(0)
				
				#------------------------------------------------------------------------------------------------------------------
				# Work Experience: Time started
				#------------------------------------------------------------------------------------------------------------------
			
				currentExpTimeStart				= striplist(hxs.select('//div[@class="position  first experience vevent vcard summary-current"]/p/abbr[@class="dtstart"]/text()').extract())
				expTimeStarts					= striplist(hxs.select('//div[@class="position   experience vevent vcard summary-past"]/p/abbr[@class="dtstart"]/text()').extract())
			
				if not currentExpTimeStart:
					if not expTimeStarts:
						item['expTimeStart1']	= []
					else:
						item['expTimeStart1']	= expTimeStarts.pop(0)
				else: 
					item['expTimeStart1']		= currentExpTimeStart.pop(0)
				if not expTimeStarts:
					item['expTimeStart2']		= []
				else:
					item['expTimeStart2']		= expTimeStarts.pop(0)
				if not expTimeStarts:
					item['expTimeStart3']		= []
				else:
					item['expTimeStart3']		= expTimeStarts.pop(0)
				if not expTimeStarts:
					item['expTimeStart4']		= []
				else:
					item['expTimeStart4']		= expTimeStarts.pop(0)
				if not expTimeStarts:
					item['expTimeStart5']		= []
				else:
					item['expTimeStart5']		= expTimeStarts.pop(0)
			
			
				#------------------------------------------------------------------------------------------------------------------
				# Work Experience: Time ended
				#------------------------------------------------------------------------------------------------------------------
			
			
				present							= striplist(hxs.select('//p[@class="period"]/abbr[@class="dtstamp"]/text()').extract())
				expTimeEnds						= striplist(hxs.select('//div[@class="position   experience vevent vcard summary-past"]/p[@class="period"]/abbr[@class="dtend"]/text()').extract())
			
				if not present:
					if not expTimeEnds:
						item['expTimeEnd1']		= []
					else:
						item['expTimeEnd1']		= expTimeEnds.pop(0)
				else:
					item['expTimeEnd1']			= present.pop(0)
			
				if not expTimeEnds:
					item['expTimeEnd2']			= []
				else:
					item['expTimeEnd2']			= expTimeEnds.pop(0)
				if not expTimeEnds:
					item['expTimeEnd3']			= []
				else:
					item['expTimeEnd3']			= expTimeEnds.pop(0)
				if not expTimeEnds:
					item['expTimeEnd4']			= []
				else:
					item['expTimeEnd4']			= expTimeEnds.pop(0)
				if not expTimeEnds:
					item['expTimeEnd5']			= []
				else:
					item['expTimeEnd5']			= expTimeEnds.pop(0)
			
			
			
			
				#------------------------------------------------------------------------------------------------------------------
				# Work Experience: Time duration
				#------------------------------------------------------------------------------------------------------------------
			
				currentDuration					= striplist(hxs.select('//div[@class="position  first experience vevent vcard summary-current"]/p/span[@class="duration"]/text()').extract())
				expTimeDurations				= striplist(hxs.select('//div[@class="position   experience vevent vcard summary-past"]/p/span[@class="duration"]/text()').extract())
			
				if not currentDuration:
					if not expTimeDurations:
						item['expTimeDuration1'] = []
					else:
						item['expTimeDuration1'] = expTimeDurations.pop(0)
				else:
					item['expTimeDuration1']	= currentDuration.pop(0)
				
				if not expTimeDurations:
					item['expTimeDuration2'] 	= []
				else:
					item['expTimeDuration2']	= expTimeDurations.pop(0)
				if not expTimeDurations:
					item['expTimeDuration3'] 	= []
				else:
					item['expTimeDuration3']	= expTimeDurations.pop(0)
				if not expTimeDurations:
					item['expTimeDuration4'] 	= []
				else:
					item['expTimeDuration4']	= expTimeDurations.pop(0)
				if not expTimeDurations:
					item['expTimeDuration5'] 	= []
				else:
					item['expTimeDuration5']	= expTimeDurations.pop(0)	
			
			
				#------------------------------------------------------------------------------------------------------------------
				# Work Experience: Description
				#------------------------------------------------------------------------------------------------------------------
				
				#currentDescription				= striplist(hxs.select('//p[@class=" description current-position"]/text()').extract())
				#expDescriptions					= striplist(hxs.select('//p[@class=" description past-position"]/text()').extract())
			
				#divs = hxs.select('//p[@class=" description past-position"]/text()')
				#for p in divs.select('.//br') :
				#	print p.extract()
			
			
	#			if not currentDescription:
	#				if not expDescriptions:
	#					item['expDescription1']	= []
	#				else:
	#					item['expDescription1']	= expDescriptions.pop(0)
	#			else:
	#				item['expDescription1']		= currentDescription.pop(0)
	#			
	#			if not expDescriptions:
	#				item['expDescription2']		= []
	#			else:
	#				item['expDescription2']		= expDescriptions.pop(0)
	#			if not expDescriptions:
	#				item['expDescription3']		= []
	#			else:
	#				item['expDescription3']		= expDescriptions.pop(0)
	#			if not expDescriptions:
	#				item['expDescription4']		= []
	#			else:
	#				item['expDescription4']		= expDescriptions.pop(0)
	#			if not expDescriptions:
	#				item['expDescription5']		= []
	#			else:
	#				item['expDescription5']		= expDescriptions.pop(0)
	#			#item['expDescription2']			= []
			
				#item['expDescription3']			= []
			
				#item['expDescription4']			= []
			
				#item['expDescription5']			= []
				
				
				
				
				
				
				
				
				
				
				#------------------------------------------------------------------------------------------------------------------
				# Education: School Names
				#------------------------------------------------------------------------------------------------------------------
				
				firstEducationSchool		= striplist(hxs.select('//div[@class="position  first education vevent vcard"]/h3[@class="summary fn org"]/text()').extract())
				schoolNames					= striplist(hxs.select('//div[@class="position  education vevent vcard"]/h3[@class="summary fn org"]/text()').extract())
				if not firstEducationSchool:
					if not schoolNames:
						item['educationSchoolName1']	= []
					else:
						item['educationSchoolName1']	= schoolNames.pop(0)
				else:
					item['educationSchoolName1']		= firstEducationSchool.pop(0)
				if not schoolNames:
					item['educationSchoolName2']		= []
				else:
					item['educationSchoolName2']		= schoolNames.pop(0)
				if not schoolNames:
					item['educationSchoolName3']		= []
				else:
					item['educationSchoolName3']		= schoolNames.pop(0)
				
				
				#------------------------------------------------------------------------------------------------------------------
				# Education: Degrees
				#------------------------------------------------------------------------------------------------------------------
				
				firstDegree 		= striplist(hxs.select('//div[@class="position  first education vevent vcard"]/h4/span[@class="degree"]/text()').extract())
				schoolDegrees		= striplist(hxs.select('//div[@class="position  education vevent vcard"]/h4/span[@class="degree"]/text()').extract())
				
				if not firstDegree:
					if not schoolDegrees:
						item['educationDegree1']		= []
					else:
						item['educationDegree1']		= schoolDegrees.pop(0)
				else:
					item['educationDegree1']			= firstDegree.pop(0)
					
				if not schoolDegrees:
					item['educationDegree2']			= []
				else:
					item['educationDegree2']			= schoolDegrees.pop(0)
				if not schoolDegrees:
					item['educationDegree3']			= []
				else:
					item['educationDegree3']			= schoolDegrees.pop(0)
				
				
				#------------------------------------------------------------------------------------------------------------------
				# Education: Majors
				#------------------------------------------------------------------------------------------------------------------
				
				firstMajor 			= striplist(hxs.select('//div[@class="position  first education vevent vcard"]/h4/span[@class="major"]/text()').extract())
				schoolMajors		= striplist(hxs.select('//div[@class="position  education vevent vcard"]/h4/span[@class="major"]/text()').extract())
				
				if not firstMajor:
					if not schoolMajors:
						item['educationMajor1']		= []
					else:
						item['educationMajor1']		= schoolmajors.pop(0)
				else:
					item['educationMajor1']			= firstMajor.pop(0)
					
				if not schoolMajors:
					item['educationMajor2']			= []
				else:
					item['educationMajor2']			= schoolMajors.pop(0)
				if not schoolMajors:
					item['educationMajor3']			= []
				else:
					item['educationMajor3']			= schoolMajors.pop(0)
				
				
				
				#------------------------------------------------------------------------------------------------------------------
				# Education: Time Start
				#------------------------------------------------------------------------------------------------------------------
				
				firstEducationStart		= striplist(hxs.select('//div[@class="position  first education vevent vcard"]/p[@class="period"]/abbr[@class="dtstart"]/text()').extract())
				educationStarts			= striplist(hxs.select('//div[@class="position  education vevent vcard"]/p[@class="period"]/abbr[@class="dtstart"]/text()').extract())
				print firstEducationStart
				print educationStarts
				
				if not firstEducationStart:
					if not educationStarts:
						item['eduTimeStart1']		= []
					else:
						item['eduTimeStart1']		= educationStarts.pop(0)
				else:
					item['eduTimeStart1']			= firstEducationStart.pop(0)
				
				if not educationStarts:
					item['eduTimeStart2']			= []
				else:
					item['eduTimeStart2']			= educationStarts.pop(0)
				if not educationStarts:
					item['eduTimeStart3']			= []
				else:
					item['eduTimeStart3']			= educationStarts.pop(0)
				
				
				print firstEducationStart
				print educationStarts
				
				
				
				yield item
			
		else : #if it is a directory
			for url in hxs.select('//ul[@class="directory"]/li/a/@href').extract(): #take all of the subdirectories that show up and request them
				if not randomSampling or random.random() < 0.1: 								#random sampling.
					yield Request('http://www.linkedin.com'+url, callback=self.parse)
				
			
			
			
			
			
			
			
			
#			
    		
    		#item['descriptionEducation']
    		
    		#tem['additionalInterests'] 	= striplist(hxs.select('//dd[@class="interests"]/p[@class=""]/text()').extract())
    		
    		#item['additionalGroups']
    		
    		#item['additionalAwards'] 		= striplist(hxs.select('//p[@class=" \'\'"]/text()').extract())
    		
    		#item['contactFor'] 				= striplist(hxs.select('//div[@class="interested"]/ul').extract())
			
		
				
				
				
