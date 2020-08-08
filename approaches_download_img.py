import requests
import shutil
import urllib.request


def app_requests(img_url, file_name):
    # use stream=True to guarantee no interruptions
    r = requests.get(img_url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            # set decode_content=True, otherwise the size of the
            # downloaded image file will be 0
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


def app_urllib(img_url, file_name):
    # adding information about user-agent
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'my_app')]
    urllib.request.install_opener(opener)
    # calling urlretrieve function to get resource
    urllib.request.urlretrieve(img_url, file_name)


"""
# test
# setting filename a d image url
fn3 = r'C:\Users\Victiny\Python_Project\Covid-19_Visualization\Flag\peru.png'
fn4 = r'C:\Users\Victiny\Python_Project\Covid-19_Visualization\Flag\france.png'
il3 = 'https://cdn.countryflags.com/thumbs/peru/flag-800.png'
il4 = 'https://cdn.countryflags.com/thumbs/france/flag-800.png'

app_requests(il3, fn3)
app_urllib(il4, fn4)

import matplotlib.pyplot as plt
a = plt.imread(fn3)
plt.imshow(a)
plt.show()
"""