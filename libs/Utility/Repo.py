import os
__repo = 'repo'
CORE_QUANTITY = os.environ['CORE_QUANTITY']



def init(url, branch):
    cmd = '{repo} init -u {url} -b {branch}'.format(repo=__repo, url=url, branch=branch)
    print cmd
    return cmd


def sync(cores=CORE_QUANTITY):
    cmd = '{repo} sync -j{cores}'.format(repo=__repo, cores=cores)
    return cmd
