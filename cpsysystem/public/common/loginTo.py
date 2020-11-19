'''
项目名称:产品溯源系统
所属模块:登录
日期:2020/10/30
作者:李锦龙
版本:version:1.0
'''
import time
from selenium import webdriver

class LoginTo():
	driver = webdriver.Firefox()
	driver.get("http://123.57.140.190/manage/")
	def login(self):
		self.driver.find_element_by_xpath("//input[@placeholder='管理员帐号']").send_keys("admin")
		self.driver.find_element_by_xpath("//input[@type='password']").send_keys("admin999")
		self.driver.find_element_by_css_selector(".btn").click()
		time.sleep(2)
		# try:
		# 	x = self.driver.find_element_by_css_selector("#top_menu > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)").text
		# 	if x=='前台浏览':
		# 		print("login success!")
		# except Exception as a:
		# 	print(a)

