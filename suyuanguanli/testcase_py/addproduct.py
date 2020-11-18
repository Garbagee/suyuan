import requests
from requests_toolbelt.multipart import MultipartEncoder
from testcase_py.common import login

class AddProduct():
	lg = login.Login()
	ck = lg.lg()
	cookie = 'PHPSESSID='+ck
	def addProduct(self):

		url = "http://123.57.140.190/manage/add_cp.php?act=save_cp"
		# coo={'PHPSESSID':'qvmu3fuulec8nfoio3nqgke121'}
		# headers = {'Content-Type':'multipart/form-data'
		# 		  }
		payload=MultipartEncoder( {
				'pro_name':'test1551',
				'cpbh':'125801258',
				'cptxm':'352522',
				'cpms':'11111'
		})
		headers = {'Content-Type': payload.content_type,
				   'Cookie':self.cookie}
		r = requests.post(url,headers=headers,data=payload)
		print(r.text)
