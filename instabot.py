from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time

class InstagramBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Firefox()

	def closeBrowser(self):
		self.driver.close()

	def login(self):
		driver = self.driver
		driver.get("https://www.instagram.com/")
		time.sleep(5)
		user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
		user_name_elem.clear()
		user_name_elem.send_keys(self.username)
		passwarword_elem = driver.find_element_by_xpath("//input[@name='password']")
		passwarword_elem.clear()
		passwarword_elem.send_keys(self.password)
		passwarword_elem.send_keys(Keys.RETURN)
		time.sleep(5)

	def follow_users_followers(self, user):
		#Going in the url of the account of we want

		driver = self.driver
		driver.get("https://www.instagram.com/" + user + "/")
		time.sleep(5)

	#Clicking onthe followers button

		driver.find_element_by_xpath("//a[@class='-nal3 ']").click()
		time.sleep(3)

	#Scrolling down

		followers_tab = driver.find_element_by_class_name("isgrP")
		followers_tab.click()
		for _ in range(1000):
			followers_tab.send_keys(Keys.ARROW_DOWN)
		time.sleep(2)

	#Following people]
		#b = 0
		a = 0
		#exit_butt = driver.find_element_by_class_name("QBdPU ")


		follow_buttons = driver.find_elements_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
		print(str(len(follow_buttons)))

		for follow_button in follow_buttons:
			follow_button.click()
			time.sleep(1)
			a += 1
			if(a == 40):
				time.sleep(3700)
				break
			#b += 1
			#print(b)
			#if(b == 30):
				#break

username = input("Username: ")
password = input("Password: ")
user = input("User that you want to follow followers: ")
while True:
	aldoIG = InstagramBot(username,password)
	aldoIG.login()
	aldoIG.follow_users_followers(user)
	aldoIG.closeBrowser()
