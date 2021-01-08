# -*- coding: utf-8 -*-

my_list = [1, 2, 3]
print(my_list)
# print(*my_list)

# 前者はlistとして値が出力されるが, 後者はリストの要素がそれぞれ出力される

print(*my_list, sep=";")