import time

from JobCrawler.read_config import read_config_file
from os import path as os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


# print(f'CWD:{os.getcwd()}')

url = 'https://www.jobs.bg/front_job_search.php?subm=1&keywords%5B%5D=python'

class Crawler():

    def __init__(self, url):
        self.base_url = url

        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    def check_date_conditions(self,nac_date)-> bool:
        today = datetime.today()

        pub_date = nac_date[0:-1]
        if pub_date == 'днес':
            return True
        elif pub_date == 'вчера':
            return True
        else:
            pub_date = datetime.strptime(pub_date, '%d.%m.%y')
        days_diff = relativedelta(today, pub_date)
        if days_diff.days>10:
            return False
        else:
            return True

    def normalize_date(self, org_date):
        pub_date = org_date[0:-1]
        if pub_date == 'днес':
            the_day_date = datetime.today()
            the_day = the_day_date.strftime('%Y-%m-%d')
        elif pub_date == 'вчера':
            the_day_date = datetime.today() + timedelta(days=-1)
            the_day = the_day_date.strftime('%Y-%m-%d')
        else:
            the_day = '20' + pub_date[6] + pub_date[7] + '-' + pub_date[3] + pub_date[4] + '-' + \
                   pub_date[0] + pub_date[1]
        return the_day

    def check_and_insert_job_row(self, date_text, title_text, skills):
        all_text_date = re.search(r"(^[^\\nbookmark_border]*)", date_text).group(0)

        if self.check_date_conditions(all_text_date):
            date_str = self.normalize_date(all_text_date)
            one_job = {
                'date': date_str,
                'title': title_text,
                'skills': skills
            }
            self.all_jobs.append(one_job)

    def gather_skills(self, skills):
        all_skills = ''
        for skill in skills:
            try:
                img = skill.find_element(By.TAG_NAME, 'img')
            except:
                pass
            all_skills += img.get_attribute("alt") + '; '
        return all_skills

    def get_title_jobs_nodes(self):
        self.all_jobs = []

        jobs = self.driver.find_elements(by=By.CSS_SELECTOR, value="div.mdc-card")
        for a_job in jobs:
            dates = a_job.find_element(by=By.CSS_SELECTOR, value="div.card-date")
            titles = a_job.find_element(by=By.CSS_SELECTOR, value="div.card-title")
            title = titles.find_element(by=By.CSS_SELECTOR, value="span:nth-of-type(2)")
            skills = a_job.find_elements(by=By.CSS_SELECTOR, value='div.skill')
            all_skills = self.gather_skills(skills)

            self.check_and_insert_job_row(dates.text, title.text, all_skills)

        for j in self.all_jobs:
            print(j)
        return self.all_jobs

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