import urlparse
import urllib2
import os
import sys
from bs4 import BeautifulSoup
import requests
import shutil

# url = raw_input("[+] Enter the URL: ")
url = "https://www.artic.edu/collection?is_public_domain=1"
download_path = raw_input("[+] Enter the full download path: ")

try:
    # headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    i = 0

    # request = urllib2.Request(url, None, headers)
    r = requests.get(url, verify=False)
    # html = urllib2.urlopen(request)
    soup = BeautifulSoup(r.text, features="html.parser")
    for tag in soup.findAll('img'):
        try:
            if tag.attrs['data-srcset']:
                image_urls = tag.attrs['data-srcset']
                image_url = image_urls.split()[0]
                # tag.attrs['data-srcset'] = urlparse.urljoin(url, tag['srcset'])
                if os.path.splitext(os.path.basename(image_url))[1] == '.jpg':
                    current = requests.get(image_url, verify=False, stream=True)
                    print "\n[*] Downloading: %s" % (os.path.basename(image_url))
                    # f = open(download_path + 'default' + str(i) + '.jpg', 'wb')
                    with open(download_path + 'default' + str(i) + '.jpg', 'wb') as f:
                        current.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)    
                    f.close
                    i += 1
        except Exception as e:
            print e
            continue

    print "\n[*] Downloaded %d files" %(i+1)
    raw_input("[+] Press any key to exit...")

except KeyboardInterrupt:
    print "[*] Exiting"

except SyntaxError:
    print "[*] Fix your code stupid"
    sys.exit(1)

except Exception as e:
    print "[*] Could not get information from server %s" % e
    sys.exit(2)
