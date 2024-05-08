import pyautogui
import time
import pandas as pd
import keyboard

pyautogui.PAUSE = 0.3

#botão para interromper a automação
def on_esc_press(event):
    if event.name == 'esc':
        global stop_loop
        stop_loop = True

# Registra a função para reagir à tecla "ESC" pressionada
keyboard.on_press(on_esc_press)
stop_loop = False

pyautogui.press("win")
pyautogui.write("edge")#pode colocar o nome do navegador que voce usa
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")#link usado
pyautogui.press("enter")
time.sleep(4)

pyautogui.click(x=696, y=365)#coloque a posição que o seu cursor fica quando utiliza a barra de texto de login
pyautogui.write("seuemail@gmail.com")#coloque seu e-mail de login
pyautogui.press("tab") 
pyautogui.write("senha")#coloque sua senha
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)


tabela = pd.read_csv("produtos.csv")#caso a tabela não esteja na pasta do programa coloque o caminho dela no lugar

print(tabela)


for linha in tabela.index:
       
    pyautogui.click(x=764, y=232)#coloque a posição que o seu cursor fica na primeira caixa de texto
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    pyautogui.scroll(10000)
    if stop_loop:  # Verifica se a tecla "ESC" foi pressionada
        print("Loop interrompido pelo usuário.")
        break 
    
