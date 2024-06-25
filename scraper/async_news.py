# from parsel import Selector
# import httpx
# import asyncio
#
#
# class AsyncNewsScraper:
#     URL = 'https://www.prnewswire.com/news-releases/news-releases-list/?page={page}&pagesize=25'
#     HEADERS = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "Accept-Encoding": "gzip, deflate, br, zstd",
#         "Accept-Language": "en-US,en;q=0.8",
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0"
#     }
#     TITLE_XPATH = '//div[@class="row newsCards"]/div/a/h3/text()'
#     IMG_XPATH = '//div[@class="img-ratio-element"]/img/@src'
#     DESCRIPTION_XPATH = '//p[@class="remove-outline"]/text()'
#     LINK_XPATH = '//a[@class="newsreleaseconsolidatelink display-outline w-100"]/@href'
#
#     async def fetch_page_call(self, client, page):
#         url = self.URL.format(page=page)
#         response = await client.get(url, timeout=10.0)
#         print(f"page: {response.url}")
#         return Selector(response.text)
#
#     async def scrape_data_call(self, selector):
#         links = selector.xpath(self.LINK_XPATH).getall()
#         print(links)
#
#     async def main(self, limit=300):
#         async with httpx.AsyncClient(headers=self.HEADERS) as client:
#             fetch_page = [self.fetch_page_call(client, page) for page in range(1, limit + 1)]
#             pages = await asyncio.gather(*fetch_page)
#
#             scrape_data = [self.scrape_data_call(selector) for selector in pages if pages is not None]
#             await asyncio.gather(*scrape_data)
#
#
# if __name__ == "__main__":
#     scraper = AsyncNewsScraper()
#     asyncio.run(scraper.main())
