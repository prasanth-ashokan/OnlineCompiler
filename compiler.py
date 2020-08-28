import os
from time import *
import datetime
from flask import *
import sys
import subprocess
def eta(seconds,st):
        sec=seconds-st
        return str(datetime.timedelta(seconds=sec))
def com(data):
    prog =data['code']
    inp=data['input']
    type=data['type']
    
    #type file
    fpt=open('type.txt','w')
    fpt.write(type)
    fpt.close()
    
    #code file
    fpc=open('white_space.txt','w')
    fpc.write(prog)
    fpc.close()
    fh = open("white_space.txt", "r")
    lines = fh.readlines()
    fh.close()
    lines = filter(lambda x: not x.isspace(), lines)
    fh = open("file.txt", "w")
    fh.write("".join(lines))
    fh.close()
    
    #execute_file
    type=data['type']
    if type=="C":
        fpp=open('white_space.txt','w')
        fpp.write(prog)
        fpp.close()
        fh = open("white_space.txt", "r")
        lines = fh.readlines()
        fh.close()
        lines = filter(lambda x: not x.isspace(), lines)
        fh = open("foo.c", "w")
        fh.write("".join(lines))
        fh.close()
    elif type=="C++":
        fpp=open('white_space.txt','w')
        fpp.write(prog)
        fpp.close()
        fh = open("white_space.txt", "r")
        lines = fh.readlines()
        fh.close()
        lines = filter(lambda x: not x.isspace(), lines)
        fh = open("dev.cpp", "w")
        fh.write("".join(lines))
        fh.close()
    elif type=="PYTHON":
        fpp=open('white_space.txt','w')
        fpp.write(prog)
        fpp.close()
        fh = open("white_space.txt", "r")
        lines = fh.readlines()
        fh.close()
        lines = filter(lambda x: not x.isspace(), lines)
        fh = open("sovi.py", "w")
        fh.write("".join(lines))
        fh.close()
    elif type=="JAVA":
        fpp=open('white_space.txt','w')
        fpp.write(prog)
        fpp.close()
        fh = open("white_space.txt", "r")
        lines = fh.readlines()
        fh.close()
        lines = filter(lambda x: not x.isspace(), lines)
        fh = open("Hello.java", "w")
        fh.write("".join(lines))
        fh.close()

    #input file
    fpi=open('input.txt','w')
    fpi.write(inp)
    fpi.close()
    
    
def com_c(data):
    st = time()
    prog=''
    fp=open("file.txt","r")    
    for i in fp:
        prog+=i
    
    cmd="python c.py"
    #subprocess.call(cmd, shell=True)
    re=subprocess.run(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    run_t=(eta(time(),st))
    data['time']=run_t
    er=str(re.stderr)[2:-1]
    if er!="":
        ae="err"
        e=open('output.txt','w')
        for i in er.split("\\r\\n")[1:]:
            #print(i)
            if (r'\t' in i):
                for j in i.split(r"\t"):
                    #print(j)
                    e.write(j+" ")
                e.writelines("\n")
            else:
                e.writelines(i)
                e.writelines("\n")
        e.close()               
    else:
        ae="noerr"
        st=str(re.stdout)
        si=(st.index(">"))
        oc=st[si+1:-1]
        e=open('output.txt','w')
        for i in oc.split("\\r\\n")[1:]:
            #print(i)
            if (r'\t' in i):
                for j in i.split(r"\t"):
                    #print(j)
                    e.write(j+" ")
                e.writelines("\n")
            else:
                e.writelines(i)
                e.writelines("\n")
        e.close()
    data['ae']=ae
    we=open('output.txt','r')
    l=[]
    for i in we.readlines():
        l.append(i)
    return l
def com_cpp(data):
    st = time()
    cmd="python c++e.py -i dev"
    sys.stdin=open('input.txt','r')
    re=subprocess.run(cmd, shell=True,stdin = sys.stdin,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    run_t=(eta(time(),st))
    data['time']=run_t
    er=str(re.stderr)[2:-1]
    if er!="":
        n=1
        ae="err"
        e=open('output.txt','w')
        for i in er.split("\\r\\n")[1:]:
            #print(i)
            if (r'\t' in i):
                for j in i.split(r"\t"):
                    #print(j)
                    e.write(j+" ")
                e.writelines("\n")
            else:
                e.writelines(i)
                e.writelines("\n")
        e.close()
    else:
        n=-1
        ae="noerr"
        st=str(re.stdout)
        si=(st.index("'"))
        oc=st[si+1:-1]
        e=open('output.txt','w')
        for i in oc.split("\\r\\n"):
            if (r'\t' in i):
                for j in i.split(r"\t"):
                    #print(j)
                    e.write(j+" ")
                e.writelines("\n")
            else:
                e.writelines(i)
                e.writelines("\n")
        e.close()
    data['ae']=ae
    we=open("output.txt","r")
    a='\\'
    b=a[-1]
    l=[]
    for i in we.readlines(n):
        ii=i.replace(b,'')
        l.append(ii)
    return (l)


def com_py(data):
    
    st = time()
    cmd="python sovi.py"
    run_t=(eta(time(),st))
    data['time']=run_t
    fh = open("input.txt", "r")
    lines = fh.readlines()
    fh.close()
    # Weed out blank lines with filter
    lines = filter(lambda x: not x.isspace(), lines)
    # Write
    fh = open("inpy.txt", "w")
    fh.write("".join(lines))
    # should also work instead of joining the list:
    # fh.writelines(lines)
    fh.close()
    sys.stdin=open('inpy.txt','r')
    re=subprocess.run(cmd, shell=True,stdin = sys.stdin,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    er=str(re.stderr)[2:-1]
    if er!="":
        ae="err"
        e=open('output.txt','w')
        for i in er.split("\\r\\n"):
            #print(i)
            if (r'\t' in i):
                for j in i.split(r"\t"):
                    #print(j)
                    e.write(j+" ")
                e.writelines("\n")
            else:
                e.writelines(i)
                e.writelines("\n")
        e.close()
    else:
        ae="noerr"
        st=str(re.stdout)
        si=(st.index("'"))
        oc=st[si+1:-1]
        e=open('output.txt','w')
        for i in oc.split("\\r\\n"):
            if (r'\t' in i):
                for j in i.split(r"\t"):
                    #print(j)
                    e.write(j+" ")
                e.writelines("\n")
            else:
                e.writelines(i)
                e.writelines("\n")
        e.close()
    we=open("output.txt","r")
    a='\\'
    b=a[-1]
    l=[]
    for i in we.readlines():
        ii=i.replace(b,'')
        l.append(ii)
    return (l)
def com_java(data):
    st = time()
    sys.stdin=open('input.txt','r')
    cmd="javac Hello.java"
    re=subprocess.run(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    cmd="java Hello"
    re=subprocess.run(cmd, shell=True,stdout=subprocess.PIPE,stdin = sys.stdin,stderr=subprocess.PIPE)
    run_t=(eta(time(),st))
    data['time']=run_t
    er=str(re.stderr)[2:-1]
    l=[]
    if er!="":
        ae="err"
        e=open('output.txt','w')
        for i in er.split("\\r\\n"):
            #print(i)
            if (r'\t' in i):
                for j in i.split(r"\t"):
                    #print(j)
                    e.write(j+" ")
                e.writelines("\n")
            else:
                e.writelines(i)
                e.writelines("\n")
        e.close()
    else:
        ae="noerr"
        st=str(re.stdout)
        si=(st.index("'"))
        oc=st[si+1:-1]
        e=open('output.txt','w')
        for i in oc.split("\\r\\n"):
            if (r'\t' in i):
                for j in i.split(r"\t"):
                    #print(j)
                    e.write(j+" ")
                e.writelines("\n")
            else:
                e.writelines(i)
                e.writelines("\n")
        e.close()
    data['ae']=ae
    we=open("output.txt","r")
    a='\\'
    b=a[-1]
    for i in we.readlines():
        ii=i.replace(b,'')
        l.append(ii)
    return (l)
f = open('file.txt', 'r+')
f.truncate(0)

f = open('foo.c', 'r+')
f.truncate(0)
f = open('input.txt', 'r+')
f.truncate(0)
f = open('output.txt', 'r+')
f.truncate(0)
f = open('dev.cpp', 'r+')
f.truncate(0)
f = open('Hello.java', 'r+')
f.truncate(0)
f = open('type.txt', 'r+')
f.truncate(0)
f = open('white_space.txt', 'r+')
f.truncate(0)
f = open('inpy.txt', 'r+')
f.truncate(0)
f = open('sovi.py', 'r+')
f.truncate(0)
li=[]
ou={'type':'','code':'','input':'','output':'','ae':'','time':''}
data={'type':'','code':'','input':'','output':'','ae':'','time':''}
app=Flask(__name__)
@app.route('/compiler',methods=['GET','POST'])
def fun():
    if request.method=='GET':
        ou.clear()
        data.clear()
        return render_template("page.html",ou=data)
    elif request.method=='POST':
        data['type']=request.form['lan']
        data['code']=request.form['file']
        data['input']=request.form['in']
        com(data)
        #input=request.form['in']
        if data['type']=="C":
            li=com_c(data)
        elif data['type']=="C++":
            li=com_cpp(data)
        elif data['type']=="PYTHON":
            li=com_py(data)
        elif data['type']=='JAVA':
            li=com_java(data)
        else:
            return " CODER ::SELECT THE LANGUAGE!!!!"
        return render_template("page.html",ou=data,lis=li)
if __name__ == '__main__':
    app.run(debug=True,port=3333)
