import pytest
from common.my_shell import MyShell



if __name__ == '__main__':
    shell = MyShell()
    html_report_path = "./report"
    args = ['-s', '-q', '--alluredir', html_report_path]
    pytest.main(args)
    cmd = 'allure serve report'
    print(cmd)
    shell.invoke(cmd)