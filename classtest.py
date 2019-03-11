#!/usr/bin/env python3
# -*- coding: UTF-8 -*-1

## 独自クラスを作ってみる
class CLASSTEST:
    def __init__(self,ham,egg):
        self.ham = 10
        self.egg = egg

    def ham(self,egg,bacon):
        print('ham','egg','bacon')

#インスタンス作成
#spam = CLASSTEST(10,egg)
spam = CLASSTEST(10,20)

print(spam.ham,spam.egg) 

obj2 = ham(egg,bacon)
print(obj2)


