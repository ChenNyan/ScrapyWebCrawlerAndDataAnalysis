import scrapy, re, time

class NextSpiderSpider(scrapy.Spider):
    name = "tiebaSpider"
    start_urls = ['https://tieba.baidu.com/p/6062186860?pn=1']

    def parse(self, response):
        # 这句的目的为提取每一层楼的内容
        floor = response.css('div.d_post_content')
        # 创建空列表，用来存储有效投票
        ticket = []
        for v in floor:
            text = v.css('.d_post_content::text').extract_first()
            # 这个正则为提取出有效票数，并过滤掉和投票无关的楼层
            Effective = re.search("^.*投.*号候选人$", text)
            # 和投票无关的楼层会输出None，所以要过滤掉
            if Effective is None:
                pass
            else:
                # 这个正则为提取出投的具体是哪位候选人，并将候选人添加进列表
                Result = re.search('\d*号候选人', Effective.group())
                ticket.append(Result.group())

        # 接下来进行写文件操作
        fileName = 'tieba.txt'
        with open(fileName, 'a+', encoding='utf-8') as f:
            f.write(str(ticket))
            f.write("\n")
            f.close()

        # Xpath选择器提取下一页链接
        next_page = response.xpath('//li[@class="l_pager pager_theme_5 pb_list_pager"]//a[last()-1]//@href').extract_first()
        if next_page is not None:
            time.sleep(1)
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)