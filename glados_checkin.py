import requests
import json

headers = {
  'authority': 'glados.rocks',
  'accept': 'application/json, text/plain, */*',
  'dnt': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
  'content-type': 'application/json;charset=UTF-8',
  'origin': 'https://glados.rocks',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://glados.rocks/console/checkin',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': ''
}

url = 'https://glados.rocks/api/user/checkin'
serve_base_url = 'https://sc.ftqq.com/'

data = {
    'token': 'glados_network'
}

def glados_check_in(cookie, serve=False, sc_key=''):
    headers['cookie'] = cookie
    response = requests.post(url=url, headers=headers, data=json.dumps(data))
    if 'message' in response.text:
        send_msg = response.json()['message']
        if serve:
            requests.get(serve_base_url + sc_key + '.send?text=' + send_msg)
    else:
        if serve:
            requests.get(serve_base_url + sc_key + '.send?text=' + 'cookie expired')

