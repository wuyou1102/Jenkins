from libs import Environment

__repo = 'repo'


def init(url, branch):
    cmd = '{repo} init -u {url} -b {branch}'.format(repo=__repo, url=url, branch=branch)
    return cmd


def sync(cores=None):
    if cores is None:
        cores = Environment.CORE_QUANTITY
    cmd = '{repo} sync -j{cores}'.format(repo=__repo, cores=cores)
    return cmd


def log(since):
    cmd = '{repo} forall -c git log --since=\"{since}\"'.format(repo=__repo, since=since)
    return cmd


def make_update_api(cores=None):
    if cores is None:
        cores = Environment.CORE_QUANTITY
    cmd = 'make update-api -j{cores}'.format(cores=cores)
    return cmd


def make(cores=None):
    if cores is None:
        cores = Environment.CORE_QUANTITY
    cmd = 'make -j{cores}'.format(cores=cores)
    return cmd
