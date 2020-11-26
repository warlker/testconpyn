# coding=utf-8
from selenium import webdriver
import unittest
import time

# chome_dirver = 'D:\python3\Lib\chromedriver.exe'


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("iTesting")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        search_results = driver.find_element_by_xpath('//*[@id="1"]/h3/a').get_attribute('innerHTML')
        self.assertEqual('iTesting' in search_results, True)

    @unittest.skip('i want to skip')
    def test_baidu_set(self):
        driver = self.driver
        driver.get(self.base_url + "/gaoji/preferences.html")
        m = driver.find_element_by_xpath(".//*[@id='nr']")
        m.find_element_by_xpath("//option[@value='10']").click()

    def test_11(self):
        self.driver.get("https://cn.bing.com/?mkt=zh-CN")
        self.driver.find_element_by_id("id_s")
        self.driver.find_element_by_css_selector( "body")
        self.driver.find_element_by_id("sb_form_q").click()
        self.driver.find_element_by_id("sb_form_q").send_keys("afs")
        self.driver.find_element_by_css_selector( "#sa_5023 > .sa_tm").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
