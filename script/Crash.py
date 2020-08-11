# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:35:57 2020

@author: Administrator
"""
import threading,time
class A():
    def __init__(self,name,func):
        self.name = name
        self.func = func
        self.thread = threading.Thread(name=self.name,target=self.func)

def sta1():
    for i in range(0,10):
        print('1')
def sta2():
    for i in range(0,10):
        print('2')
a = A('sa',sta1)
b = A("as",sta2)
main=threading.main_thread()
def main():
    a.thread.run()
    b.thread.run()
main.target=main
