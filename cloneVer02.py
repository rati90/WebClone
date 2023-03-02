from urllib.parse import urlencode
import requests


output = open("clone.html", 'w')

API_KEY="3f2d711c-5ef9-4ee0-9a10-784aee2512e7"
URL="https://www.classcentral.com/"


def get_scrapeops_url(url):
    payload = {'api_key': API_KEY, 'url': URL, 'bypass': 'cloudflare'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

r = requests.get(get_scrapeops_url('http://example.com/'))


print(r.text, file=output)

# from pywebcopy import save_webpage
# save_webpage(
#       url=URL,
#       project_folder="savedpages//",
#       project_name="my_site",
#       bypass_robots=True,
#       debug=True,
#       open_in_browser=True,
#       delay=None,
#       threaded=False,
# )











