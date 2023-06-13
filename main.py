from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui


# переменные для логина пароля и полного пути к файлу(фото)
username = 'username'
password = 'password'
photo = 'Полний путь к фотографии'


driver = webdriver.Chrome()


url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
driver.get(url)
sleep(10)

# Вход в аккаунт
# введения логина
login = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
login.send_keys(username)
sleep(1)

# Введения пароля
password_ = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
password_.send_keys(password)
sleep(1)

# нажатие на кнопку входа
button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
button.click()
sleep(15)

# Выставляем фото
# нажатие на кнопку новая публикация
but_1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span')
but_1.click()
sleep(1)

# нажатие на кнопку выбора фото
but_2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button')
but_2.click()
sleep(1)


# загрузка фото
pyautogui.typewrite(photo)
pyautogui.press('enter')
sleep(5)


# нажатие на кнопку далее
but_next = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div')
but_next.click()
sleep(1)

# нажатие на кнопку далее
but_next_2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div')
but_next_2.click()
sleep(1)

# вставляем текст в описание к фото

send_bio = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]')
send_bio.send_keys('The official home of the Python Programming Language.')
sleep(3)


# публикация фото
share = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div')
share.click()
sleep(15)


# выход из аккаунта
button_menu = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/span/div/a/div')
button_menu.click()
sleep(1)


quit_ = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[6]/div[1]')
quit_.click()


sleep(10)


driver.quit()


