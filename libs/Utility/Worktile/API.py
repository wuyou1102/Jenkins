# -*- encoding:UTF-8 -*-
import Common


def get_users():
    resp = Common.GET('https://dev.worktile.com/api/scim/users?startIndex=0&count=200')
    content = resp.content
    content = Common.JSON_LOADS(data=content)
    return content['users']


for user in get_users():
    print user
    # print "\'%s\':(\'%s\',u\'%s\')," % (user['userName'], user['id'], user['displayName'])
