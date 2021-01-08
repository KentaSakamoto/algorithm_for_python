# -*- coding: utf-8 -*-

# 受け取った文字列を逆順に出力する関数
def val_inverse(val):
    n = len(val)
    for i in range(n):
        print(val[n-i-1])
        

val_inverse("abc")

# 再起関数を使った方法
def inverse_ans(val):
    if len(val) != 0:
        print(val[:-1], end="")
        inverse_ans(val[:-1])
    return

inverse_ans("abc")