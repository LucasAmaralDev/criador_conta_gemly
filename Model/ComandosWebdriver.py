from selenium.webdriver.common.by import By
from time import sleep


def digitar_texto_tagname_name(driver, tagname, name, texto):
    contador = 0
    while contador < 5:
        sleep(1)
        elemento_tagname = driver.find_elements(By.TAG_NAME, tagname)
        for elemento in elemento_tagname:
            try:
                if elemento.get_attribute("name") == name:
                    elemento.send_keys(texto)
                    return True
            except:pass
        contador += 1
    return False


def retornar_texto_tagname_id(driver, tagname, id):
    contador = 0
    while contador < 5:
        sleep(1)
        elemento_tagname = driver.find_elements(By.TAG_NAME, tagname)
        for elemento in elemento_tagname:
            try:
                if elemento.get_attribute("id") == id:
                    return elemento.text
            except:pass
        contador += 1
    return False