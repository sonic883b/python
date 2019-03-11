import json
import requests

url = "XXX"

company_name = "yahoo"+"\n"
title = "Yahoo japan"+"\n"
link_to = "<https://yahoo.co.jp>"
content = company_name + title + link_to

payload_dic = {
  "text":content,
  "username":'webhooks test',
  "icon_emoji":':mailbox_with_mail:',
  "channel":'#chatbot'
}

if __name__ == '__main__':
    r = requests.post(url,data=json.dumps(payload_dic))
