import requests
import json

class Login():
	def lg(self):

		url = "http://123.57.140.190/manage/?act=adminlogin"
		headers = {'Content-Type':'application/x-www-form-urlencoded'
				# 'Cookie':"revptdv10lh6ms9fp4rb5ok687"
				  }
		payload= {
				'Username':'admin',
				'Password':'admin999',
				'Submit':'管理登录'
		}
		r = requests.post(url,headers=headers,data=payload)
		cookie = r.cookies['PHPSESSID']
		return cookie

