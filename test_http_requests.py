# test_http_requests.py
# -----------------
import requests
import json
class TestClass:
    # base url for test requests, httpbin.org is used as a good playground for http requests
    base_url = 'https://httpbin.org'

    def test_get_notexisting_url(self):
        request_url = f'{self.base_url}/abc'
        response = requests.get(request_url)
        assert response.status_code == 404

    def test_post_notexisting_url(self):
        request_dict = {
            'testing_key': 'testing value'
        }
        request_url = f'{self.base_url}/abc'
        response = requests.post(request_url, json=request_dict)
        assert response.status_code == 404

    def test_get(self):
        # request_url = 'https://httpbin.org/get?argument1=textvalue&argument2=12345'
        arguments = {
            'argument1': 'textvalue',
            'argument2': '12345'
        }
        request_url = '{0}/get?{1}'.format(self.base_url, '&'.join(['{}={}'.format(k, v) for k, v in arguments.items()]))

        response = requests.get(request_url)
        # assert response code
        assert response.status_code == 200
        # convert response body json to python dict
        assert response.headers['Content-Type'] == 'application/json'
        response_json = json.loads(response.content.decode('utf-8'))
        # assert some response body values
        assert response_json['url'] == request_url
        assert response_json['args'] == arguments

    def test_post(self):
        request_url = '{}/post'.format(self.base_url)
        request_dict = {
            'testing_key': 'testing value',
            'testing_int': 12345
        }
        # make http post request
        response = requests.post(request_url, json=request_dict)
        # assert response code
        assert response.status_code == 200
        # convert response body json to python dict
        assert response.headers['Content-Type'] == 'application/json'
        response_json = json.loads(response.content.decode('utf-8'))
        # assert data as string
        assert response_json['data'] == json.dumps(request_dict)
        # assert data as json
        assert response_json['json'] == request_dict

