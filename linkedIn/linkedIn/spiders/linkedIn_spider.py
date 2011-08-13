from scrapy.spider import BaseSpider

class linkedInSpider(BaseSpider):
	name = "linkedin.com"
	allowed_domains = ["linkedin.com"]
	start_urls = [
		"http://www.linkedin.com/directory/people/a.html"#,
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
		#filename = response.url.split("/")[-2]
		#open(filename, 'wb').write(response.body)
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//ul/li')
		for site in sites:
			sites2 = site.select('//ul/li').extract()
			#print newSite
			for site2 in sites2:
				sites3 = site2.select('//ul/li').extract()
				print newSite

