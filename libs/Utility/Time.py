import time
from libs import Environment as Env


def get_timestamp(time_fmt='%Y_%m_%d-%H_%M_%S', t=None):
    t = t if t else time.time()
    return time.strftime(time_fmt, time.localtime(t))


def convert_timestamp(str, time_fmt='%Y_%m_%d-%H_%M_%S'):
    return time.mktime(time.strptime(str, time_fmt))


def get_job_time():
    start_time = Env.BUILD_TIMESTAMP
    t = convert_timestamp(str=start_time, time_fmt="%Y%m%d.%H%M%S")
    return t
    t = t - 24 * 3 * 3600
    return get_timestamp(time_fmt="%Y-%m-%d %H:%M", t=t)


if __name__ == '__main__':
    print get_job_start_time()
