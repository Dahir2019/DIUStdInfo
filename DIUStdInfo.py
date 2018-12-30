#!/usr/bin/python

from bs4 import BeautifulSoup
import requests, sys,json
import time
from time import ctime,sleep
#from fake_useragent import UserAgent
#global ua
#ua = UserAgent()

# terminal colors
R = "\033[1;31m"  
B = "\033[1;34m"
CY = "\033[1;36m"
G = "\033[1;32m"
Y = "\33[1;93m"
NO = "\033[0;0m"
BO = "\033[;1m"

def request():
	url = 'http://software.diu.edu.bd/studentportalApi/result/studentInfo?studentId='
	#headers = {
	#	"User-Agent": str(ua.chrome)
	#}

	#requesting with the help of handling errors
	try:
		ID = input(G+"ID: (ex: 172-15-1502)  "+NO)
		resp = requests.get(url+ID).json() #, headers=headers
		print (B+"Requesting Data..."+NO)
		
	except KeyboardInterrupt:
		print (R+"Exiting..."+NO)
		sys.exit()

	print(G+"Retreving Data of the Student...\n"+NO)
	time.sleep(2)
	print(G+"Started Time: "+NO+time.ctime())
	
	
	print ("Student Name: ",resp['studentName'])
	print ("Student ID: ",resp['studentId'])
	print ("Campus Name: ",resp['campusName'])
	print ("Batch ID: ",resp['batchId'])
	print ("Batch No: ",resp['batchNo'])
	print ("Program ID: ",resp['programId'])
	print ("Program Name: ",resp['programName'])
	print ("Program ShortName: ",resp['progShortName'])
	print ("Program Type: ",resp['programType'])
	print ("Dept Name: ",resp['departmentName'])
	print ("Dept ShortName: ",resp['deptShortName'])
	print ("Faculty Name: ",resp['facultyName'])
	print ("Faculty ShortName: ",resp['facShortName'])
	print ("Semester ID: ",resp['semesterId'])
	print ("Semester Name: ",resp['semesterName'])
	print ("Shift: ",resp['shift'])
	
	print(G+"\nEnded Time: "+NO+time.ctime())


	
if __name__ == "__main__":
	request()


