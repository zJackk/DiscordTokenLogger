from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os, ctypes, time
ctypes.windll.kernel32.SetConsoleTitleW("Token Logger")
driver = webdriver.Chrome(ChromeDriverManager().install())
cmd = 'mode 60,15'
os.system(cmd)
def cls():
    os.system("cls" if os.name == "nt" else "clear")   
def start():
    cls();   
    print(
    '''
     _____ _____ _   __ _____ _   _  _     _____ _____ 
    |_   _|  _  | | / /|  ___| \ | || |   |  _  |  __ |
      | | | | | | |/ / | |__ |  \| || |   | | | | |  \/
      | | | | | |    \ |  __|| . ` || |   | | | | | __ 
      | | \ \_/ / |\  \| |___| |\  || |___\ \_/ / |_\ |
      \_/  \___/\_| \_/\____/\_| \_/\_____/\___/ \____/
    '''
    )
    atoken = input("Token: ")
    cls()
    print(f"logging token: {atoken}")
    URL = 'https://www.discord.com/login'
    driver.get(URL)
    driver.execute_script(
        '''
        function login(token) {
        setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
        location.reload();
        }, 2500);
        }
        login("''' + atoken + '''")'''             
    )
    start()
start()



