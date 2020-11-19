'''
项目名称:产品溯源系统
所属模块:防伪码管理unittest
日期:2020/11/08
作者:李锦龙
版本:version:1.0
'''
import time
import unittest
from ddt import ddt,data,unpack
from data.testdata import getdata
from public.common import loginTo
from testcase import securityBatchGen
from testcase import securitybatchimp
from testcase import securityOne
from testcase import securityBatchEdit
from testcase import securityDelete
@ddt
class MainFun_02(unittest.TestCase):
	mm = loginTo.LoginTo()
	md = mm.driver
	# @classmethod
	# def setUpClass(cls):
	# 	cls.mm.login()
	# 	cls.md.maximize_window()
	# 	time.sleep(3)
	#批量生成防伪码
	def test_01(self):
		self.s1 = securityBatchGen.SecurityBatchGen()
		self.s1.test_01_add()
		xx = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(xx,msg="新增防伪码失败")

	def test_02(self):
		self.s2 = securitybatchimp.SecurityImp()
		self.s2.test_Imp()

	def test_03(self):
		self.s3 = securityOne.SecurityOne()
		self.s3.test_One()
		xx = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(xx,msg="生成单个防伪码失败")

	def test_04(self):
		self.s4 = securityBatchEdit.Security_Edit()
		self.s4.test_logistic()
		x1 = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x1,msg="按物流码修改失败")

		self.s4.test_ID()
		x2 = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x2, msg="按ID修改失败")

		self.s4.test_Pc()
		x3 = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x3, msg="按批次修改失败")

		self.s4.test_product()
		x4= self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x4, msg="按产品修改失败")

		self.s4.test_date()
		x5 = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x5, msg="按日期修改失败")

	def test_05(self):
		self.s5 = securityDelete.Security_Del()
		self.s5.test_del_Pc()
		x2 = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x2, msg="按批次删除失败")

		self.s5.test_del_Product()
		x2 = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x2, msg="按产品删除失败")

		self.s5.test_del_Date()
		x2 = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x2, msg="按日期删除失败")

		self.s5.test_del_Num()
		x2 = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x2, msg="按修改次数删除失败")

		self.s5.test_del_All()
		x2 = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x2, msg="全部删除失败")

	@classmethod
	def tearDownClass(cls):
		cls.md.quit()

# if __name__ == '__main__':
#
#     unittest.main()