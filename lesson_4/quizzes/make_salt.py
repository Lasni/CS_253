import random
import string
import hashlib


def make_salt():
    return "".join(random.choice(string.letters) for x in range(5))

print(make_salt())


def make_pw_hash(name, pw):
    salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return "{},{}".format(h, salt)

print(make_pw_hash("burek", "tralala"))

