from utils.helpers import login


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#funcion que testea el login
def test_login( driver ):
    login(driver, "standard_user", "secret_sauce")
    #validamos que x está en la url
    
    #verifica que inventory.html esté dentro de la URL actual
    assert "inventory.html" in driver.current_url

    title = driver.find_element(By.CLASS_NAME, "title").text
    # valido si titulo = Products   
    assert title == "Products"

def test_catalog_products( driver):
    login(driver, "standard_user", "secret_sauce")

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"
    #valido la presencia del contenedor que contiene los productos
    productos = driver.find_elements(By.CSS_SELECTOR, "[data-test = 'inventory-item']")
    
    #verifico que tenga mas de 0 para poder visualizar
    assert len(productos) > 0 

    nombre = productos[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
    assert nombre == "Sauce Labs Backpack"
    
    precio = productos[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-price']"
    ).text
    
    
    print(f"Precio: {precio}")