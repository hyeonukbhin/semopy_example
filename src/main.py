#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import numpy as np
import os
import json
from my_tools import first_module, second_module

EXE_PATH = os.getcwd()  # 실행 경로
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))  # 스크립트 경로
UPPER_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 상위 경로
CONFIG_PATH = UPPER_PATH + "/config.json"


def main():
    print("Execution Path : {}".format(EXE_PATH))
    print("Script Path : {}".format(SCRIPT_PATH))
    print("Config Path : {}".format(CONFIG_PATH))

    with open(CONFIG_PATH) as json_file:
        json_data = json.load(json_file)

    print("Config Data : {}".format(json_data))

    print("Hello Worlds!")

    first_module.function_1()
    first_module.call_function_in_second_module()
    second_module.function_2()
    second_module.call_function_in_first_module()


if __name__ == "__main__":
    main()
