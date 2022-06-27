import JobCrawler.crawler
import JobCrawler.db

if __name__=='__main__':
    job_cr = JobCrawler()
    job_cr.start()
    html = job_cr.html
    db = JobCrawler.db.DB()
    db.get_info_in_db()
    db.insert_job(html)
    job_cr.close()