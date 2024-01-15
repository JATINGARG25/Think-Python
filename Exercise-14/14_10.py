import urllib.request

zipcode = '02492'

ur = 'http://uszip.com/zip/' + zipcode
conn = urllib.request.urlopen(ur)
