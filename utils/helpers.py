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
    #configuramos una espera para la carga de los elementos

    wait = WebDriverWait(driver,10)
    #pasamos la url a buscar
    driver.get("https://www.saucedemo.com")

    # localizamos el username, para eso buscamos el selector.
    #verificamos la presencia del elemento ID
    wait.until(
        EC.presence_of_element_located((By.ID,"user-name"))
    ).send_keys(username)

  
   # Espera explícita para asegurar la presencia de los campos
    wait.until(
        EC.presence_of_element_located((By.ID, "password"))

    ).send_keys(password)
    wait.until(
        EC.presence_of_element_located((By.ID, "login-button"))

    ).click()