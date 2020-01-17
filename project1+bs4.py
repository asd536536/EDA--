from selenium import webdriver
import time

def get_replys(url,imp_time=5, delay_time= 0.1):


    #웹드라이버
    driver = webdriver.Chrome('C:/Users/munsu/Desktop/chromedriver_win32/chromedriver.exe')
    driver.implicitly_wait(imp_time)
    driver.get(url)

    #더보기 계속 클릭하기
    while True:
        try:
            더보기 = driver.find_element_by_css_selector('a.u_cbox_btn_more.u_cbox_btn_more')
            더보기.click()
            time.sleep(delay_time)
        except:
            break

    html = driver.page_source
    print(html)

    # 모듈 참조
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')

    #댓글 추출
    contents = soup.select('span.u_cbox_contents')
    contents = [content.text for content in contents]

    # 작성자 추출
    nicks = soup.select('span.u_cbox_nick')
    nicks = [nick.text for nick in nicks]

    # 날짜 추출
    dates = soup.select('span.u_cbox_date')
    dates = [date.text for date in dates]


    # #댓글추츨
    # contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
    # # for content in contents:
    # #     print(content.text)
    # contents = [content.text for content in contents]
    #
    # #작성자
    # # nicks = driver.find_elements_by_css_selector('span.u_cbox_nick')
    # # for nick in nicks:
    # #     print(nick.text)
    # nicks = [nick.text for nick in nicks]
    #
    # #날짜 추출
    # # dates = driver.find_elements_by_css_selector('span.u_cbox_date')
    # # for date in dates:
    # #     print(date.text)
    # dates = [date.text for date in dates]
    #
    # # 취합
    # # print(contents)
    # # print(nicks)
    # # print(dates)
    #
    replys = list(zip(nicks,dates,contents))

    driver.quit()
    return replys

    # for reply in replys
    #     print(reply)

if __name__ == '__main__':
    # url = "https://news.naver.com/main/ranking/read.nhn?m_view=1&includeAllCount=true&mid=etc&sid1=111&rankingType=popular_day&oid=011&aid=0003682090&date=20200117&type=1&rankingSeq=10&rankingSectionId=102"
    url = "https://news.naver.com/main/ranking/read.nhn?m_view=1&includeAllCount=true&mid=etc&sid1=111&rankingType=popular_day&oid=025&aid=0002968527&date=20200117&type=1&rankingSectionId=100&rankingSeq=1"
    reply_data = get_replys(url,5,0.1)

    import pandas as pd #pandas, openpyxl
    col = ['작성자','날짜','내용']
    data_frame = pd.DataFrame(reply_data, columns = col)
    data_frame.to_excel('news.xlsx',sheet_name='해리슨',startrow=0,header=True)








