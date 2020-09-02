from selenium import webdriver
import time

class webDrivers:

	def openLink(self,link,mail,password):
		driver = webdriver.Chrome(executable_path="chromedriver.exe")
		driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
		time.sleep(5)
		driver.find_element_by_name("identifier").send_keys(mail)

		driver.find_element_by_id("identifierNext").click()
		time.sleep(7)
		driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
		driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()

		time.sleep(10)


		frame = driver.execute_script("window.open('{}');".format(link))
		time.sleep(7)

		driver.switch_to.window(driver.window_handles[-1])
		driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click()
		time.sleep(3)

		# time.sleep(7)
		driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()