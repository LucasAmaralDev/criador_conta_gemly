from Model.WebdriverModelBot import Navegador
from Controllers.CreateAccountController import Criar_Conta




contador = 0

while contador < 10:
    Bot = Navegador()
    driver = Bot.driver
    Criar_Conta(driver)
    driver.quit()

