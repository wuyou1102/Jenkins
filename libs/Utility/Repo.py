__repo = 'repo'


def init(url, branch):
    cmd = '{repo} init -u {url} -b {branch}'.format(repo=__repo, url=url, branch=branch)
    print cmd
    return cmd


def sync(thread_num):
    cmd = '{repo} sync -j{thread_num}'.format(repo=__repo, thread_num=thread_num)
    return cmd
