# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class linkedInItem(Item):
    # define the fields for your item here like:
    
    url = Field()
    name = Field()
    headlineTitle = Field()
    location = Field()
    industry = Field()
    overviewCurrent = Field()
    overviewPast = Field()
    overviewEducation = Field()
    #recommendations = Field()
    connections = Field()
    #websites = Field()
    
    descriptionSummary = Field()
    summarySpecialties = Field()
        
    experienceHeads = Field()
    expCompany = Field()
    expTimeStarts = Field()
    expTimeEnds	= Field()
    #expDescriptions = Field()
    expTimeDurations = Field()

    educationSchoolName1 = Field()
    educationMajor1 = Field()
    educationDegree1 = Field()
    eduTimeStart1 = Field()
    eduTimeEnd1 = Field()
    
    educationSchoolName2 = Field()
    educationMajor2 = Field()
    educationDegree2 = Field()
    eduTimeStart2 = Field()
    eduTimeEnd2 = Field()
    
    educationSchoolName3 = Field()
    educationMajor3 = Field()
    educationDegree3 = Field()
    eduTimeStart3 = Field()
    eduTimeEnd3 = Field()
    
    #descriptionEducation = Field()    
    #additionalInterests = Field()
    #additionalGroups = Field()
    #additionalAwards = Field()
    #contactFor = Field()
    
