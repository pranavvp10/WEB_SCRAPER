#importing Scarpy
import scrapy

# Spider
class StatSpider(scrapy.Spider):
    name = "stats"
    urls=[]
    for i in range(0,961,60):
        url='https://sofifa.com/?r=200019&set=true&offset={i}'.format(i=i)
        urls.append(url)
    start_urls=urls

# Parse Function
    def parse(self, response):

        rows=response.xpath('//*[@id="adjust"]/div/div[1]/table/tbody/tr')
        for row in rows:
           names=row.xpath('//td[2]/a[1]//text()').extract()
           ages=row.xpath('//td[3]//text()').extract()
           overall=row.xpath('//td[4]//text()').extract()
           teams = row.xpath('//td[6]/div/a//text()').extract()
           values=row.xpath('//td[7]//text()').extract()
           wages = row.xpath('//td[8]//text()').extract()
        for name,age,ovr,team,value,wage in zip(names,ages,overall,teams,values,wages):
            yield {
                'name':name,
                'age':age,
                'ovr':ovr,
                'team':team,
                'value':value,
                'wage':wage
            }

