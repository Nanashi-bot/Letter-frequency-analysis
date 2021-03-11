from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Path to chromedriver
# PATH = '/home/aditya/Desktop/python_work/cypher_breaking/chromedriver.exe'

# To stop browser from opening
options = Options()
options.add_argument("headless")
# self.driver = webdriver.Chrome(executable_path='/Users/${userName}/Drivers/chromedriver', chrome_options=options)

driver = webdriver.Chrome(options=options)
url = "http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html"
driver.get(url)

letter_frequency = {}
letter = ''
frequency = 0

for i in range(2, 28):
    letter_xpath = '/html/body/font/center[2]/table/tbody/tr[{}]/td[4]/font'.format(
        i)
    frequency_xpath = '/html/body/font/center[2]/table/tbody/tr[{}]/td[5]/font'.format(
        i)
    letter = driver.find_element_by_xpath(letter_xpath).text
    frequency = float(driver.find_element_by_xpath(frequency_xpath).text)
    letter_frequency[letter] = frequency


driver.quit()
print(letter_frequency)
