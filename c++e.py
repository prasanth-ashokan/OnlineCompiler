import sys,os,getopt
def run(cpp_file,exe_file):
    os.system('g++ ' + cpp_file + ' -o ' + exe_file)
    os.system(exe_file)
def main(argv):
    cpp_file=''
    exe_file=''
    opts,args=getopt.getopt(argv, "i:", ['ifile='])
    for o,a in opts:
        if o in ("-i","--ifile"):
            cpp_file=a+'.cpp'
            exe_file=a+'.exe'
            run(cpp_file,exe_file)

if __name__=='__main__':
    main(sys.argv[1:])
