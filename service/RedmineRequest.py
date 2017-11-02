import requests
from furl import furl

BASE_URL = "https://dev.framgia.com/"
ATOM_KEY = '16e31f4e41ffaa1b29dd8a7f5c11fb21c1dd00c0'
ATOM_EXTENSION = '.atom'


def getRequest(url, **kwargs):
    url = furl('%s%s' % (url, ATOM_EXTENSION))
    url.add({'key': '16e31f4e41ffaa1b29dd8a7f5c11fb21c1dd00c0'})
    return requests.get(url.url, **kwargs)


def postRequest(url, **kwargs):
    header = {'Authorization': 'Basic vu.duy.chuong:Adgjm232', "Content-Type": "application/json"}
    return requests.post(url, headers=header, **kwargs)


def getIssues():
    url = furl('%s' % BASE_URL)
    url.path.add('/issues.json')
    # url.fragment.args = {'assigned_to_id' : 'me'}
    return getRequest(url.url)


def getInfo():
    return getRequest('https://dev.framgia.com/redmine/issues/144811')
