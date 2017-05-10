#!/usr/bin/env python
# -*- coding: utf-8 -*-
# copyRight by heibanke

# 闭包closure
# 1. 嵌套函数
# 2. 内部函数使用外部变量(通常是外部函数的参数)
# 3. 外部函数返回内部函数

# closure
def pow_x(x):
    def echo(value):
        # x=2
        print value
        return value ** x

    return echo


if __name__ == '__main__':
    p = pow_x(2)
    print p(3)

