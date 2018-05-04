import scrapy
from scrapy_01_text_project.scrapy_01_text_project.items import Scrapy01TextProjectItem as DemoItems

class DemoSpider(scrapy.Spider):
    name = 'demo'  #scrapy crawl <name> 选取哪个爬虫
    allowed_domains = ['###']
    start_urls = ['http://www.sina.com','http://www.sohu.com']

    def parse(self,response):
        items = []
        sel = scrapy.Selector()
        sites = sel.xpath('//ul[@class=""]/li')
        for site in sites:
            item  = DemoItems()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
            items.append(item)
        return items

        #filename = response.url.split("/")[-2]
        #with open(filename,'wb') as f:
            #f.write(response.body)

