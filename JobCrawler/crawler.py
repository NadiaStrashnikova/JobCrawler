import time

from os import path as os
from selenium import webdriver
from selenium.webdriver.common.by import By

# test_url = 'https://www.jobs.bg/front_job_search.php?subm=1&categories%5B%5D=56&domains%5B%5D=3'
# test_url = 'https://www.jobs.bg/?categories%5B0%5D=56'
test_url = 'https://www.jobs.bg/front_job_search.php?subm=1&keywords%5B%5D=python'

class JobCrawler:

    def __init__(self, base_url):
        self.base_url = base_url

        #self.driver = webdriver.Chrome('./chromedriver')
        self.driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

        # executable_path = 'C:/ProgramFiles(x86)/Google/Chrome/Application/chromedriver.exe'
        # if os.exists(executable_path):
        #     self.driver = webdriver.Chrome(executable_path)

    def get_title_jobs_nodes(self):
        # dates = self.driver.find_elements(by=By.CSS_SELECTOR, value="div.card-date")
        # titles = self.driver.find_elements(by=By.CSS_SELECTOR, value="div.card-title")

        #one_job = {}
        all_jobs = []
        jobs = self.driver.find_elements(by=By.CSS_SELECTOR, value="div.mdc-card")

        for a_job in jobs:
            dates = a_job.find_element(by=By.CSS_SELECTOR, value="div.card-date")
            titles = a_job.find_element(by=By.CSS_SELECTOR, value="div.card-title")
            # one_job['date'] = dates.text
            # one_job['title'] = titles.text
            one_job = (dates.text,  titles.text)
            all_jobs = all_jobs + [one_job]

        print(all_jobs)

        # for title_node in titles:
        #     title = title_node.find_element(by=By.CSS_SELECTOR, value="span:nth-of-type(2)")
        #     print(title.text)
        #
        # for dates_node in dates:
        #     #date = dates_node.find_element(by=By.CSS_SELECTOR, value="span:nth-of-type(2)")
        #     #print(date.text)
        #     print(dates_node.text)

        #print(titles)
        # return titles

    def get_html(self):
        self.driver.get(self.base_url)
        #time.sleep(2)  # Let the user actually see something!
        #btnCookies = self.driver.find_element_by_css_selector('button[onclick="closeCookieBar();"]')
        btnCookies = self.driver.find_element(by=By.CLASS_NAME, value='cookie-bar-button')
        btnCookies.click()

        titles_jobs = self.get_title_jobs_nodes()


    def start(self):
        html = self.get_html()
        self.html = html
        print(html)

if __name__ == '__main__':
    test = JobCrawler(test_url)
    test.start()