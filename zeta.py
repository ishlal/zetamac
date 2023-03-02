from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
if __name__ == "__main__":
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(driver_path)
    driver.get("http://arithmetic.zetamac.com")
    # driver.find_element_by_id("username").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    # words = driver.find_element(By.XPATH, "//span[@class='problem']").text
    
    while(True):
        try:
            words = driver.find_element(By.XPATH, "//span[@class='problem']").text.split(" ")
            # print(ord(words[1]))
            ans = 0
            if ord(words[1]) == 43:
                print('add')
                ans = int(words[0]) + int(words[2])
            elif ord(words[1]) == 8211:
                print('subtract')
                ans = int(words[0]) - int(words[2])
            elif ord(words[1]) == 215:
                print('multiply')
                ans = int(words[0]) * int(words[2])
            elif ord(words[1]) == 247:
                print('divide')
                ans = int(int(words[0]) / int(words[2]))
            driver.find_element(By.XPATH, "//input[@class='answer']").send_keys(ans)
            print(ans)
        except:
            pass
    sleep(10)