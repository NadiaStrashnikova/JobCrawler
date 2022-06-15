import requests

# test_url = 'https://www.jobs.bg/front_job_search.php?subm=1&categories%5B%5D=56&domains%5B%5D=3'
# test_url = 'https://www.jobs.bg/?categories%5B0%5D=56'
test_url = 'https://www.jobs.bg/front_job_search.php?subm=1&keywords%5B%5D=python'
test_url = 'dd'

class JobCrawler:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_html(self):
        r = requests.get(self.base_url)

        if r.ok:
            return r.text
        else:
            raise Exception('Something went wrong. Try again.')

    def start(self):
        html = self.get_html()
        self.html = html
        print(html)

if __name__ == '__main__':
    test = JobCrawler(test_url)
    test.start()