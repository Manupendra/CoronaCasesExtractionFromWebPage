import scrapy


class QuotesSpider(scrapy.Spider):
    name = "IndiaCoronaCases"
    start_urls = [
        'https://www.mohfw.gov.in/'
    ]

    def parse(self, response):
        for quote in response.css('div.site-stats-count'):
            yield {
                'Active Cases': quote.css('li.bg-blue strong::text').get(),
                'Cured / Discharged': quote.css('li.bg-green strong::text').get(),
                'Deaths': quote.css('li.bg-red strong::text').get()
            }
        for row in response.xpath('//*[@class="table table-striped"]//tbody/tr'):
            yield {
                'Name of State / UT': row.xpath('td[2]//text()').extract_first(),
                'Total Confirmed cases': row.xpath('td[3]//text()').extract_first(),
                'Cured/Discharged': row.xpath('td[4]//text()').extract_first(),
                'Deaths': row.xpath('td[5]//text()').extract_first()
            }