from lxml import html
import requests

class AppCrawler:
	def __init__(self,starting_url,depth):
		self.starting_url=starting_url
		self.depth=depth
		self.apps=[]
	def crawl(self):
		self.get_app_from_link(self.starting_url)
		return
	def get_app_from_link(self,link):
		start_page=requests.get(link)
		tree=html.fromstring(start_page.text)
		name=tree.xpath('//h1[@class="product-header__title product-header__title--app-header"]/text()')[0]#gives Cndy crush Saga :)
		developer=tree.xpath('//a[@class="link"]/text()')[0]#name of developer of candy crush
		price=tree.xpath('//li[@class="inline-list__item inline-list__item--bulleted"]/text()')[0]
		links=tree.xpath('//div[@class="l-row l-row--peek"]/a[@class="we-lockup targeted-link l-column small-2 medium-3 large-2 ember-view"]/@href')
		name=name.lstrip()
		name=name.rstrip()
		developer=developer.lstrip()
		for link in links:
			print(link)
		app=App(name,developer,price,links)
		self.apps.append(app)
class App:
	def __init__(self,name,developer,price,links):
		self.name=name
		self.developer=developer
		self.price=price
		self.links=links
	def __str__(self):
		return("Name: {} \nDeveloper:{} \nPrice:{}".format(self.name,self.developer,self.price)) 
crawler=AppCrawler('https://itunes.apple.com/us/app/candy-crush-saga/id553834731?mt=8',0)
crawler.crawl()

for app in crawler.apps:
	print(app)
