import customtkinter as ctk
import pandas as pd
import pyautogui
import pyscreeze


def pegarInformacoes():
    df = pd.read_excel("arquivo_teste.xlsx")
    df = pd.DataFrame(df)
    
    localizarImg = pyscreeze.locateOnScreen("novoUser.PNG",confidence=0.8)
    if localizarImg:
        x,y = pyautogui.center(localizarImg)
        pyautogui.click(x,y)
    
    
    #for d in df.values:
        #print(d[0])



ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Teste")
app.geometry("200x200")

label = ctk.CTkLabel(app, text="Clique no botão para iniciar")
label.pack(pady=20)

btn = ctk.CTkButton(app, text="Clique aqui",command=pegarInformacoes)
btn.pack(pady=20,padx=20)
app.mainloop()


