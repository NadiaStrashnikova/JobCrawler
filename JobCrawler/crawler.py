import time

from JobCrawler.read_config import read_config_file
from os import path as os
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import datetime
from dateutil.relativedelta import relativedelta

# print(f'CWD:{os.getcwd()}')

url = 'https://www.jobs.bg/front_job_search.php?subm=1&keywords%5B%5D=python'

class Crawler():

    def __init__(self, url):
        self.base_url = url

        app_setting = read_config_file(filename='../config.ini', section='settings')
        executable_path = app_setting['chromedriver_path']
        if os.exists(executable_path):
            self.driver = webdriver.Chrome(executable_path)
        else:
            raise Exception(f'There is no file {executable_path} for Chrome driver.')

    def check_date_conditions(self,nac_date)-> bool:
        today = datetime.date.today()

        pub_date = nac_date[0:-1]
        if pub_date == 'днес':
            return True
        elif pub_date == 'вчера':
            return True
        else:
            pub_date = datetime.datetime.strptime(pub_date, '%d.%m.%y')
        days_diff = relativedelta(today, pub_date)
        if days_diff.days>10:
            return False
        else:
            return True

    def get_title_jobs_nodes(self):
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
                    pass
                all_skills += img.get_attribute("alt") + ';'

            clear_date = re.search(r"(^[^\\nbookmark_border]*)", dates.text).group(0)
            if self.check_date_conditions(clear_date):
                one_job = {
                    'date': clear_date[0:-1],
                    'title': title.text,
                    'skills': all_skills
                }
                all_jobs.append(one_job)

        for j in all_jobs:
            print(j)

        return all_jobs

    def get_html(self):
        self.driver.get(self.base_url)

        btnCookies = self.driver.find_element(by=By.CLASS_NAME, value='cookie-bar-button')
        btnCookies.click()

        titles_jobs = self.get_title_jobs_nodes()   #on this page
        return titles_jobs

        # print('  scroll next pages  ')
        # time.sleep(2)
        # # Scroll down to bottom
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # print('  search in next pages  ')
        # titles_jobs = self.get_title_jobs_nodes()   #on NEXT page


    def start(self):
        self.jobs = self.get_html()

    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    test = Crawler(url)
    test.start()
    test.close()