from Utils.geradorDeUsername import gerarUserame
from Model.ComandosWebdriver import *
from Model.WebdriverModelBot import Navegador
from Controllers.ManipularEmailController import *
from Model.ManipularCookies import *

def Criar_Conta(driver):
    
    username = gerarUserame()

    driver.get("https://gemly.gg/?r=pedrocamposrr608")
    sleep(2)

    #clicar no a com o class "link" e p href="/signup"
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        try:
            if link.get_attribute("href") == "https://gemly.gg/signup":
                link.click()
                break
        except:pass
    sleep(2)

    digitar_username = digitar_texto_tagname_name(driver, "input", "login", username)
    if digitar_username == False:
        return False
    
    #Invocar um navegador para manipular o site de email
    Email = Navegador(headless=True)
    driver_email = Email.driver

    email = novo_email(driver_email)
    if email == False:
        return False
    
    digitar_email = digitar_texto_tagname_name(driver, "input", "email", email)
    if digitar_email == False:
        return False

    digitar_senha = digitar_texto_tagname_name(driver, "input", "password", "@Luc97ari")
    if digitar_senha == False:
        return False
    
    digitar_senha_confirmar = digitar_texto_tagname_name(driver, "input", "password-confirm", "@Luc97ari\n")
    if digitar_senha_confirmar == False:
        return False
    
    contador = 0
    while True:
        if driver.current_url != "https://gemly.gg/signup":
            break
        sleep(2)
        contador += 1
        if contador == 100:
            return False
    
    link_confirmar_conta = capturar_link_confirmar_conta(driver_email)
    driver_email.quit()
    if link_confirmar_conta == False:
        return False
    
    link_confirmar_conta = link_confirmar_conta.replace('https://anon.ws/?', '')
    driver.get(link_confirmar_conta)
    sleep(2)

    driver.get("https://gemly.gg/game")
    sleep(4)

    #clicar na div com tem a class = "times-close"
    for i in range(2):
        driver.find_element(By.CLASS_NAME, "times-close").click()
        sleep(1.6)
    sleep(2)

    #clicar na div com a class = "mobile-trigger"
    driver.find_element(By.CLASS_NAME, "mobile-trigger").click()
    sleep(1.8)

    #clicar na div com a class = "button" o atributo data-action="skip" e o texto "Pular tutorial"
    driver.find_element(By.CSS_SELECTOR, "div[data-action='skip']").click()
    sleep(1.8)

    #clicar no button com o texto "Pular" 
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for button in buttons:
        try:
            if button.text == "PULAR":
                button.click()
        except:pass
    sleep(4)

    #clicar na div com a class = "cell custom" e o atributo data-tooltip-id="19"
    divs = driver.find_elements(By.CLASS_NAME, "cell")
    for div in divs:
        try:
            if div.get_attribute("data-tooltip-id") == "19":
                div.click()
                break
        except:pass

    #tentar em todos os inputs com o name="count" ate conseguir inserir o texto "100155" 
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for input in inputs:
        try:
            if input.get_attribute("name") == "count":
                input.send_keys("100155")
                break
        except:pass
    
    #tentar em todos os div com a class = "button" e o atributo data-action="buy" ate conseguir clicar
    divs = driver.find_elements(By.CLASS_NAME, "button")
    for div in divs:
        try:
            if div.get_attribute("data-action") == "buy":
                div.click()
                break
        except:pass


    
    #Salvar os dados de username email e senha na ultima linha do arquivo "contas.txt"
    with open("contas.txt", "a") as arquivo:
        arquivo.write(f"{username} {email} @Luc97ari\n")
        arquivo.write("\n")
    return [username, email, "@Luc97ari"]



def criar_conta_payeer(driver):
    driver.get("https://payeer.com/en/auth/?register=yes")
    sleep(2)

    #Invocar um navegador para manipular o site de email
    Email = Navegador(headless=True)
    driver_email = Email.driver

    email = novo_email(driver_email)
    if email == False:
        return False
    
    digitar_email = digitar_texto_tagname_name(driver, "input", "email", email+"\n")
    if digitar_email == False:
        return False
    sleep(2)

    codigo = capturar_codigo_confirmar_conta_payeer(driver_email)
    driver_email.quit()
    if codigo == False:
        return False
    
    digitar_codigo = digitar_texto_tagname_name(driver, "input", "code", codigo+"\n")
    if digitar_codigo == False:
        return False
    sleep(2)

    contador = 0

    while True:
        try:
            #limpar input e digitar a senha
            input_senha = driver.find_element(By.NAME, "new_password")
            input_senha.clear()
            input_senha.send_keys("@Luc97ari")
            break
        except:
            sleep(1)
            contador += 1
            if contador == 15:
                return False

    #limpar input e digitar a senha
    input_senha_confirmar = driver.find_element(By.NAME, "new_password2")
    input_senha_confirmar.clear()
    input_senha_confirmar.send_keys("@Luc97ari")

    #limpar o input e digitar o secret code
    input_code = driver.find_element(By.NAME, "secret_word")
    input_code.clear()
    input_code.send_keys("249710")

    #capturar o numero da conta payeer
    input_account_number = driver.find_element(By.NAME, "nick")
    account_number = input_account_number.get_attribute("value")


    buttons = driver.find_elements(By.TAG_NAME, "button")
    for button in buttons:
        try:
            if button.text == "Next":
                button.click()
                break
        except:pass
    
    contador = 0 
    while True:
        try:
            #Inserir o nome e sobrenome 
            input_name = driver.find_element(By.NAME, "name")
            input_name.send_keys("Lucas")
            break
        except:
            sleep(1)
            contador += 1
            if contador == 15:
                return False

    input_sobrenome = driver.find_element(By.NAME, "last_name")
    input_sobrenome.send_keys("Henrique\n")

    sleep(5)

    return {"email":email, "senha":"@Luc97ari", "account_number":account_number}
