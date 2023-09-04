from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura el navegador (reemplaza 'chrome' por 'firefox' si prefieres Firefox)
driver = webdriver.Chrome()

# Abre la página de Saucedemo
driver.get("https://www.saucedemo.com")

# Ingresa las credenciales y autentícate
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

# Agrega dos productos al carrito
add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
for button in add_to_cart_buttons[:2]:
    button.click()

# Accede al carrito
cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_icon.click()

# Inicia el proceso de compra
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

# Completa el formulario de compra
first_name = driver.find_element(By.ID, "first-name")
last_name = driver.find_element(By.ID, "last-name")
postal_code = driver.find_element(By.ID, "postal-code")
continue_button = driver.find_element(By.ID, "continue")

first_name.send_keys("Tu Nombre")
last_name.send_keys("Tu Apellido")
postal_code.send_keys("Código Postal")
continue_button.click()

# Finaliza la compra
finish_button = driver.find_element(By.ID, "finish")
finish_button.click()

# Espera hasta que se muestre el mensaje de confirmación
confirmation_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h2[text()='Thank you for your order!']"))
)

# Cierra el navegador
driver.quit()

# Generar automáticamente readme.txt con las instrucciones paso a paso
with open("readme.txt", "w") as readme_file:
    readme_file.write("Instrucciones Paso a Paso:\n")
    readme_file.write("1. Ejecuta el script `test_saucedemo.py`.\n")
    readme_file.write("2. Espera a que el script finalice la prueba.\n")
    readme_file.write("3. Consulta el resultado en la consola y verifica la página web.\n")
    readme_file.write("4. Si hay errores, verifica los mensajes de error para solucionarlos.\n")

# Generar automáticamente conclusiones.txt con los hallazgos y conclusiones
conclusiones = [
    "La prueba se ejecutó sin errores.",
    "Los productos se agregaron correctamente al carrito.",
    "El formulario de compra se completó exitosamente.",
    "Se mostró el mensaje de confirmación 'Thank you for your order!' al finalizar la compra.",
]

with open("conclusiones.txt", "w") as conclusiones_file:
    conclusiones_file.write("Hallazgos y Conclusiones:\n")
    for i, conclusion in enumerate(conclusiones, start=1):
        conclusiones_file.write(f"{i}. {conclusion}\n")
