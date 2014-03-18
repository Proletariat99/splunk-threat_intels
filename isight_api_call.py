import httplib
import json
import hashlib
import hmac
import urllib
import urlparse


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
    return content
    #for report in content:
    #    print ""
    #    print ""
    #    printBasicSearch(report)

#myquery = {'md5': '098f6bcd4621d373cade4e832627b4f6', 'format': 'json'}
#ioc_query = {'format': 'json'}
#basic_query = {}
#adv_query = {}


#report_index_query = {'format': 'json'} # downloads using default time
#report_get_query = {'format': 'json'}
#basic_query = {'format':'json', 'Protocol':'http'}
basic_query = {'format':'json', 'ips':'93.170.130.109'}
#basic_query = {'format':'json', 'description':'93.170.130.109'}
advanced_query = {'format':'json','networkIdentifier': 'Attacker'}
warn_query = {'format':'json'}
ioc_query = {'format':'json'}
rep_ix_query = {'format':'json'}
rep_query = {'format':'json'}

intels_basic = parseJsonAndPrint("api.isightpartners.com", "/search/basic", urllib.urlencode(basic_query), PUB, PRV)
intels_adv = parseJsonAndPrint("api.isightpartners.com", "/search/advanced", urllib.urlencode(advanced_query), PUB, PRV)
intels_warn = parseJsonAndPrint("api.isightpartners.com", "/view/indicators", urllib.urlencode(warn_query), PUB, PRV)
intels_ioc = parseJsonAndPrint("api.isightpartners.com", "/view/iocs", urllib.urlencode(ioc_query), PUB, PRV)
intels_ix = parseJsonAndPrint("api.isightpartners.com", "/report/index", urllib.urlencode(rep_ix_query), PUB, PRV)
intels_rep = parseJsonAndPrint("api.isightpartners.com", "/report/14-30106", urllib.urlencode(rep_query), PUB, PRV)

 #{u'message': {u'url': u'', u'description': u'The credentials you provided are invalid', u'error': u'unauthorized'}, u'success': False}

types_basic_search = [x[u'productType'] for x in intels_basic]
types_warn = [x[u'productType'] for x in intels_warn]
types_ioc = [x[u'productType'] for x in intels_ioc]
