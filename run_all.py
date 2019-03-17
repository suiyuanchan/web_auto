from common.HTMLTestRunner_cn import HTMLTestRunner
import unittest
import os

# 获取当前的绝对路径
curr = os.path.realpath(__name__)
# 获取当前目录
di = os.path.dirname(curr)
print(dir)

# 获取case路径
case = os.path.join(di, "cases")

# 报告路径是否存在,不存在就创建
report = os.path.join(di, "report")
a = os.path.exists(report)
if not a:
    os.mkdir(report)
# 报告文件
repx = os.path.join(report, '', 'result.html')

# 装载测试用例
al = unittest.defaultTestLoader.discover(case, pattern="test*.py")

# 运行测试用例
fp = open(repx, "wb")
runner = HTMLTestRunner(stream=fp, title="报告标题", description="报告描述")
runner.run(al)

# 只有driver 才会去显示截图
