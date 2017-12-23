#!/usr/bin/python

from base64 import b64decode
import sys

def decyph(msg,key):
    ckey=key
    for i in range(len(msg)-len(key)):
        ckey=ckey+key[i%len(key)]
    decypher=""
    for i in range(len(msg)):
        decypher=decypher+chr(ord(msg[i])^ord(ckey[i]))
    return decypher

def usage():
    print "Usage: xor [opt] [message] [key]"
    print "Missing or wrong arguments."
    print "[opt]"
    print "-d    Base64 decode message."
    sys.exit()

if len(sys.argv)==3:
    msg=sys.argv[1]
    key=sys.argv[2]
    print decyph(msg,key)
elif len(sys.argv)==4:
    if sys.argv[1]!="-d":
        print sys.argv[1]+" not an argument."
        usage()
    try:
        msg=b64decode(sys.argv[2])
    except:
        print "Base64 not well formed"
        sys.exit()
    key=sys.argv[2]
    print decyph(msg,key)
else:
    usage()
