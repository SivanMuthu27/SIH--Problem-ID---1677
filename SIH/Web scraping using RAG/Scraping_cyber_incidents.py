import scrapy
from scrapy.crawler import CrawlerProcess

class CyberIncidentSpider(scrapy.Spider):
    name = "cyber_incident"
    start_urls = ['https://www.cvedetails.com/vulnerability-list.php']

    def parse(self, response):
        for row in response.css('tr.srrowns'):
            yield {
                'cve_id': row.css('td a::text').get(),
                'description': row.css('td::text')[1].get(),
                'publish_date': row.css('td::text')[2].get()
            }

# Run Scrapy in Google Colab
process = CrawlerProcess(settings={
    'FEEDS': {
        'cyber_incidents.json': {'format': 'json'},
    },
})

process.crawl(CyberIncidentSpider)
process.start()
