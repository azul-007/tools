from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/danny/Projects/tools/reconnaissance/chromedriver")
driver.maximize_window()
driver.get("http://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_name("email").send_keys("Shetty")



#driver.find_element_by_id("exampleCheck1").click()