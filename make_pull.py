# -*- coding: utf-8 -*-
import github
import sys
import os

GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN','')
gh = github.GitHub( access_token = GITHUB_ACCESS_TOKEN )

args = sys.argv

print(args)


## make pull test
#gh.repos('sonic883b')('terraform').pulls.post(title='apitest from githubpy', body='test ya nenn.', head='sonic883b:prmaketest', base='master')


issues = gh.repos( ).sonic883b()('terraform').issues( ).get()
pulls = gh.repos( ).sonic883b()('terraform').pulls( ).get()
repos = gh.users('sonic883b' ).repos().get()

#print(issues[0])
#print("issues: " + issues[ 0 ][ 'state' ] )
#print("issues: " + issues[ 0 ][ 'url' ] )

#print(pulls)
#print("pulls: " + pulls[ 0 ][ 'review_comments_url' ] )

print(repos)


print(len(repos))
print(repos[0]['html_url'])
print(repos[1]['html_url'])
print(repos[2]['html_url'])
print(repos[3]['html_url'])
print(repos[4]['html_url'])
print(repos[5]['html_url'])
print(repos[6]['html_url'])
#print("repos: " + pulls[ 0 ][ 'review_comments_url' ] )






#gh.repos( ).sonic883b( )( 'terraform' ).statuses( )( sha ).post(
#    state       = sys.argv[ 1 ],
#    target_url  = "https://twitter.com/sonic883b",
#    description = "test",
#    context     = 'test from githubpy'
#)

