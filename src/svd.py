#!/usr/bin/env python
#title           :svd.py
#description     :Singular Value Decomposition
#author          :Johan Astborg, joastbg@gmail.com
#date            :2015-06-01
#version         :0.1
#usage           :python svd.py
#notes           :NUMA22
#python_version  :2.7.9
#==============================================================================

class Reflection:
    """A simple example class"""
    i = 0
    def __init__(self, ii):
        self.i = ii

class Householder:
    j = 0
    def __init__(self, jj):
        self.j = jj

class Givens:
    k = 0
    def __init__(self, kk):
        self.k = kk

class SVD:
    l = 0
    def __init__(self, ll):
        self.l = ll

def main():
        x = Reflection(3.14)
        print x.i
        y = Householder(3.15)
        print y.j
        z = Givens(3.16)
        print z.k
        w = SVD(3.17)
        print w.l
        # r = Reflection(v)
        # a = array([...])
        # result = r * a
	print "Singular Value Decomposition"

if __name__ == "__main__":
    main()
