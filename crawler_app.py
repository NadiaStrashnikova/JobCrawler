from JobCrawler.crawler import Crawler
import JobCrawler.db as job_db

BASE_URL = 'https://www.jobs.bg/front_job_search.php?subm=1&keywords%5B%5D=python'


if __name__=='__main__':
    job_cr = Crawler(BASE_URL)
    job_cr.start()
    list_job = job_cr.jobs
    print(len(list_job))

    # if it crawls the site from scratch - first clear DB
    db = job_db.DB()
    db.drop_jobadv_table()
    db.create_jobadv_table()

    # db.get_info_in_db()
    db.insert_jobs(list_job)
    job_cr.close()