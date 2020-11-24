'''
项目名称:产品溯源系统
所属模块:溯源实例管理unittest
日期:2020/11/08
作者:李锦龙
版本:version:1.0
'''
import time
import unittest
from ddt import ddt,data,unpack
from data.testdata import getdata
from public.common import loginTo
from testcase import addSource
from testcase import sourceManage
from testcase import batchSource
from testcase import sourceRecord
@ddt
class MainFun_01(unittest.TestCase):
	# mm = loginTo.LoginTo()
	# md = mm.driver
	# @classmethod
	# def setUpClass(cls):
	# 	cls.mm.login()
	# 	cls.md.maximize_window()
	# 	time.sleep(2)
	#打开溯源实例管理功能
	def test_06(self):
		self.s1 = addSource.AddSource()
		self.s1.test_01_pre()

	ms = getdata.GetData(r"../data/testdata/data.xlsx", "addshili").login_data()
	@data(*ms)
	@unpack
	#新增溯源实例
	def test_07(self,a,b):
		self.md.find_element_by_link_text("新增溯源实例").click()
		time.sleep(1)
		self.s2 = addSource.AddSource()
		self.s2.test_02_add(a,b)
		x = self.md.find_element_by_id("layui-layer1")
		self.assertTrue(x,msg="新增失败")

	#溯源实例管理
	def test_08(self):
		self.s3 = sourceManage.SourceManage()
		self.s3.test_02_search()
		a = self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > b:nth-child(2)").text
		self.assertIn("产品", a, msg="搜索失败")
		# print("搜索执行成功")
		self.s3.test_03_edit()
		x = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x, msg="编辑失败")
		# print("编辑执行成功")
		x = self.s3.test_04_del()
		y ="批量删除成功"
		self.assertEqual(x,y,msg="失败")
		# print("删除执行成功")
	#批量溯源操作
	def test_09(self):
		self.s4 = batchSource.BatchSource()
		self.s4.batch_Logistic()
		x = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x, msg="失败")

		self.s4.batch_Id()
		x = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x, msg="失败")

		self.s4.batch_Pc()
		x = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x, msg="失败")

		self.s4.batch_name()
		x = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x, msg="失败")

		self.s4.batch_date()
		x = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x, msg="失败")

	#溯源操作记录
	def test_10(self):
		self.s5 = sourceRecord.SourceRecord()
		self.s5.test_search()
		a = self.md.find_element_by_css_selector(
			".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > p:nth-child(4)").text
		self.assertIn("2020", a, msg="搜索失败")

		x = self.s5.test_del()
		y = "批量删除成功"
		self.assertEqual(x,y,"删除失败")
	# @classmethod
	# def tearDownClass(cls):
	# 	cls.md.quit()
#
# if __name__ == '__main__':
#     unittest.main()