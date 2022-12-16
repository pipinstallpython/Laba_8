#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    A = tuple(map(int, input().split()))
    for item in range(len(A)-2, 1, -1):
        if A[item-1] < A[item] and A[item] > A[item+1]:
            print(A[:item - 1])
            break
