import pyautogui

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
pyautogui.write("web.whatsapp")
pyautogui.press("enter")

import pandas as pd
tabela = pd.read_csv("teste.csv")
print(tabela)

for i in tabela.index:
    print(tabela.loc[i,"nome"])