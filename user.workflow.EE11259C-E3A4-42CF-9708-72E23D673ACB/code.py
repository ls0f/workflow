#codiong:utf-8

from feedback import Feedback
import base64
import hashlib
import sys

fb = Feedback()
if len(sys.argv) >=2:
    query = sys.argv[1]
else:
    query = "{query}"


def gen_base64(s):
    return base64.b64encode(s)


def gen_sha256(s):
    sh = hashlib.sha256()
    sh.update(s)
    return sh.hexdigest()


def gen_md5(s):
    sh = hashlib.md5()
    sh.update(s)
    return sh.hexdigest()


def gen_sha1(s):
    sh = hashlib.sha1()
    sh.update(s)
    return sh.hexdigest()


def test(s):

    print gen_base64(s)
    print gen_md5(s)
    print gen_sha1(s)
    print gen_sha256(s)

def main():

    b64 = gen_base64(query)
    fb.add_item(title='BASE64', subtitle=b64, arg=b64)

    md5 = gen_md5(query)
    fb.add_item(title='MD5', subtitle=md5, arg=md5)

    sha1 = gen_sha1(query)
    fb.add_item(title="SHA1", subtitle=sha1, arg=sha1)

    sha256 = gen_sha256(query)
    fb.add_item(title="SHA256", subtitle=sha256, arg=sha256)

    print fb

if __name__ == '__main__':
    main()



