import scrapy
from webscrap.items import TableScrapSpider
''' in this spider we will scrap data from table 
    with help  of CSS and XPATH Selector 
    and will use pagination in this spider to get data from multiple pages'''

class TableScrapSpider(scrapy.Spider):
    name = "table_scrap"
    allowed_domains = ["www.scimagomedia.com"]
    start_urls = ["https://www.scimagomedia.com/rankings.php?edition=2024_01&total_size=5452&order=overall&ord=desc&page=1"]


    def parse(self, response):
        items =TableScrapSpider()
        name = response.xpath("//tbody/tr/td[3]//text()").getall()
        domain = response.xpath("//tbody/tr/td[3]//@href").getall()
        priority = response.xpath("//tbody/tr/td[7]//text()").getall()
        for nam,domain,priority in zip(nam,domain,priority):
            items['Name'] =name
            items['Domian'] =domain
            items['Priority'] =priority
            yield items
        
if __name__ == "__main__":
    
