from connect import *
from bs4 import BeautifulSoup
from dbconnect import *
from parsing import *
gu_part = ["은평구"]
for gu_list in gu_part:
    print(gu_list)

    for page_num in range(1, 11):
        initpage(gu_list, page_num)
        p = Parsing()
        collect = p.getHotLink()

        for i in collect:

            info = p.parsingHot(i)
            try:
                a = driver.find_element_by_css_selector(
                    "li.review_fliter_item:nth-child(4) > .review_fliter_item_btn").get_attribute("data-review_count")
                if int(a) != 0:
                    driver.find_elements_by_css_selector(
                        'li.review_fliter_item')[3].click()
                    time.sleep(0.2)
                    if int(a) > 5:
                        while(1):
                            try:
                                driver.find_element_by_xpath(
                                    "//button[@class='btn-reivews-more']").click()
                                time.sleep(0.2)
                            except ElementNotVisibleException:
                                break
                            except WebDriverException:
                                break

                    b = [p.text.replace('\n', ' ').strip(
                    ) for p in driver.find_elements_by_css_selector("span.review_content")]

                    for j in b[:-1]:
                        info['리뷰'] = j
                        insertDB(info)

            except:
                continue