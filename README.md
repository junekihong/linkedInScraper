LinkedIn Scraper
================

Juneki Hong 

juneki@cs.jhu.edu

Updated August 2014
-------------------

Updated this README file and updated this project.
Linkedin seems to have changed its website in the last few years, leaving this project to be outdated and only partially functional. 
This seems like it will be a recurring problem. 
However, for now I have updated the project to properly scrape the data that it used to years ago. I also cleaned up the code a bit.



Originally written/uploaded August 2011
---------------------------------------

This is a project that will go through and scrape public profile information off of linkedin. 
This is information that anyone can find and see from linkedIn's directory such as:
http://www.linkedin.com/directory/people/a.html

I used Scrapy, which is an open-source online library in python that helps you scrape websites.
http://scrapy.org/


INSTRUCTIONS
------------

-In order to run this scraper, you need to go and install scrapy. 
-Once you do, all you need to do is jump into your terminal or command line and navigate to ~/linkedInScraper/linkedIn/
-Now type in: "scrapy crawl linkedin.com"
    -I have the CSV formatted data being outputted to standard out. If you would like data in a nice CSV format you should redirect this output
    -You can run the command "scrapy crawl linkedin.com > items.txt"


SUMMARY OF FILES
----------------

-items.py is the "item" object being scraped. Here we specify what exactly we are trying to scrape for. If we want only some names, we can specify the item to have a "name" element. When we scrape linkedIn, we'll only scrape items (containing only names) and return them for us to save.
-pipelines.py defines how exactly we unpackage the item objects after we scrape them. Once we extract the "name" out of an item, for example, we can decide how we are going to store it or display it in whatever format (in this case, the information was needed in a .txt or in an excel format)
-linkedIn_spider.py is the spider. It goes through and requests webpages (you can imagine that it goes and automatically "clicks on" each webpage to open it up). Once it opens up a page, it will go through and store all the information we want in an "item" object and then returns the item (which was specified in items.py).
      -If you look near the top of linkedIn_spider.py, where the spider is being initialized, you will see a big list of URLs. Those are the URLs I wanted the spider to start with, and as it explores linkedIn it will add new URLs that it discovers to this list. 
      -Linkedin is nice enough to have this phonebook-like directory structure so we can go through it looking for profiles to scrape, or more directory pages to explore. If you have a specific list of URLs you want to scrape, you could put that into the spider's starting URL list.
-settings.py is the settings file. Scrapy does a lot of very convenient things by default, but sometimes I wanted it to specifically do something else (for example, searching through the LinkedIn directory of people in a Breadth-First Order strategy instead of the default Depth-First Order). All that stuff is specified here.
-items.txt is the output file that is created by the project when you run it. It contains all of the delicious data that you want!


NOTES
-----

-The data was to be stored in an excel document.
-Because I wanted to keep each person to 1 line, I had to make a compromise:
	-Instead of taking every single work experience (title, dates, descriptions) possible, I took the top 5 (if they existed). 
	-I arranged them in seperate columns across a single row.
	-I did the same with education

-This scraper samples a small number of profiles off of LinkedIn. If you would like for the scraper to exhaustively scrape every single profile, just go to linkedIn_spider.py and set the variable randomSampling at the top to false.
-Similarly, if you want to increase the size of the sample of profiles scraped off of LinkedIn, you can increase the scaping probability by going to linkedIn_spider.py and setting the variable samplingProbability to a higher value.

-Finally, the scraper was originally designed to scrape only for US profiles. This is now set to false by default, but if you would like this turned on as well, you need to go to linkedIn_spider.py and set the variable filterForUS to true.

