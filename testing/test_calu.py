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
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    def setup(self):
        print('计算开始')

    def teardown(self):
        print('计算结束')

    @pytest.mark.parametrize('a,b,c', [
        (1, 1, 2),
        (200, 200, 400),
        (0.1, 0.1, 0.2)
    ], ids=['xiao', 'da', 'fudianshu'])
    def test_add(self, a, b, c):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == c

    @pytest.mark.parametrize('a,b,c', [
        (1, 1, 0),
        (200, 200, 0),
        (300, 100, 200)
    ], ids=('1-1', '200-200', '300-100'))
    def test_sub(self, a, b, c):
        result = self.calc.sub(a, b)
        assert result == c


if __name__ == '__main__':
    pytest.main()
