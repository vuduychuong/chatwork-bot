import requests
from furl import furl

from constant import Constants

BASE_URL = "https://api.chatwork.com/v2/"
API_KEY = '16e31f4e41ffaa1b29dd8a7f5c11fb21c1dd00c0'
HEADER_TOKEN_REDMINE = 'X-Redmine-API-Key'


def getRequest(url):
    f = furl('%s' % url)
    header = {'Authorization': 'Basic vu.duy.chuong:Adgjm232', "Content-Type": "application/json"}
    return requests.get(f.url, headers=header)


def postRequest(url, **kwargs):
    f = furl('%s' % url)
    header = {'Authorization': 'Basic vu.duy.chuong:Adgjm232', "Content-Type": "application/json"}
    return requests.post(f.url, headers=header, **kwargs)

def getIssues():
    url = furl('%s' % BASE_URL)
    url.path.add('/issues.json')
    # url.fragment.args = {'assigned_to_id' : 'me'}
    return getRequest(url.url)