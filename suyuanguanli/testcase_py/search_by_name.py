import requests
from requests_toolbelt.multipart import MultipartEncoder
from testcase_py.common import login

class AddProduct():
	lg = login.Login()
	ck = lg.lg()
	cookie = 'PHPSESSID='+ck
	def addProduct(self):

		url = "http://123.57.140.190/manage/list_cp.php?pro_name=4523"
		payload=MultipartEncoder( {
				'pro_name':'qqq'
		})
		headers = {'Content-Type': payload.content_type,
				   'Cookie':self.cookie}
		r = requests.post(url,headers=headers,data=payload)
		print(r.text)
