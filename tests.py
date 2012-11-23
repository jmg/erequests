import unittest
import erequests

http_bin_url = "http://httpbin.org/"

class AsyncRequestsTests(unittest.TestCase):

    urls = [
        'http://httpbin.org',
        'http://httpbin.org/ip',
        'http://httpbin.org/get',        
        'http://httpbin.org/deny',
        'http://httpbin.org/robots.txt',
    ]

    def _tests_status_code(self, method):

        rs = (erequests.get(u) for u in self.urls)
        responses = method(rs)

        for response in responses:
            self.assertTrue(response.status_code, 200)

    def test_map_requests(self):

        self._tests_status_code(erequests.map)

    def test_imap_requests(self):

        self._tests_status_code(erequests.imap)


if __name__ == "__main__":

    unittest.main()