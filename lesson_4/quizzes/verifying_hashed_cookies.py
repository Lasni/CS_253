import hashlib


def hash_str(s):
    return hashlib.md5(s).hexdigest()


def make_secure_val(s):
    return "%s,%s" % (s, hash_str(s))

# -----------------
# User Instructions
#
# Implement the function check_secure_val, which takes a string of the format
# s,HASH
# and returns s if hash_str(s) == HASH, otherwise None


def check_secure_val(h):
    ###Your code here
    val, hashed_val = h.split(',')
    if hash_str(val) == hashed_val:
        return val
    return None
