import subprocess

#subprocess.check_call('docker login -u $DOCKER_USER -p $DOCKER_PASSWORD',shell=True)
for version in ['14.04','16.04']:
    repo = 'rscohn2/bench.ubuntu%s.python' % version
    subprocess.check_call('docker build -t %s -f Dockerfile.%s .' % (version,version), shell=True)
    #subprocess.check_call('docker push %s' % repo,shell=True)
