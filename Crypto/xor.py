#!/usr/bin/python

from base64 import b64decode
import sys


def decyph(msg, key):
    ckey = key
    for i in range(len(msg) - len(key)):
        ckey = ckey + key[i % len(key)]
    decypher = ""
    for i in range(len(msg)):
        decypher = decypher + chr(ord(msg[i]) ^ ord(ckey[i]))
    return decypher


def usage():
    print "Usage: xor [opt] [message] [key]"
    print "Missing or wrong arguments."
    print "[opt]"
    print "-d    Base64 decode message."


def main(argv):
    if len(argv) == 3:
        msg = argv[1]
        key = argv[2]
        print decyph(msg, key)
    elif len(argv) == 4:
        if argv[1] != "-d":
            print argv[1]+" not an argument."
            usage()
            return 1
        try:
            msg = b64decode(argv[2])
        except Exception as e:
            print("Base64 not well formed %s", e)
            return 1
        key = argv[2]
        print decyph(msg, key)
    else:
        usage()
        return 0


if __name__ == "__main__":
    main(sys.argv)
