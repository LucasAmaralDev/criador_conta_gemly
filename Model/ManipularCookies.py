import pickle

def salvar_cookies(driver, username):
    cookies = driver.get_cookies()
    with open(f"./cookies/{username}.pkl", "wb") as f:
        pickle.dump(cookies, f)

def carregar_cookies(driver, username):
    with open(f"./cookies/{username}.pkl", "rb") as f:
        cookies = pickle.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    return driver