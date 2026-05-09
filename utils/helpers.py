#inicializamos nuestro web driver

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# importo los servicios para actualizar el navegador 
from selenium.webdriver.chrome.service import Service


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# funcion que nos permite instalar el Driver

def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
# nos tiene que devolver el driver
    return driver

#necesito abrir el navegador
# para ello creo un Fx
 

 #paso el driver y los datos que necesito para el login
def login(driver, username, password):
    
    driver.get("https://www.saucedemo.com")