#!/usr/bin/python3
for i in range(0, 100):
    if i <= 9:
        i = "0{}".format(i)
    if i == 99:
        print(i)
    else:
        print("{},".format(i), end=" ")
