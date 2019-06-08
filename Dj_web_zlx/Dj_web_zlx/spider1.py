from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
# 进入爬取页面
def search():
    try:
        url = 'https://news.sina.com.cn/roll/#pageid=153&lid=2509&k=&num=50&page=1'
        browser.get(url)
        wait.until(EC.presence_of_element_located((By.ID, 'pL_Main')))
        getDetail()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#d_list > div > span:nth-child(14) > a')))
        return total.text
    except TimeoutError:
        return search()
# 得到具体信息
def getDetail():
    html = pq(browser.page_source,parser="html")
    content = html.find('#d_list')
    uls = content.find('ul').items()
    for ul in uls:
        lis = ul('li').items()
        for li in lis:
            news = {
                'title': li.find('.c_tit a').text(),
                'href': li.find('.c_tit a').attr('href'),
                'time': li.find('.c_time').text()
            }
            print(news)
# 爬取下一页
def next_detail(page_number):
    try:
        nextBotton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#d_list > div > span:last-child > a')))
        nextBotton.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#d_list > div > span.pagebox_num_nonce'), str(page_number)))
        getDetail()
    except TimeoutException:
        next_detail(page_number)

def main():
    try:
        total = search()
        total = int(total)
        print(total)
        for i in range(2, total + 1):
            next_detail(i)
    except Exception:
        print(Exception)
    finally:
        browser.close()

if __name__ == '__main__':
    main()


