import scrapy
from ..items import AmazonItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = [
        "https://www.amazon.com/gp/bestsellers/books/283155/ref=s9_acsd_ri_bw_clnk/ref=s9_acsd_ri_bw_c2_x_c2cl?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-10&pf_rd_r=QX5G3S992CY2Z6Q7D46E&pf_rd_t=101&pf_rd_p=d2e01c79-7462-4300-8d41-3633536344dc&pf_rd_i=283155"
    ]

    def parse(self, response):
        item = AmazonItem()
        book_title = response.css('.a-spacing-small').css('img::attr(alt)').getall()
        book_author = response.css('.a-link-child::text').getall()
        book_price = response.css('.p13n-sc-price::text').getall()
        image_link = response.css('.a-spacing-small').css('img::attr(src)').getall()

        item['book_title'] = book_title
        item['book_author'] = book_author
        item['book_price'] = book_price
        item['image_link'] = image_link
        print(len(item['book_title']))
        yield item

        yield from response.follow_all(css='li.a-last a', callback=self.parse)
