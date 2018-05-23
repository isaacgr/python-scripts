import urlparse
import urllib2
import os
import sys
from bs4 import BeautifulSoup


url = raw_input("[+] Enter the URL: ")
download_path = raw_input("[+] Enter the full download path: ")

try:
    headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}

    i = 0

    request = urllib2.Request(url, None, headers)
    html = urllib2.urlopen(request)
    soup = BeautifulSoup(html.read(), "lxml")
    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        if os.path.splitext(os.path.basename(tag['href']))[1] == '.pdf':
            current = urllib2.urlopen(tag['href'])
            print "\n[*] Downloading: %s" % (os.path.basename(tag['href']))
            f = open(download_path + os.path.basename(tag['href']), 'wb')
            f.write(current.read())
            f.close
            i += 1

    print "\n[*] Downloaded %d files" %(i+1)
    raw_input("[+] Press any key to exit...")

except KeyboardInterrupt:
    print "[*] Exiting"

except SyntaxError:
    print "[*] Fix your code stupid"
    sys.exit(1)

except:
    print "[*] Could not get information from server"
    sys.exit(2)
