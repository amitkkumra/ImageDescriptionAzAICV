from datetime import time
from pydoc import pager
from telnetlib import EC

from PIL.XVThumbImagePlugin import r
from bs4 import BeautifulSoup
from selenium import webdriver
from parsel import Selector
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# chromedrive_path = 'C://Users//ais//Downloads//chromedriver_win32//chromedriver.exe'
# driver = webdriver.Chrome(chromedrive_path)
#
# url = 'https://www.google.com/search?q=cqs+training&sxsrf=APq-WBv5PoEZT4oVSpgWFztpVRkETzXdwg%3A1643775621944&source=hp&ei=hQb6YZ2zN92J4-EP8auGmAs&iflsig=AHkkrS4AAAAAYfoUlQsdOgU9VdW22zuu5hSvDGky_zpz&gs_ssp=eJzj4tVP1zc0TKnMNcmyqEo3YLRSNagwtjRIMTBJSjU1MjNJNrS0tDKoSDa3tDQ3M020TLJMTk5NTfLiSS4sVigpSszMy8xLBwCTZRRK&oq=cqs&gs_lcp=Cgdnd3Mtd2l6EAMYADILCC4QgAQQxwEQrwEyCwguEIAEEMcBENEDMgsILhCABBDHARCvATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgcIABCABBAKMgcIABCABBAKOggIABCABBCxAzoLCAAQgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBEKMCOhEILhCABBCxAxCDARDHARDRAzoOCC4QgAQQsQMQxwEQ0QM6CAgAELEDEIMBUABY7wJg_x1oAHAAeACAAZ4CiAHZBJIBBTAuMS4ymAEAoAEB&sclient=gws-wiz#lrd=0x390d04be5264c199:0xc799765a9b9cceeb,1,,,'
# driver.get(url)
# page_content = driver.page_source
# response = Selector(page_content)
# print("response is ",response)
# #print("xpath si ",page_content)

# results = []
#
# for el in response.xpath('//div/div[@data-review-id]/div[contains(@class, "content")]'):
#     results.append({
#         'title': el.xpath('.//div[contains(@class, "title")]/span/text()').extract_first(''),
#         'rating': el.xpath('.//span[contains(@aria-label, "stars")]/@aria-label').extract_first('').replace('stars',
#                                                                                                             '').strip(),
#         'body': el.xpath('.//span[contains(@class, "text")]/text()').extract_first(''),
#     })
#
# print(results)
#
#

# options = Options()
# options.add_argument("--lang=en")
# driver = webdriver.Chrome(chrome_options=options)

chromedrive_path = 'C://Users//ais//Downloads//chromedriver_win32//chromedriver.exe'
driver = webdriver.Chrome(chromedrive_path)
url = 'https://www.google.com/search?q=cqs+training&sxsrf=APq-WBv5PoEZT4oVSpgWFztpVRkETzXdwg%3A1643775621944&source=hp&ei=hQb6YZ2zN92J4-EP8auGmAs&iflsig=AHkkrS4AAAAAYfoUlQsdOgU9VdW22zuu5hSvDGky_zpz&gs_ssp=eJzj4tVP1zc0TKnMNcmyqEo3YLRSNagwtjRIMTBJSjU1MjNJNrS0tDKoSDa3tDQ3M020TLJMTk5NTfLiSS4sVigpSszMy8xLBwCTZRRK&oq=cqs&gs_lcp=Cgdnd3Mtd2l6EAMYADILCC4QgAQQxwEQrwEyCwguEIAEEMcBENEDMgsILhCABBDHARCvATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgcIABCABBAKMgcIABCABBAKOggIABCABBCxAzoLCAAQgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBEKMCOhEILhCABBCxAxCDARDHARDRAzoOCC4QgAQQsQMQxwEQ0QM6CAgAELEDEIMBUABY7wJg_x1oAHAAeACAAZ4CiAHZBJIBBTAuMS4ymAEAoAEB&sclient=gws-wiz#lrd=0x390d04be5264c199:0xc799765a9b9cceeb,1,,,'
driver.get(url)

# wait = WebDriverWait(driver, 10)
# menu_bt = wait.until(EC.element_to_be_clickable(
#                        (By.XPATH, '//button[@data-value=\'Sort\']'))
#                    )
# menu_bt.click()
# recent_rating_bt = driver.find_elements_by_xpath(
#                                      '//div[@role=\'menuitem\']')[1]
# recent_rating_bt.click()
# time.sleep(5)

response = BeautifulSoup(driver.page_source, 'html.parser')
rlist = response.find_all('div', class_='section-review-content')

# id_r = r.find('button',
#               class_='section-review-action-menu')['data-review-id']
# username = r.find('div',
#                   class_='section-review-title').find('span').text
try:
    review_text = r.find('span', class_='section-review-text').text
except Exception:
    review_text = None
rating = r.find('span', class_='section-review-stars')['aria-label']
rel_date = r.find('span', class_='section-review-publish-date').text
scrollable_div = driver.find_element_by_css_selector(
 'div.section-layout.section-scrollbox.scrollable-y.scrollable-show'
                     )
driver.execute_script(
               'arguments[0].scrollTop = arguments[0].scrollHeight',
                scrollable_div
               )
