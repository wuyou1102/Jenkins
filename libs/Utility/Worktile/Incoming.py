# -*- encoding:UTF-8 -*-

import Common
import Message
import traceback
from libs import Environment

__incoming_url = 'https://hook.worktile.com/incoming/24eeed87286b43aea84ce87e4374e66e'
build_info = Environment.environ


def get_traceback():
    tmp = traceback.format_exc()
    if tmp != 'None\n':
        return tmp
    return ""


def job_started(users=[], text=""):
    data = Message.job_started(build_info=build_info, text=text, users=users)
    return Common.POST(__incoming_url, data=Common.JSON_DUMPS(data))


def job_finished(users=[], text=""):
    data = Message.job_finished(build_info=build_info, text=text, users=users)
    return Common.POST(__incoming_url, data=Common.JSON_DUMPS(data))


def job_error(users=[], text=""):
    data = Message.job_error(build_info=build_info, text=text, users=users)
    return Common.POST(__incoming_url, data=Common.JSON_DUMPS(data))


def job_exception(users=[]):
    return job_error(users=users, text=get_traceback())
