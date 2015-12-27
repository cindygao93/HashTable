#!/usr/bin/python
# -*- coding: utf-8 -*-
## lowercase ASCII: goes from 97-122

## aka h'(k) = key = (ord(word[0])-97)*80 + (ord(word[1])-97)*3.7

## h(k) = h'(k) + i

import math

def genHash():
    hashT = [None] * 2347
    return hashT

def H1(key, tableSize):
    hashVal = 0
    for c in key:
        hashVal = 37 * hashVal + ord(c);
    hashVal = hashVal % tableSize
    if hashVal < 0:
        hashVal = hashVal + tableSize
    return int(hashVal)

def H2(key, tableSize):
    hashVal = ord(key[0]) << 7
    for c in key:
        hashVal = eval(hex((long(1000003) * hashVal) & 0xFFFFFFFFL)[:-1]) ^ ord(c)
    hashVal = hashVal ^ len(key)
    hashVal = hashVal % tableSize
    if hashVal < 0:
        hashVal = hashVal + tableSize
    return int(hashVal)

def hashList():
    aList = []
    file = open('secret.txt', 'r')
    for line in file:
        aList.append(line.strip())
    return aList


def InsertLin(key, hashT):
    hashV = 17 * ((ord(key[0]) - 97) * 80 + (ord(key[1]) - 97) * 3.7) \
        % len(hashT)

##    if HashT[hashV] == None:
##        HashT[hashV] = key
##        else:

    col = 0
    hashLen = len(hashT)
    while col < hashLen and hashT[hashV] != None:
        col = col + 1
        hashV = (hashV + col) % hashLen
    if hashT[hashV] == None:
        hashT[hashV] = key
    else:
        print 'Table is full, insert failed'
    return col


## f(col) = col + col**2
## for c1=1, c2=2, smallest hash table size where all
## values inserted was 4300. More than double the number of entries, average comparisons was 43
## for c1=0.5, c2=0.5, table size 4300 yielded comparison of 23

def InsertQuad(key, hashT):
    hashVal = H1(key, len(hashT))
    index = hashVal
    col = 0
    while (col < len(hashT)) and (hashT[index] != None):
        col = col + 1
        index = (hashVal + col + col*col) % len(hashT)
    if (hashT[index] == None):
        hashT[index] = key
        return col
    print 'Table is full, insert failed'
    return col
    
def InsertDouble(key, hashT):
    hashVal = H1(key, len(hashT))
    skip = H2(key, len(hashT))
    index = hashVal
    col = 0
    while (col < len(hashT)) and (hashT[index] != None):
        col = col + 1
        index = (index + skip) % len(hashT)

    if hashT[index] == None:
        hashT[index] = key
        return col
    print 'Table is full, insert failed'
    return col


def main():
    hashT = genHash()
    aList = hashList()
    num = 0
    c = 0
    for i in aList:
        a = InsertDouble(i, hashT)
        num = num + a
        c = c + 1

 # #       print c

##    print hashT
    print 'double hashing function'
    print num
    print num / 2000
    b = 0
    e = 0
    for i in hashT:
        if i == None:
            b = b + 1
        else:
            e = e + 1
    print b
    print e

    hashD = genHash()
    bList = hashList()
    num = 0
    c = 0
    for i in bList:
        a = InsertQuad(i, hashD)
        num = num + a
        c = c + 1

##        print c

    print 'quad probing function'
    print num
    print num / 2000


main()
