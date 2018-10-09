#!/usr/bin/env python
# coding: utf-8

import nfc
import time
import pygame.mixer
import os


#初期設定
pygame.mixer.init()
count = 0
loop = 0

#財宝を判定する
def connected(tag):
    global count
    global loop
    print str(count+1) + "回目"
    judge = str(tag.identifier).encode('hex').upper()

    #本物の財宝の場合
    if judge == '0451B3F2295881':
        if judge != loop:
            print "正解"
            pygame.mixer.music.load("/home/pi/sound/Sounds/Answer.mp3")
            pygame.mixer.music.play(1)
            time.sleep(3)
            pygame.mixer.music.stop()
            loop = judge
        print "本物の財宝が乗っています"
        count += 1
        time.sleep(1)

    #偽物の財宝の場合
    else:
        if judge != loop:
            print "不正解"
            pygame.mixer.music.load("/home/pi/sound/Sounds/Buzzer.mp3")
            pygame.mixer.music.play(1)
            time.sleep(3)
            pygame.mixer.music.stop()
            loop = judge
        print "偽物の財宝が乗っています"
        count += 1
        time.sleep(1)

#プロセスID表示
print "プロセスID：" + str(os.getpid())

#財宝を感知した時
while True:
    clf = nfc.ContactlessFrontend('usb')
    clf.connect(rdwr={'on-connect': connected})
    clf = ""

print "ゲームオーバー"