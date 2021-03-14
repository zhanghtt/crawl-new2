from scrapy_redis.spiders import RedisSpider


import scrapy
import re

class BaiduSpider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']
    allcnt_pattern = re.compile(r'"CommentCount": \"(\d+)\",')

    def parse(self, response):
        #print(self.allcnt_pattern.findall(response.text))
        # 通过导入CookieJar来实现cookie的获取
        from scrapy.http.cookies import CookieJar
        cookie_jar = CookieJar()
        cookie_jar.extract_cookies(response, response.request)
        print(response.request.headers)
        print(cookie_jar)  # <scrapy.http.cookies.CookieJar object at 0x7f8888a0f940>
        cookie_dict = dict()
        for k, v in cookie_jar._cookies.items():
            for i, j in v.items():
                for m, n in j.items():
                    cookie_dict[m] = n.value
        print("cookie_dict>>>", cookie_dict)
        yield scrapy.Request(url='https://wq.jd.com/commodity/comment/getcommentlist?callback=fetchJSON_comment98&pagesize=10&sceneval=2&skucomment=1&score=0&sku=65959006654&sorttype=6&page=1',dont_filter=True,headers={
               'Connection': 'keep-alive',
               "Referer": "https://item.m.jd.com/72321801855.html",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
               "cookie":"shshshfpa=230b299e-b267-3f39-748a-5274ba04573e-1526388430; shshshfpb=0e4a63e00c3146f1205679ecef0af468fb452b7038a3edfd15afad6d12; __jdu=1595213903005116662704; pin=jd_49e6f74229a5c; unick=jd_188014ctk; _tp=f8skMf7S6k8VPMVjjhCn8S7vk6UqsuFMW8o68xx3ddc%3D; _pst=jd_49e6f74229a5c; ipLocation=%u5317%u4eac; pinId=CL2LG1jQi0fBGlwodztkXrV9-x-f3wj7; unpl=V2_ZzNtbRAFShd8AUZWfk0IB2JTRwgSBxBBfAtGUHseXFFkCxINclRCFnQURldnG1wUZwQZWUNcRhJFCEdkeB5fA2AFEFlBZxBFLV0CFi9JH1c%2bbRpdS1BKFnQLRlZLKV8FVwMTbUJTSxF2CERcehtdBGMDElpFUEATdA12ZHwpbDVjCxVUQVdzFEUJdhYvRVsNbwAaWw9XRx1xC0ZWcxheBGYHEl1FUEQWcwlDZHopXw%3d%3d; __jdv=76161171|direct|-|none|-|1609750532540; TrackID=14z86bRECmD_c8hnyUzWqPbiv0pHgxgGJ0tgMH9b8UmBPkuTndrN5VhNCH5t8h3LTmlYuJbzhHXbftdRKDtXKBnPgOEXXzqhXAH9ZY-6s5MAR2ncnCvnEbToPqbFrYgEt; user-key=43a6e8ea-993d-49e9-8763-4e756d81ae6f; cn=0; PCSYCityID=CN_110000_110100_110105; areaId=1; ipLoc-djd=1-72-55653-0; wxa_level=1; jxsid=16109508048628837173; webp=1; visitkey=31014972499970792; __jda=122270672.1595213903005116662704.1595213903.1610948455.1610955353.123; __jdc=122270672; 3AB9D23F7A4B3C9B=HV7XTTHFGASMIJRSRKK34KLHMYELLS47K4NBCIR2PEFYCZUMIX225JHQCMEJUTEKYFDA47E3QEMFC3TYKKQRYXFS2Q; shshshfp=8e6807b1ccf37dd2a527f63ee133d3e6; shshshsID=48908f8b4d08dd6a4ad6ea045c548f30_2_1610955836722; wq_logid=1610955927.1063071573; retina=1; cid=9; wqmnx1=MDEyNjM4NHMubXQxMzQyL25yOzVNQUszTEdoLjFsaTFzZjQyRUgmUg%3D%3D; __jdb=122270672.12.1595213903005116662704|123.1610955353; mba_muid=1595213903005116662704; mba_sid=16109559266537842608963232693.1"
           })