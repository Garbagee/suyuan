
import sys
import os
curPath = os.path.abspath(os.path.dirname(r'D:\pycharm\产品溯源系统测试\runn\runcase.py'))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import HTMLTestRunner
import time



def run():
	reportpath = "../report"
	test_dir = '../testcase'
	suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_*.py')
	now = time.strftime('%Y-%m-%d_%H_%M_%S')
	reportname = reportpath + '\\' + 'TestResult' + now + '.html'
	with open(reportname, 'wb') as f:
		runner = HTMLTestRunner.HTMLTestRunner(
			stream=f,
			title='测试报告',
			verbosity = 2,
			tester = "李锦龙",
			description='Test the import testcase'
		)
		runner.run(suite)
	time.sleep(1)



if __name__ == '__main__':

	run()
