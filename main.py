import requests
from bs4 import BeautifulSoup
import urllib
import urllib2
import requests

alpha = 'abcdefghijklmnopqrstuvwxyz'
url1 = "http://www.tdk.gov.tr/index.php?option=com_yazimkilavuzu&view=yazimkilavuzu&kelime1="
url2 = "&kategori1=yazim_listeli&ayn1=bas&konts="
search = "a"

def getUrl(search, tab):
    return url1 + search + url2 + str(tab*no)

tab = 0
no = 60
total = 0
out = open("Dictionary.txt",'w')
for letter in alpha[:]:
    search = letter
    print "Now the letter ",letter
    for k in range(700):
        print k
        s = getUrl(search, k)
        req = requests.get(s)
        soup = BeautifulSoup(req.text,'html.parser')
        a = soup.find_all('p', {'class':"thomicb"})
        if(len(a) == 0):
            break
        for i in a:
            total+= 1
            out.write(i.text.encode('utf8') + '\n')


print "The total num of word = ", total