import os
import sys
import subprocess
cmd="python c++.py -i dev"
sys.stdin=open('input.txt','r')
re=subprocess.run(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print(re.stdout)
print(re.stderr)