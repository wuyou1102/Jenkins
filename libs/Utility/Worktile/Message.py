# -*- encoding:UTF-8 -*-
import Config
from libs.Utility import TimeFormat


def at_users(users):
    tmp = [u'[@cd84cf5364134bd686cdda3a54cb4305|吴忧]']
    for user in users:
        if user in Config.users.keys():
            item = Config.users[user]
            tmp.append("[@%s|%s]" % (item[0], item[1]))
    return ''.join(tmp)


def at_users_filed(users):
    return {
        "title": u"提醒关注",
        "value": at_users(users),
        "short": 0
    }


def url_filed(url):
    return {
        "title": u"Link",
        "value": '[{url}|点击查看详情]'.format(url=url),
        "short": 1
    }


def trigger_user_filed(user):
    if user in Config.users.keys():
        item = Config.users[user]
        user = "[@%s|%s]" % (item[0], item[1])
    return {
        "title": u"触发者：",
        "value": user,
        "short": 1
    }


def trigger_time_filed(time):
    return {
        "title": u"触发时间：",
        "value": TimeFormat.get_timestamp(t=time),
        "short": 1
    }


def finished_time_filed():
    return {
        "title": u"完成时间：",
        "value": TimeFormat.get_timestamp(),
        "short": 1
    }


def base(title, text, color, fields):
    print fields
    msg = {
        "attachment": {
            "fallback": "Jenkins",
            "color": color,
            "title": title,
            "text": text,
            "fields": fields,
        }
    }
    return msg


job_name = "job_name"
BUILD_TIMESTAMP = "BUILD_TIMESTAMP"
trigger = "trigger"
number = "number"


def job_started(users, build_info, text):
    title = "Jenkins:%s - Started" % build_info[job_name]
    fields = [
        trigger_user_filed(build_info[trigger]), trigger_time_filed(build_info[BUILD_TIMESTAMP]),
        at_users_filed(users=users),
        url_filed(url="http://jenkins.sensethink.cn/job/%s/%s/" % (build_info[job_name], build_info[number]))
    ]
    return base(title=title, text=text, color="#1E90FF", fields=fields)


def job_finished(users, build_info, text):
    title = "Jenkins:%s - Finished" % build_info[job_name]
    fields = [
        trigger_user_filed(build_info[trigger]), finished_time_filed(),
        at_users_filed(users=users),
        url_filed(url="http://jenkins.sensethink.cn/job/%s/%s/" % (build_info[job_name], build_info[number]))
    ]
    return base(title=title, text=text, color="#00FF7F", fields=fields)


def job_error(users, build_info, text):
    title = "Jenkins:%s - Error" % build_info[job_name]
    fields = [
        at_users_filed(users=users),
        url_filed(url="http://jenkins.sensethink.cn/job/%s/%s/" % (build_info[job_name], build_info[number]))
    ]
    return base(title=title, text=text, color="#FF0000", fields=fields)
