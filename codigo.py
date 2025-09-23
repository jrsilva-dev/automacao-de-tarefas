import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.8

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=687, y=367)
pyautogui.write("jrsilva.dev084@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.press("enter")

time.sleep(2)

tabela = pandas.read_csv("C:\\Users\Jr\\Documents\\VSCode\\python powerup\\gabarito\\produtos.csv")
print(tabela)

pyautogui.click(x=669, y=255)

for linha in tabela.index:

    pyautogui.click(x=669, y=255)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")


    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")


    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")


    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")


    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")


    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")


    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000) 
