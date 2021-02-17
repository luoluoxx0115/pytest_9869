#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File ：test_calc.py
@Auth ： luoluo
@Time ： 2021-02-17 16:23:49
@Description：课程贴：https://ceshiren.com/t/topic/9869 的作业
作业要求：
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
"""

import pytest
import yaml
from pytest_9869.calc import Calculator


# 【读取测试数据】
with open('./datas/calc.yaml') as f:
    datas = yaml.safe_load(f)


# 【测试计算器类】
class TestCalc:

    def setup_class(self):
        print('开始计算')
        self.calc = Calculator()

    def teardown_class(self):
        print('结束计算')

    # 【测试加法】
    @pytest.mark.parametrize(
        'a, b, expect',
        datas['add']['datas'],
        ids=datas['add']['myid']
    )
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    # 【测试除法】
    @pytest.mark.parametrize(
        'a, b, expect',
        datas['div']['datas'],
        ids=datas['div']['myid']
    )
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect
