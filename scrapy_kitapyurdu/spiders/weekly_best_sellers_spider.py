# Import Scrapy Framework
import scrapy



# Create spider class as a subclass of Spider from Scrapy
class WeeklyBestSellersSpider(scrapy.Spider):

    # Spider name
    name = "weeklybestsellers"

    # Start url
    start_urls = [
        'https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=1&filter_in_stock=1&filter_in_stock=1&page=1']

    # Callback function used by Scrapy to process downloaded responses
    def parse(self, response):

        # Dictionary that keeps book informations, for each book in the page
        for book in response.css('div.product-cr'):
            yield {
                "name": book.css('div.name.ellipsis a span::text').get(),
                "publisher": book.css('div.publisher span a.alt span::text').get(),
                "author": book.css('div.author.compact.ellipsis a.alt::text').get(),
            }

        # Next page link
        next_page = response.css(
            'div.pagination div.links a.next::attr(href)').get()

        # Redirecting to next page
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
