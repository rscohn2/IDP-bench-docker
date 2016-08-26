import subprocess

subprocess.check_call('docker login -u $DOCKER_USER -p $DOCKER_PASSWORD',shell=True)
for version in ['pip','apt']:
    repo = 'rscohn2/bench.ubuntu.%s.python' % version
    subprocess.check_call('docker build -t %s -f Dockerfile.%s .' % (repo,version), shell=True)
    subprocess.check_call('docker push %s' % repo,shell=True)
