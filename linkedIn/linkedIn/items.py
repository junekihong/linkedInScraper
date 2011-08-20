# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class linkedInItem(Item):
    # define the fields for your item here like:

    name = Field()
    headlineTitle = Field()
    location = Field()
    industry = Field()


    overviewCurrent = Field()
    overviewPast = Field()
    overviewEducation = Field()
    #recommendations = Field()
    #connections = Field()
    #websites = Field()
