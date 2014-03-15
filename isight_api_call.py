import httplib
import json
import hashlib
import hmac
import urllib
import urlparse

PUB = mine
PRV = mine

def getData(url, path, query, pub, prv):
    hashed = hmac.new(prv, '', hashlib.sha256)
    headers = {'X-Auth' : pub, 'X-Auth-Hash' : hashed.hexdigest()}
    conn = httplib.HTTPSConnection(url)
    conn.request('GET', path + '?' + query, '', headers)
    resp = conn.getresponse()
    jsondata = json.loads(resp.read())
    print jsondata
    return jsondata

def printBasicSearch(data):
    print 'Id: {}'.format(data[u'reportId'])
    print 'Title: {}'.format(data[u'title'])
    print 'ReportLink: {}'.format(data[u'reportLink'])
    print 'WebLink: {}'.format(data[u'webLink'])
    print 'PublishedOn: {}'.format(data[u'publishDate'])


def parseJsonAndPrint(url, path, query, pub, prv):
    data = getData(url, path, query, pub, prv);
    content = data[u'message']
    for report in content:
     print ""
     print ""
     printBasicSearch(report)

myquery = {'md5': '098f6bcd4621d373cade4e832627b4f6', 'format': 'json'}

parseJsonAndPrint("api.isightpartners.com", "/search/basic", urllib.urlencode(myquery), PUB, PRV)
# {u'message': {u'url': u'', u'description': u'The credentials you provided are invalid', u'error': u'unauthorized'}, u'success': False}

