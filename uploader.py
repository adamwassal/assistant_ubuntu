from time import sleep
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import os

username = input('Enter Your github username: ') # if you want enter the username auto delete "input('Enter Your github username: ')" and write your username 'username'
password = input('Enter Your github password: ') # if you want enter the password auto delete "input('Enter Your github password: ')" and write your username 'password'
repo_name = input('Enter repo name: ')
commit = input('Your commit: ')
what = str(input("""
    what do you want
             1- upload first
             2- update the repo
    ??: 
"""))
while True:
    if what == '1':

        driver  = webdriver.Chrome()
        driver.get(url='https://github.com/new')

        if driver.current_url != 'https://github.com/new':
            XPATH_username='//*[@id="login_field"]'
            XPATH_pass='//*[@id="password"]'
            XPATH_sub='//*[@id="login"]/div[4]/form/div/input[13]'
            driver.find_element(By.XPATH,XPATH_username).send_keys(username)
            sleep(2)

            driver.find_element(By.XPATH,XPATH_pass).send_keys(password)
            sleep(2)

            driver.find_element(By.XPATH,XPATH_sub).click()
            if driver.current_url == 'https://github.com/sessions/verified-device':
                sleep(60)
        XPATH_name='//*[@id=":r3:"]'
        XPATH_clock='/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button'

        driver.find_element(By.XPATH,XPATH_name).send_keys(repo_name)
        sleep(2)

        driver.find_element(By.XPATH,XPATH_clock).click()

        os.system('git init')
        os.system(f'git add .')
        os.system(f"git commit -m '{commit}'")
        os.system(f"git remote add origin https://github.com/{username}/{repo_name}.git")
        os.system('git push -u origin master')
        break
    elif what == '2':
        os.system(f'git add .')
        os.system(f'git status')
        os.system(f"git commit -m '{commit}'")
        os.system('git push')
        break

    else:
        print('error please enter (1, 2)')
        pass