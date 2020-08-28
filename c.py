print(input)
import os
import sys
import subprocess
fp=open("file.txt","r")
prog=""
for i in fp:
    prog+=i

sys.stdin=open('input.txt','r')
if not os.path.exists('foo'):
    f = open('foo.c', 'w')
    f.write(prog)
    f.close()
    subprocess.call(["gcc", "foo.c", "-ofoo", "-std=c99", '-w', '-Ofast'])
    sys.stdout=open("output.txt",'w')
subprocess.call(["./foo"], stdin = sys.stdin)
