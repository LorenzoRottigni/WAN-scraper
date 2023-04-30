import scrapy

class WanScraperSpider(scrapy.Spider):
    name = "wan_scraper"
    #start_urls = [
    #    "https://www.google.com",
    #]

    def start_requests(self):
        # Here you can generate a dynamic list of URLs to crawl
        urls = ['https://www.deesup.com/', 'https://www.facebook.com/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Your parsing logic here
        print(str(response.body))
        pass
