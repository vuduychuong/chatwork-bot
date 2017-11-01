import requests
from furl import furl

BASE_URL = "https://api.chatwork.com/v2/"
HEADER_TOKEN_CHATWORK = 'X-ChatWorkToken'
API_TOKEN_CHATWORK = '1ab26b4a7f7f07f86e0b23babb42bf85'


def getRequest(url):
    f = furl('%s' % url)
    header = {HEADER_TOKEN_CHATWORK: API_TOKEN_CHATWORK, "Content-Type": "application/json"}
    return requests.get(f.url, headers=header)


def postRequest(url, **kwargs):
    f = furl('%s' % url)
    header = {HEADER_TOKEN_CHATWORK: API_TOKEN_CHATWORK, "Content-Type": "application/json"}
    return requests.post(f.url, headers=header, **kwargs)


def getStatus():
    url = furl('%s' % BASE_URL)
    url.path.add('/my/status')
    return getRequest(url.url)


def getListRoom():
    url = furl('%s' % BASE_URL)
    url.path.add('/rooms')
    return getRequest(url.url)


def addNewMessage(roomId, message):
    url = furl('%s' % BASE_URL)
    url.path.add('/rooms').add(roomId).add('/messages')
    param = {'body': message}
    return postRequest(url.url, params=param)
