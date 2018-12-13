# -*- encoding:utf-8 -*-
import module_name

def a():
    module_name.hello()
    print("func a")

def b():
    module_name.hello()
    print("func b")
    

if __name__ == '__main__':
    a()
    b()
