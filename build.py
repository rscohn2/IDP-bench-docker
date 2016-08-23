import subprocess

repo = 'rscohn2/bench.ubuntu.python'
subprocess.check_call('docker login -u $DOCKER_USER -p $DOCKER_PASSWORD',shell=True)
subprocess.check_call('docker build -t %s .' % repo, shell=True)
subprocess.check_call('docker push %s' % repo,shell=True)
