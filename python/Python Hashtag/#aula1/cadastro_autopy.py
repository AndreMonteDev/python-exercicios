import pyautogui
import time
import pandas
from unicodedata import category

# executar pyautogui com intervalo de 0.5 segundos
pyautogui.PAUSE = 0.5

# abrir chorme e endereço de url
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)

# clicar nas celulas e inserir email e senha
pyautogui.click(x=2620, y=406)
pyautogui.write("meuemail@gmail.com")
pyautogui.click(x=2637, y=509)
pyautogui.write("Senha@123")
pyautogui.press("tab")
pyautogui.press("enter")

# importar base de dados csv
tabela = pandas.read_csv("produtos.csv")
# print(tabela)

# buscar dados na tabela e preencher no site

for linha in tabela.index:

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.click(x=2596, y=290)
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("home")
