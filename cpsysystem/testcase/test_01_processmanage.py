'''
项目名称:产品溯源系统
所属模块:流程记录管理unittest
日期:2020/11/05
作者:李锦龙
版本:version:1.0
'''
import time
import unittest
from testcase import processRecord
from testcase import reordManage
from testcase import addRecord
from testcase import msgManage
from ddt import ddt,data,unpack
from data.testdata import getdata
from public.common import loginTo

@ddt
class MainFun(unittest.TestCase):
	mm = loginTo.LoginTo()
	md = mm.driver
	@classmethod
	def setUpClass(cls):
		time.sleep(5)
		cls.mm.login()
		cls.md.maximize_window()
		time.sleep(2)

	# 新增流程类别
	def test_01(self):
		self.x1 = processRecord.ProcessRecord()
		self.x1.test_02_pre()

	ms = getdata.GetData(r"../data/testdata/data.xlsx","addrecord").login_data()
	@data(*ms)
	@unpack
	def test_02(self,p1,p2):
		self.x2 = processRecord.ProcessRecord()
		self.x2.test_02_addRecord(p1,p2)
		# a = self.md.find_element_by_css_selector(".layui-layer-content")
		# self.assertTrue(a, "失败")
		#流程类别管理
	def test_03(self):
		#搜索流程
		self.x3 = reordManage.RecordManage()
		self.x3.test_02_searchRecord()
		a = self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)").text
		self.assertIn("取消",a,msg="搜索失败")
		#编辑流程类别记录
		self.x3.test_03_editRecord()
		x =self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(x,msg="编辑失败")

		#删除流程记录
		a =self.x3.test_04_delRecord()
		b = "批量删除成功"
		self.assertEqual(a,b,msg="失败")

	ms1 = getdata.GetData(r"../data/testdata/data.xlsx","lcjl").login_data()
	@data(*ms1)
	@unpack
	def test_04(self,lgs):
		#录入流程记录
		wlh = lgs
		self.ad= addRecord.AddRecord()
		self.ad.test_01_add(wlh)
		a = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(a,msg="录入流程记录失败")

	def test_05(self):
		#流程记录管理
		self.x5 = msgManage.MsgManage()
		self.x5.test_02_searchMsg()
		a = self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4) > span:nth-child(1)").text
		self.assertIn("5",a,msg="搜索失败")
		self.x5.test_03_editMsg()
		b = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(b, msg="更新失败")
		self.x5.test_04_delMsg()
		c = self.md.find_element_by_css_selector(".layui-layer-content")
		self.assertTrue(c,msg="删除失败")
	# @classmethod
	# def tearDownClass(cls):
	# 	cls.md.quit()

if __name__ == '__main__':
    unittest.main()