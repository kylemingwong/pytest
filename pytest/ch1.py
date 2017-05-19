#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: nulige

n1 = raw_input("请输入用户名：")
n2 = raw_input("请输入密码：")
if n1 == 'root' and n2 == 'root@123':
    print "login success!"
else:
    print "login failed!"