
from selenium import webdriver
import time
import xlrd

#增加注释 
def Login_url():
	
	#打开一个workbook
	workbook = xlrd.open_workbook('D:\\python_jenkins\\simple-test\\dataforlogin.xls')
	#抓取所有sheet页的名称
	worksheets = workbook.sheet_names()
	print('worksheets is %s' %worksheets)
	#定位到sheet1
	worksheet1 = workbook.sheet_by_name(u'Sheet1')
	"""
	#遍历sheet1中所有行row
	num_rows = worksheet1.nrows
	for curr_row in range(num_rows):
		row = worksheet1.row_values(curr_row)
		print('row%s is %s' %(curr_row,row))
	#遍历sheet1中所有列col
	num_cols = worksheet1.ncols
	for curr_col in range(num_cols):
		col = worksheet1.col_values(curr_col)
		print('col%s is %s' %(curr_col,col))
	#遍历sheet1中所有单元格cell
	for rown in range(num_rows):
		for coln in range(num_cols):
			cell = worksheet1.cell_value(rown,coln)
			print (cell)
				
	"""		
	#driver=webdriver.Chrome()
	#driver=webdriver.Ie()
	driver=webdriver.Ie()
	#改成从excel里读出来
	username=worksheet1.cell_value(1,1)
	passw=worksheet1.cell_value(1,2)
	url=worksheet1.cell_value(1,0)
	driver.get(url)
	time.sleep(1)
	elem=driver.find_element_by_id("lbNormal")
	elem.click()
	
	driver.switch_to.frame('x-URS-iframe')

	elem=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div/div[2]/input")
	elem.clear()
	elem.send_keys(username)
	elem=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]")
	elem.send_keys(passw)
	elem=driver.find_element_by_xpath("//div[@id='cnt-box']/div[2]/form/div/div[8]/a")
	elem.click()
	
	"""def Logini(driver,username,passw):
		url='https://mail.126.com/'
		driver.get(url)
		elem=driver.find_element_by_id("lbNormal")
		elem.click()
		elem=driver.find_element_by_xpath("html/body/div[2]/div[2]/form/div/div/div[2]/input[@name='email']")
		elem.send_keys(username)
		elem=driver.find_element_by_id("html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[@name='password']")
		elem.send_keys(passw)
		elem=driver.find_element_by_id("dologin")
		elem.click()
	"""
	
if __name__ == '__main__':
	
	Login_url()