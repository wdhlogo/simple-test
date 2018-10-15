
from selenium import webdriver
import time

	
def Login_url():

	driver=webdriver.Chrome()
	"""driver=webdriver.Ie()"""
	username='wdhlogo'
	passw='wdhlogo336*'
	url='https://mail.126.com/'
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