#!/usr/bin/env python
# coding: utf-8

import nfc
import time

count = 0

def connected(tag):
    global count
    print str(count+1) + "回目"
    num = str(tag.identifier).encode('hex').upper()
    print num
    count += 1
    time.sleep(1)
while True:
    clf = nfc.ContactlessFrontend('usb')
    clf.connect(rdwr={'on-connect': connected})
    clf = ""
