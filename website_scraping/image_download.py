import urlparse
import urllib2
import os
import sys
from bs4 import BeautifulSoup
import requests
import shutil

# url = raw_input("[+] Enter the URL: ")
url = "https://www.artic.edu/collection/more?is_public_domain=1"
download_path = raw_input("[+] Enter the full download path: ")
pages = raw_input("[+] Enter the number of pages to fetch: ")
i = 0

for page in range(2, int(pages) + 1):
    try:
        print '[*] Requesting images'
        r = requests.get(url + '&page=%s' % page)
        soup = BeautifulSoup(r.content, 'lxml')
        for tag in soup.find_all('img'):
            try:
                if tag.attrs['data-srcset']:
                    image_url = tag.attrs['data-srcset'].replace('\\', '').replace('"','')
                    if os.path.splitext(os.path.basename(image_url))[1] == '.jpg':
                        current = requests.get(image_url, stream=True)
                        print "\n[*] Downloading: %s" % (os.path.basename(image_url))
                        with open(download_path + str(i) + '.jpg', 'wb') as f:
                            current.raw.decode_content = True
                            shutil.copyfileobj(current.raw, f)    
                            f.close()
                        i += 1
            except:
                print '[*] Could not download image'
                continue

        print "\n[*] Downloaded %d files" %(i+1)

    except KeyboardInterrupt:
        print "[*] Exiting"

    except SyntaxError:
        print "[*] Fix your code stupid"
        sys.exit(1)

    except:
        print "[*] Could not get information from server %s" % e
        continue

raw_input('[+] Press any key to exit')
