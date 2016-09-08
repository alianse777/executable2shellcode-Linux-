import subprocess as sp
import sys
import shlex

if len(sys.argv) < 3:
    print ("Usage: %s binfile outputfile")
    sys.exit(-1)

#This command converts files to shellcodes
p = sp.check_output(shlex.split("objdump -D %s |grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\\\x/g'|paste -d '' -s" % sys.argv[1]))

try:
    fl = open(sys.argv[2])
    fl.write(p)
    fl.close()
except:
    print ("Cannot write shellcode to file!")
