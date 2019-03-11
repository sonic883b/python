# -*- coding: utf-8 -*-
import github
import sys
import os

## arg check
argvs = sys.argv
argc = len(argvs)
print(argvs)
print(argc)

if ( argc <= 2 ):
    print("arg is small")
    quit()

# os.environ でAPI TOKEN 取得
GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN','')
gh = github.GitHub( access_token = GITHUB_ACCESS_TOKEN )
# API TOLKEn入力後にusername情報取得
getuser = gh.user.get()
USER = getuser[ 'name' ]

#pulls =  gh.repos( ).sonic883b( )( 'terraform' ).pulls( ).get( )
#sha   = pulls[ 0 ][ 'head' ][ 'sha' ]
#gh.repos('sonic883b')('terraform').issues.post(title='sample issue', body='found a bug')
#pulls = gh.repos('sonic883b')('terraform').pulls.get
#print(pulls)
## make pull test
#gh.repos('sonic883b')('terraform').pulls.post(title='apitest from githubpy', body='test ya nenn.', head='sonic883b:prmaketest', base='master')
#issues = gh.repos( ).sonic883b()('terraform').issues( ).get()
#print(issues)
#print("issues: " + issues[ 0 ][ 'state' ] )
#print("issues: " + issues[ 0 ][ 'url' ] )

# cmd 毎に実行

cmd1 = sys.argv[1]
cmd2 = sys.argv[2]

if cmd1 == "get":
  if cmd2 == "pull":
    cmd3 = sys.argv[3]
    print(cmd3)
    pulls = gh.repos(USER)(cmd3).pulls( ).get()
    print("pulls: " + pulls[ 0 ][ 'review_comments_url' ] )
  elif cmd2 == "user":
    getuser = gh.user.get()
    sonic883b = gh.users(USER).get()
    print(getuser)
    print(sonic883b)

elif cmd1 == "make":
  if cmd2 == "pull":
    if ( argc <= 7 ):
      print("usage githubpy.py make pulll REPOS TITLE BODY HEAD BASE")
      quit()

    REPOS = sys.argv[3]
    TITLE = sys.argv[4]
    BODY = sys.argv[5]
    HEAD = sys.argv[6]
    BASE = sys.argv[7]
    #mpull = gh.repos('sonic883b')(cmd3).pulls.post(title='apitest from githubpy', body='test ya nenn.', head='sonic883b:prmaketest', base='master')
    mpull = gh.repos(USER)(REPOS).pulls.post(title=TITLE, body=BODY, head=HEAD, base=BASE)
    print(mpull)



#gh.repos( ).sonic883b( )( 'terraform' ).statuses( )( sha ).post(
#    state       = sys.argv[ 1 ],
#    target_url  = "https://twitter.com/sonic883b",
#    description = "test",
#    context     = 'test from githubpy'
#)
