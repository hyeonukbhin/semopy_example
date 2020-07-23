#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import os
import sys

EXE_PATH = os.getcwd()  # 실행 경로
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))  # 스크립트 경로
UPPER_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 상위 경로
sys.path.append(UPPER_PATH)  # 상위 경로를 추가
from my_tools import first_module  # Upper directory 에서 Lower directory 참조


def function_2():
    print("function_2 of second module imported")


def call_function_in_first_module():
    print("called from second module to first module")
    first_module.function_1()


if __name__ == "__main__":
    function_2()
    call_function_in_first_module()
