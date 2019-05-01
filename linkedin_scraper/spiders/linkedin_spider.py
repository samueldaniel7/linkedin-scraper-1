import scrapy


class LinkedinSpider(scrapy.Spider):
    name = "linkedin"
    login_page = 'https://www.linkedin.com/uas/login'

    def start_requests(self):
        urls = [
            'https://www.linkedin.com/uas/login?',
        ]
        for url in urls:
            self.log(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def init_request(self):
        #"""This function is called before crawling starts."""
        self.log("inside init request");
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        #"""Generate a login request."""
        self.log("inside login");
        return FormRequest.from_response(response,
                    formdata={'session_key': 'user@email.com', 'session_password': 'somepassword'},
                    callback=self.check_login_response)

    def parse(self, response):
        self.log(response)
