import os
import scrapy


class Qoute_scrap(scrapy.Spider):
    name = "quote_scrap"
    # start_urls = ["https://quotes.toscrape.com/"]
    def start_requests(self):
        urls = ["https://quotes.toscrape.com/"]
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)
    

    def parse(self,response):
        page_title = response.xpath("//title/text()").get()  ## to get the head title
    
        quotes = response.xpath("//div[@class='quote']")
        # print(quotes)
        for quote in quotes:
            text = quote.xpath(".//span[@class='text']/text()").get()
            author = quote.xpath(".//small[@class='author']/text()").get()
            tag = quote.xpath(".//a[@class='tag']/text()").getall()
            print(text, author,tag, end='\n')
        try:
            file = os.path.exists("reponse.text")
            print(file)
            with open('reponse.text','a') as text:  # i used open() method  in append mode to  open a file in append mode #
                writer = text.writelines([text,author,tag])           # than write text of response in file #
        except Exception as e:
            print(str(e))
              
