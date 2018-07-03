from scrapy.spiders import CrawlSpider

from scrapy.selector import Selector

from jianshu.items import JianshuItem


class JianshuSpider(CrawlSpider):
    name = "jianshu"
    start_urls = ['https://www.jianshu.com/trending/monthly']
    url = 'https://www.jianshu.com'

    def parse(self, response):
       item = JianshuItem()
       selector = Selector(response)
       articles = selector.xpath('//ul[@class="note-list"]/li')

       for article in articles:
           title = article.xpath('div[@class="content"]/a/text()').extract()
           print(title)
           link = article.xpath('a[@class="wrap-img"]/@href').extract()
           author = article.xpath(
               'div[@class="content"]/div/a[@class="nickname"]/text()').extract()
           memo = article.xpath('div[@class="content"]/p/text()').extract()

           item['title'] = title
           item['link'] = link
           item['author'] = author
           item['memo'] = memo

           yield item
