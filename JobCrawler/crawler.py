import time

from os import path as os
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

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

        all_jobs = []
        jobs = self.driver.find_elements(by=By.CSS_SELECTOR, value="div.mdc-card")

        for a_job in jobs:
            dates = a_job.find_element(by=By.CSS_SELECTOR, value="div.card-date")
            titles = a_job.find_element(by=By.CSS_SELECTOR, value="div.card-title")
            title = titles.find_element(by=By.CSS_SELECTOR, value="span:nth-of-type(2)")
            skills = a_job.find_elements(by=By.CSS_SELECTOR, value='div.skill')

            all_skills = ''
            for skill in skills:
                try:
                    img = skill.find_element(By.TAG_NAME, 'img')
                except:
                    print('Not found')

                all_skills += img.get_attribute("alt") + ';'

            clear_date = re.search(r"(^[^\\nbookmark_border]*)", dates.text).group(0)
            one_job = {
                'date': clear_date[0:-1],
                'title': title.text,
                'skills': all_skills
            }

            all_jobs.append(one_job)

        for j in all_jobs:
            print(j)

        # return titles

    def get_html(self):
        self.driver.get(self.base_url)
        #time.sleep(2)  # Let the user actually see something!
        #btnCookies = self.driver.find_element_by_css_selector('button[onclick="closeCookieBar();"]')
        btnCookies = self.driver.find_element(by=By.CLASS_NAME, value='cookie-bar-button')
        btnCookies.click()

        titles_jobs = self.get_title_jobs_nodes()   #on this page

        # print('  scroll next pages  ')
        # time.sleep(2)
        # # Scroll down to bottom
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # print('  search in next pages  ')
        # titles_jobs = self.get_title_jobs_nodes()   #on NEXT page


    def start(self):
        html = self.get_html()
        self.html = html

    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    test = JobCrawler(test_url)
    test.start()
    test.close()