from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import csv
import json

EMOJIS = (
    'one',
    'two',
    'three',
    'four',
    'five',
)

@respond_to('疲れた')
def cheer(message):
    message.reply("ファイト")
    message.react("heart")
    message.docs_reply()

@respond_to('天気')
def weather(message):
	import urllib
	import json

	url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
	# '130010'とすると東京の情報を取得してくれる
	# ここを変えれば任意の地域の天気情報を取得できる
	city_id = '130010'

	html = urllib.request.urlopen(url+city_id)
	jsonfile = json.loads(html.read().decode('utf-8'))
	text = jsonfile['description']['text']

	message.send(text)

@respond_to('poll (.*)')
def poll(message, params):
    args = [row for row in csv.reader([params], delimiter=' ')][0]
    if len(args) < 3:
        message.reply('使用方法: poll タイトル 質問 [質問 ...]')
        return

    title = args.pop(0)
    options = []
    for i, o in enumerate(args):
        options.append('* :{}: {}'.format(EMOJIS[i], o))

    # ref https://github.com/lins05/slackbot/issues/43
    send_user = message.channel._client.users[message.body['user']][u'name']
    post = {
        'pretext': '{}さんからアンケートがあります。'.format(send_user),
        'title': title,
        'author_name': send_user,
        'text': '\n'.join(options),
        'color': 'good'
    }

    ret = message._client.webapi.chat.post_message(
        message._body['channel'],
        '',
        username=message._client.login_data['self']['name'],
        as_user=True,
        attachments=[post]
    )
    ts = ret.body['ts']

    for i, _ in enumerate(options):
        message._client.webapi.reactions.add(
            name=EMOJIS[i],
            channel=message._body['channel'],
            timestamp=ts
        )

@listen_to('get (.*) (.*)', re.IGNORECASE)
def getgithub(message, CMD,REPOS):
  # -*- coding: utf-8 -*-
  import github
  import sys
  import os

  # os.environ でAPI TOKEN 取得
  GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN','')
  gh = github.GitHub( access_token = GITHUB_ACCESS_TOKEN )
  # API TOLKEM入力後にusername情報取得
  getuser = gh.user.get()
  USER = getuser[ 'name' ]

  if CMD == "issue":
    issues = gh.repos(USER)(REPOS).issues( ).get()

    print("issues: " + issues[ 0 ][ 'state' ] )
    print("issues: " + issues[ 0 ][ 'url' ] )
    text = issues[0]['url']

  elif CMD == "pull":
    pulls = gh.repos(USER)(REPOS).pulls( ).get()
    print("pulls: " + pulls[ 0 ][ 'review_comments_url' ] )
    for key, value in getuser.items():
      print(key, value)
    text = pulls[ 0 ][ 'review_comments_url' ]
  else:
    text = ("usage:get [issue or pull] [REPOS]")

  message.send(text)

#@listen_to('make (.*) (.*) (.*) (.*) (.*) (.*)', re.IGNORECASE)
#def makegithub(message, CMD,REPOS,TITLE,BODY,HEAD01,BASE):
#  # -*- coding: utf-8 -*-
#  import github
#  import sys
#  import os

#  # os.environ でAPI TOKEN 取得
#  GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN','')
#  gh = github.GitHub( access_token = GITHUB_ACCESS_TOKEN )
#  # API TOLKEM入力後にusername情報取得
#  getuser = gh.user.get()
#  USER = getuser[ 'name' ]

#  if CMD == "pull":
#    HEAD02 = USER+":"+HEAD01
#    print(REPOS,TITLE,BODY,HEAD01,BASE)
#    print(HEAD02)
#    mpull = gh.repos(USER)(REPOS).pulls.post(title=TITLE, body=BODY, head=HEAD02, base=BASE)
#    for key, value in getuser.items():
#      print(key, value)
#    text = "mpull"
#  else:
#    text = "usage:make [pull] REPOS TITLE BODY HEAD BASE\n(e.g.:make pull terraform TESTSLACK TESTSLACKBODY prmaketest master"

#  message.send(text)

@listen_to('make pull (.*)')
def makepull(message, params):
  args = [row for row in csv.reader([params], delimiter=' ')][0]
  print(args)
