#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import os
import sys

EXE_PATH = os.getcwd()  # 실행 경로
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))  # 스크립트 경로
UPPER_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 상위 경로
sys.path.append(UPPER_PATH)  # 상위 경로를 추가
from my_tools import second_module  # Upper directory 에서 Lower directory 참조


def function_1():
    print("function_1 of first module imported")


def call_function_in_second_module():
    print("called from first module to second module")
    second_module.function_2()


if __name__ == "__main__":
    function_1()
    call_function_in_second_module()
