import pytest
import os
import shutil
import pytest
import configparser

# config = configparser.ConfigParser()
# config.read('na')

if __name__ == '__main__':
    # 不要加-s参数，allure将stdout输出到allure报告，加了只会输出到console里
    # -v 打印详细日志
    # 用例执行步骤中会有一个stdout附件记录单个用例执行过程中的stdout
    # pytest.main(["--alluredir", "./result", "--clean-alluredir"])
    # shutil.copy("environment.properties", "./result")
    # os.system('allure generate ./result/ -o ./report_allure/ --clean')
    # os.system('allure serve result')

    pytest.main(['-v', '-s', './testcase/testCase.py'])
