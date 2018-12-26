# -*- encoding:UTF-8 -*-

import Common
import Message

__incoming_url = 'https://hook.worktile.com/incoming/24eeed87286b43aea84ce87e4374e66e'


def job_started(users, build_info, text):
    return Common.POST(__incoming_url, data=Message.job_started(build_info=build_info, text=text, users=users))


def job_finished(users, build_info, text):
    return Common.POST(__incoming_url, data=Message.job_finished(build_info=build_info, text=text, users=users))


def job_error(users, build_info, text):
    return Common.POST(__incoming_url, data=Message.job_error(build_info=build_info, text=text, users=users))
