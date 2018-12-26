# -*- encoding:UTF-8 -*-

import Common
import Message
import traceback

__incoming_url = 'https://hook.worktile.com/incoming/24eeed87286b43aea84ce87e4374e66e'


def get_traceback():
    tmp = traceback.format_exc()
    if tmp != 'None\n':
        return tmp
    return ""


def job_started(build_info, users=[], text=""):
    data = Message.job_started(build_info=build_info, text=text, users=users)
    return Common.POST(__incoming_url, data=Common.JSON_DUMPS(data))


def job_finished(build_info, users=[], text=""):
    data = Message.job_finished(build_info=build_info, text=text, users=users)
    return Common.POST(__incoming_url, data=Common.JSON_DUMPS(data))


def job_error(build_info, users=[], text=""):
    data = Message.job_error(build_info=build_info, text=text, users=users)
    return Common.POST(__incoming_url, data=Common.JSON_DUMPS(data))


def job_exception(build_info, users=[]):
    return job_error(build_info=build_info, users=users, text=get_traceback())
