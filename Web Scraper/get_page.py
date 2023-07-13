import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')

with open("main.html", 'w') as f:
    for line in html.decode():
        f.write(line)

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find relevant elements (link, script, img)
link_tags = soup.find_all('link')
script_tags = soup.find_all('script')
img_tags = soup.find_all('img')

# Extract URLs or file paths
urls = [link.get('href') for link in link_tags] + [script.get('src') for script in script_tags] + [img.get('src') for img in img_tags]

# Download the files
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split('/')[-1]  # Extract the file name from the URL
        with open(file_name, 'wb') as file:
            file.write(response.content)
            print(f"File downloaded: {file_name}")
    else:
        print(f"Failed to download: {url}")