# _*_coding: UTF-8 _*_
# 开发团队  :
# 开发人员  :   lihc
# 开发时间  :   2019-11-07 09:13
# 文件名称  :   login_page_abs.PY
# 开发工具  :   PyCharm
from pythoncode.calculator import Calculator
import pytest


class Testcalc:
    def setup_class(self):
        self.calc = Calculator()

    def teardown(self):
        pass

    @pytest.mark.parametrize('a,b,c', [
        (1, 1, 2),
        (2, 2, 4)
    ], ids=['test1', 'test2'])
    def test_add(self, a, b, c):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == c

    def test_add1(self):
        # calc = Calculator()
        result = self.calc.add(1, 1)
        assert result == 2

    def test_add2(self):
        # calc = Calculator()
        result = self.calc.add(1, 1)
        assert result == 2

    def test_add3(self):
        # calc = Calculator()
        result = self.calc.add(1, 1)
        assert result == 2


if __name__ == '__main__':
    pytest.main()
