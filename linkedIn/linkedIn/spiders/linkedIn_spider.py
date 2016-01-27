from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from linkedIn.items import linkedInItem

import sys
import random
from countries import checkLocation


randomSampling = True
samplingProbability = 0.1

filterForUS = False

def striplist(l):
    l = [x.strip().replace('\t',"") for x in l]
    return [x for x in l if x != u'']

class linkedInSpider(BaseSpider):
    name = "linkedin.com"
    allowed_domains = ["linkedin.com"]
    start_urls = ["http://www.linkedin.com/directory/people-%s" % s
                  for s in "abcdefghijklmnopqrstuvwxyz"]
    
    #start_urls = ["https://www.linkedin.com/directory/people-a-1"]
    #start_urls = ["https://www.linkedin.com/in/aakriti-tambi-b593ba4a","https://www.linkedin.com/in/exobialegal"]
    
    def parse(self, response):
        # If you want to look at the HTML you are parsing, uncomment the next few lines and then look at the file

        """
        f = open("html.txt","w+")
        f.write(response.url)
        f.write("\n\n")
        f.write(response.body)
        f.close()
        """
        
        hxs = HtmlXPathSelector(response)

        #if it is a directory
        if hxs.select('//body[@id="pagekey-seo_people_directory"]'):
            for url in hxs.select('//ul[@class="column dual-column"]/li/a/@href').extract(): #take all of the subdirectories that show up and request them
                url = url.encode('utf-8')
                
                #print url
                if "linkedin.com" not in url:
                    url = "https://www.linkedin.com" + url
                #print url
                
                if randomSampling and random.random() > samplingProbability: #random sampling.
                    continue
                yield Request(url, callback=self.parse)

        
        #if it is not a directory (its a regular page)
        elif hxs.select('//meta[@name="pageImpressionID"]'):

            f = open("html.txt","w+")
            f.write(response.url)
            f.write("\n\n")
            f.write(response.body)
            f.close()

            
            item = linkedInItem()		
            item['url'] = response.url

            #print response.url
            item['headlineTitle'] = striplist(hxs.select('//p[@class="headline title"]/text()').extract())
                
            HTMLtitle = striplist(hxs.select('//title/text()').extract())
            item['name'] = [HTMLtitle[0].split('|')[0].strip()]
            item['location'] = striplist(hxs.select('//dd/span/text()').extract())			
            
            #if not checkLocation(item['location']):
            #print item['location']
            #sys.stdout.flush()
            #else:
            
            if not filterForUS or checkLocation(item['location']):
                item['industry'] = striplist(hxs.select('//dd[@class="descriptor"]/text()').extract())



                item['overviewCurrent'] = striplist(hxs.select('//li/span[@class="org"]/text()').extract())
                item['overviewPast'] = striplist(hxs.select("//td/ol/li/text()").extract())

                # TODO: overviewEducation and overviewPast have the same xpath...
                item['overviewEducation'] = striplist(hxs.select('//td/ol/li/text()').extract())

                
                #item['recommendations'] 		= striplist(hxs.select('').extract())
                item['connections'] = striplist(hxs.select('//div[@class="member-connections"]/strong/text()').extract())
                #item['websites'] 				= striplist(hxs.select('').extract())
		
                item['descriptionSummary'] = striplist(hxs.select('//section/div[@class="description"]/p/text()').extract())


                # TODO: broken from here on down.
                item['summarySpecialties'] = striplist(hxs.select('//div[@id="profile-specialties"]/p/text()').extract())
                
			
                # ------------------------------------------------------------------------------------------------------------------
                # Education
                # ------------------------------------------------------------------------------------------------------------------
                    
                # Education: School Names
                firstEducationSchool = []
                for scope in hxs.select('//div[@class="position  first education vevent vcard"]/h3[@class="summary fn org"]'):
                    names1 = scope.xpath('a/text()').extract()
                    names2 = scope.xpath('text()').extract()
                    firstEducationSchool += names1 + names2
                firstEducationSchool = striplist(firstEducationSchool)
                    
                schoolNames = []
                for scope in hxs.select('//div[@class="position  education vevent vcard"]/h3[@class="summary fn org"]'):
                    names1 = scope.xpath('a/text()').extract()
                    names2 = scope.xpath('text()').extract()
                            
                    schoolNames += names1 + names2
                    """
                    for x in names1:
                    x = x.strip()
                    if x:
                    schoolNames.append(x)
                    for x in names2:
                    x = x.strip()
                    if x:
                    schoolNames.append(x)
                    """
                schoolNames = striplist(schoolNames)
                        
                # Education: Degrees
                firstDegree = striplist(
                    hxs.select('//div[@class="position  first education vevent vcard"]/h4/span[@class="degree"]/text()').extract())
                schoolDegrees = striplist(
                    hxs.select('//div[@class="position  education vevent vcard"]/h4/span[@class="degree"]/text()').extract())
                            
                # Education: Majors
                firstMajor = striplist(
                    hxs.select('//div[@class="position  first education vevent vcard"]/h4/span[@class="major"]/text()').extract())
                schoolMajors = striplist(
                    hxs.select('//div[@class="position  education vevent vcard"]/h4/span[@class="major"]/text()').extract())
                            
                # Education: Time Start
                firstEducationStart = striplist(
                    hxs.select('//div[@class="position  first education vevent vcard"]/p[@class="period"]/abbr[@class="dtstart"]/text()').extract())
                educationStarts	= striplist(
                    hxs.select('//div[@class="position  education vevent vcard"]/p[@class="period"]/abbr[@class="dtstart"]/text()').extract())
			
                # Education: Time End
                firstEducationEnd = striplist(
                    hxs.select('//div[@class="position  first education vevent vcard"]/p[@class="period"]/abbr[@class="dtend"]/text()').extract())
                educationEnds = striplist(
                    hxs.select('//div[@class="position  education vevent vcard"]/p[@class="period"]/abbr[@class="dtend"]/text()').extract())
                                        
                item['educationSchoolName1'] = []
                item['educationDegree1'] = []
                item['educationMajor1']	= []
                item['eduTimeStart1'] = []
                item['eduTimeEnd1'] = []
                
                if firstEducationSchool:
                    item['educationSchoolName1'] = firstEducationSchool.pop(0)

                    if firstDegree:
                        item['educationDegree1'] = firstDegree.pop(0)

                    if firstMajor:
                        item['educationMajor1'] = firstMajor.pop(0)

                    if firstEducationStart:
                        item['eduTimeStart1'] = firstEducationStart.pop(0)

                    if firstEducationEnd:
                        item['eduTimeEnd1'] = firstEducationEnd.pop(0)

                elif schoolNames:
                    item['educationSchoolName1'] = schoolNames.pop(0)

                    if schoolDegrees:
                        item['educationDegree1'] = schoolDegrees.pop(0)
                            
                    if schoolMajors:
                        item['educationMajor1']	= schoolMajors.pop(0)

                    if educationStarts:
                        item['eduTimeStart1'] = educationStarts.pop(0)
						
                    if educationEnds:
                        item['eduTimeEnd1'] = educationEnds.pop(0)

                if not schoolNames:
                    item['educationSchoolName2'] = []
                else:
                    item['educationSchoolName2'] = schoolNames.pop(0)
                if not schoolNames:
                    item['educationSchoolName3'] = []
                else:
                    item['educationSchoolName3'] = schoolNames.pop(0)
			
                if not schoolDegrees:
                    item['educationDegree2'] = []
                else:
                    item['educationDegree2'] = schoolDegrees.pop(0)
                if not schoolDegrees:
                    item['educationDegree3'] = []
                else:
                    item['educationDegree3'] = schoolDegrees.pop(0)
			
                if not schoolMajors:
                    item['educationMajor2']	= []
                else:
                    item['educationMajor2'] = schoolMajors.pop(0)
                if not schoolMajors:
                    item['educationMajor3']	= []
                else:
                    item['educationMajor3']	= schoolMajors.pop(0)
						
                if not educationStarts:
                    item['eduTimeStart2']			= []
                else:
                    item['eduTimeStart2']			= educationStarts.pop(0)
                if not educationStarts:
                    item['eduTimeStart3']			= []
                else:
                    item['eduTimeStart3']			= educationStarts.pop(0)
			
                if not educationEnds:
                    item['eduTimeEnd2']			= []
                else:
                    item['eduTimeEnd2']			= educationEnds.pop(0)
                if not educationEnds:
                    item['eduTimeEnd3']			= []
                else:
                    item['eduTimeEnd3']			= educationEnds.pop(0)
			
                #------------------------------------------------------------------------------------------------------------------
                # Work Experience
                #------------------------------------------------------------------------------------------------------------------

                # Work Experience: Title
                experienceHeads	= striplist(
                    hxs.select('//h3/span[@class="title"]/text()').extract())
                item['experienceHeads'] = experienceHeads
                            
                # Work Experience: Company
                experienceCompany = []
                for scope in hxs.select('//h4/strong'):
                    #print "current scope:", scope 
                    companies1 = scope.xpath('span[@class="org summary"]/text()').extract()
                    companies2 = scope.xpath('a/span[@class="org summary"]/text()').extract()
                    experienceCompany += companies1 + companies2
                    experienceCompany = striplist(experienceCompany)
                item['expCompany'] = experienceCompany
                    
                    
                # Work Experience: Time started
                expTimeStarts = striplist(
                    hxs.select('//div[contains(@class, "experience")]/p/abbr[@class="dtstart"]/text()').extract())
                item['expTimeStarts'] = expTimeStarts
					
                            
                # Work Experience: Time ended
                timePresent = striplist(
                    hxs.select('//div[contains(@class, "experience")]/p/abbr[@class="dtstamp"]/text()').extract())
                expTimeEnds = striplist(
                    hxs.select('//div[contains(@class, "experience")]/p/abbr[@class="dtend"]/text()').extract())
                expTimeEnds = timePresent + expTimeEnds
                item['expTimeEnds'] = expTimeEnds			
                
                # Work Experience: Time duration
                expTimeDurations = striplist(
                    hxs.select('//div[contains(@class, "experience")]/p/span[@class="duration"]/text()').extract())
                item['expTimeDurations'] = expTimeDurations
		
                # Work Experience: Description
                #expDescriptions = striplist(
                #hxs.select('//p[@class=" description past-position"]/text()').extract())
                yield item
		
        			
			

