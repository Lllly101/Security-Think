#! /usr/bin/env python3
"""
guess the token with the related user infomation
token = encrypt(user_info, current_time)
"""

import time
import base64
import hashlib
import argparse

def get_user_info():
    pass

def get_current_time(time_type=0):
    """
    Parameters
        time_type: 0 default second, 1 microsecond
    Return
        <int> t
    """
    t = int(time.time())
    if time_type == 1:
        current_time = t * 1000
    elif time_type == 0:
        current_time = t

    return t

def hash_str(strings, algorithm=0):
    """
    Parameters
        strings: to be hashed
        algorithm: 
            0 --> sha256(default)
            1 --> md5
            2 --> sha512
    Return
        <byte> digest
    """
    strings = strings.encode('utf-8')

    if algorithm == 0:
        m = hashlib.sha256(strings)
    elif algorithm == 1:
        m = hashlib.md5(strings)
    elif algorithm == 2:
        m = hashlib.sha512(strings)

    digest = base64.b64encode(m.digest())

    return digest

def cut(t, length=4):
    """
    Parameters
        t: <str> 
        length: <int> default key parameter
    Return the last chars
    """
    if type(t) != str:
        t = str(t)

    return t[len(t)-length-1:]
    

def combine(strings, method=0):
    """
    Parameters
        strings: <str> strings
        method: <int> 
    """
    t = get_current_time()
    if method == 0:
        result = hash_str(strings + str(t))
        print("[+] {}+{} result: {}".format(strings, t, result))
        result = hash_str(str(t) + strings)
        print("[+] {}+{} result: {}".format(t, strings, result))
    elif method == 1:
        digest = hash_str(strings).decode('utf-8')
        result = digest + str(t)
        print("[+] {}+{} result: {}".format(strings, t, result))
        result = str(t) + digest
        print("[+] {}+{} result: {}".format(t, strings, result))

def help():
    """ 
    Return tuple
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("strings", help="user info")
    parser.add_argument("-m", "--method", choices=[0,1], type=int, help="0 sha256; 1 md5; 2 sha512", default=0)
    args = parser.parse_args()

    method = args.method
    strings = args.strings

    return (method, strings)

if __name__ == "__main__":
    help()
    method, strings = help()
    combine(strings, method)

