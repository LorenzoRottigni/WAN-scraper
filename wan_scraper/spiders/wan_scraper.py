import scrapy
from ..services.dns import DNSService
class WanScraperSpider(scrapy.Spider):
    name = "wan_scraper"
    #start_urls = [
    #    "https://www.google.com",
    #]

    def start_requests(self):
        urls = ['https://www.deesup.com/']
        self.dns = DNSService()
        self.dns.dump()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Your parsing logic here
        # print(str(response.body))
        pass
