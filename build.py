import os
import subprocess

def get_proxies():
    proxies = ''
    for var in ['http_proxy','https_proxy','no_proxy']:
        if var in os.environ:
            proxies += ' --build-arg %s=%s' % (var,os.environ[var])
    return proxies

def build(ext, push=True):
    repo = 'rscohn2/bench.%s' % ext
    subprocess.check_call('docker build %s -t %s -f Dockerfile.%s .' % (get_proxies(),repo,ext), shell=True)
    if push:
        subprocess.check_call('docker push %s' % repo,shell=True)


subprocess.check_call('docker login -u $DOCKER_USER -p $DOCKER_PASSWORD',shell=True)
build('ubuntu.base', False)
#build('centos.base', False)
for v in ['ubuntu.pip','apt.openblas','apt.reference','apt.atlas']:
    build(v,True)

