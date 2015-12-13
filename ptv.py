# -*- coding: utf-8 -*-
#論文をボイロに読ませて快適に学習しよう 

#練習
src = "ABC ABC"
dst = src.replace("A", "B")
print dst

#日本語いけるのかな
src2 = "a pen"
dst2 = src2.replace("a", "あ")
print dst2

src3 = "make yourself in a house"
#文法的にまずいのでは
#最初のaを弾きたい
#両脇に半角スペースが入ってるaだけ置換したいわけだが
dst3 = src3.replace(" a "," あ ")
print dst3
#できた
#練習おわり

#ちょっと論文で使う表現とかを洗い出さないといけないな

fi = open("testi.txt","r")
fo = open("testo.txt","w")
#ファイルは用意してね
line = fi.readline()

while line: #この書き方かっこいい
    line = line.replace(" a "," あ ")
    print line
    fo.write(line)
    line = fi.readline()

fi.close
fo.close


