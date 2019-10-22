from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import io                                                                       
import urllib3

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'referer': 'https://scrapingclub.com/exercise/basic_captcha/'
}
data = {
    'csrfmiddlewaretoken': '',
    'name': 'scrapingclub',
    'password': 'scrapingclub',
    'captcha_0': '',
    'captcha_1': ''
}

with requests.Session() as s:
    url = "https://scrapingclub.com/exercise/basic_captcha/"
    r = s.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    
    csrf_token = soup.find('input', attrs = {'name': 'csrfmiddlewaretoken'})['value']
    data['csrfmiddlewaretoken'] = csrf_token
    
    captcha_0 = soup.find('input', attrs = {'name': 'captcha_0'})['value']
    data['captcha_0'] = captcha_0
    
    #print(type(soup.find('img', attrs = {'alt': 'captcha'})['src']))
    
    img_url = "https://scrapingclub.com/" + soup.find('img', attrs = {'alt': 'captcha'})['src']
    print(img_url)
    #url_opener = urllib3.PoolManager()
    #.build_opener()                                     
    #url_opener.addheaders.append(('Cookie', 'PHPSESSID=xyz'))  
    img_bytes = s.get(img_url)
    print(img_bytes.content)
    img = Image.open(io.BytesIO(img_bytes.content))                                 
    captcha = pytesseract.image_to_string(img)                              
    print('Captcha solved:', captcha)

    r = s.post(url, data = data, headers = headers) #, headers = r.headers
    print(r)