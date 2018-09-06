__repo = 'repo'


def init(url, branch):
    cmd = '{repo} init -u {url} -b {branch}'.format(repo=__repo, url=url, branch=branch)
    print cmd
    return cmd


def sync(cores=8):
    cmd = '{repo} sync -j{cores}'.format(repo=__repo, cores=cores)
    return cmd
