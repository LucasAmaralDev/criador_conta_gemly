from Model.ComandosWebdriver import *

def novo_email(driver_email):

    driver_email.get("https://tmail.social/mailbox")

    email = retornar_texto_tagname_id(driver_email, "div", "email_id")
    if email == False:
        return False
    
    return email

    
def capturar_link_confirmar_conta(driver_email):
    contador = 0
    while True:
        try:
            clicar_botao_email = driver_email.find_element(By.XPATH, "/html/body/div[1]/main/div/div[1]/div/div/div[1]/div[2]/div").click()
            break
        except:
            contador += 1
            sleep(1)
        if contador == 21:
            return False
    #Entrar no primeiro iframe
    driver_email.switch_to.frame(0)
    #retornar o href ta tagname a com o texto "Confirmar Email"
    contador = 0
    while contador < 5:
        try:
            elemento_a = driver_email.find_elements(By.TAG_NAME, "a")
            for elemento in elemento_a:
                try:
                    if elemento.text == "Confirmar Email":
                        return elemento.get_attribute("href")
                except:pass
        except:pass
        contador += 1
        sleep(1)
    return False

def capturar_codigo_confirmar_conta_payeer(driver_email):
    contador = 0
    driver_email.refresh()
    while True:
        try:
            clicar_botao_email = driver_email.find_element(By.XPATH, "/html/body/div[1]/main/div/div[1]/div/div/div[1]/div[2]/div").click()
            break
        except:
            contador += 1
            sleep(1)
        if contador == 40:
            return False
    #Entrar no primeiro iframe
    driver_email.switch_to.frame(0)
    #retornar o texto no xpath "/html/body/div/div[1]/div[4]/span"
    contador = 0
    while contador < 5:
        try:
            texto = driver_email.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/span").text
            return texto
        except:pass
        contador += 1
        sleep(1)
    return False

    
