import subprocess

def build(ext, push=True):
    repo = 'rscohn2/bench.ubuntu.%s' % ext
    subprocess.check_call('docker build -t %s -f Dockerfile.%s .' % (repo,ext), shell=True)
    if push:
        subprocess.check_call('docker push %s' % repo,shell=True)


subprocess.check_call('docker login -u $DOCKER_USER -p $DOCKER_PASSWORD',shell=True)
build('base', False)
build('pip')
build('apt.openblas')
build('apt.reference')
build('apt.atlas')
