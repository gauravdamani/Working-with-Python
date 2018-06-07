from lxml import html
import requests
import time

class AppCrawler:
	def __init__(self,starting_url,depth):
		self.starting_url=starting_url
		self.depth=depth
		self.current_depth=0
		self.depth_links=[]
		self.apps=[]
	def crawl(self):#crawling the web . Difficult but easy to understand
		app=self.get_app_from_link(self.starting_url)
		self.apps.append(app)
		self.depth_links.append(app.links)
		while self.current_depth<self.depth:
			current_links=[]
			for link in self.depth_links[self.current_depth]:
				current_app=self.get_app_from_link(link)
				current_links.extend(current_app.links)
				self.apps.append(current_app)
				time.sleep(5)#if we send requests to a particular http repeatedly ,our ip would be blocked.
			self.current_depth+=1
			self.depth_links.append(current_links)

	def get_app_from_link(self,link):#scraping data from an app(extracting data)
		start_page=requests.get(link)
		tree=html.fromstring(start_page.text)
		name=tree.xpath('//h1[@class="product-header__title product-header__title--app-header"]/text()')[0]#gives Cndy crush Saga :)
		developer=tree.xpath('//a[@class="link"]/text()')[0]#name of developer of candy crush
		price=tree.xpath('//li[@class="inline-list__item inline-list__item--bulleted"]/text()')[0]
		links=tree.xpath('//div[@class="l-row l-row--peek"]/a[@class="we-lockup targeted-link l-column small-2 medium-3 large-2 ember-view"]/@href')
		name=name.lstrip()
		name=name.rstrip()
		developer=developer.lstrip()
		app=App(name,developer,price,links)
		return app
class App:
	def __init__(self,name,developer,price,links):
		self.name=name
		self.developer=developer
		self.price=price
		self.links=links
	def __str__(self):
		return("Name: {} \nDeveloper:{} \nPrice:{}".format(self.name,self.developer,self.price)) 
crawler=AppCrawler('https://itunes.apple.com/us/app/candy-crush-saga/id553834731?mt=8',2)#number of times we want to gain data from subsequent pages
crawler.crawl()

for app in crawler.apps:
	print(app)
