# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    book_title = scrapy.Field()
    book_author = scrapy.Field()
    book_price = scrapy.Field()
    image_link = scrapy.Field()