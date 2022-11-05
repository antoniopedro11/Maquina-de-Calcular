# António Velez nº18390 - Qualidade de Software

# comandos para importar o tkinter
from tkinter import *
from tkinter import ttk

# cores da calculadora
corAzul= "#719beb" # cor azul
corCinza = "#D9D9D9" # cor cinza
corBranca = "#f5f5f5" # cor branca

# Janela da calculadora
janela = Tk()
janela.title("Máquina de Calcular - António Velez")
janela.geometry("235x302")
janela.config(bg=corAzul)

# Frame do Cabeçalho de cima da calculadora
frame_tela = Frame(janela, width= 235, height=50, bg=corAzul)
frame_tela.grid(row=0, column=0)

# Frame de Corpo da calculadora
frame_corpo = Frame(janela, width= 235, height=268)
frame_corpo.grid(row=1, column=0)

# variaveis
todos_valores = ''
valor_texto = StringVar()
# funcao entrada de valores 
def input_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    # Passando o valor para a tela
    valor_texto.set(todos_valores) 

# Função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores) 
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)

# Função limpar tela 
def limpar():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


# Label do input da calculadora
app_label = Label(frame_tela, textvariable=valor_texto,width=16,height=2,padx=7,relief=FLAT,anchor="e",justify=RIGHT,font=('Ivy 18'),bg=corAzul,fg=corBranca)
app_label.place (x=0,y=0)    

# Botoes da calculadora
buttonApagar = Button(frame_corpo,command=limpar, text="APAGAR", width=11, height=2, bg=corCinza,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonApagar.place(x=0,y=0)
button2 = Button(frame_corpo, command= lambda: input_valores('%'), text="%", width=5, height=2, bg=corCinza,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button2.place(x=118,y=0)
buttonDividir = Button(frame_corpo, command= lambda: input_valores('/'), text="/", width=5, height=2,bg=corAzul,fg=corBranca,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonDividir.place(x=177,y=0)

button4 = Button(frame_corpo,command= lambda: input_valores('7'), text="7", width=5, height=2, bg=corCinza,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button4.place(x=0,y=52)
button5 = Button(frame_corpo,command= lambda: input_valores('8'), text="8", width=5, height=2, bg=corCinza,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button5.place(x=59,y=52)
button6 = Button(frame_corpo,command= lambda: input_valores('9'), text="9", width=5, height=2, bg=corCinza,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button6.place(x=118,y=52)
buttonMultiplicar = Button(frame_corpo,command= lambda: input_valores('*'), text="*", width=5, height=2,bg=corAzul,fg=corBranca,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonMultiplicar.place(x=177,y=52)

button7 = Button(frame_corpo,command= lambda: input_valores('4'), text="4", width=5, height=2, bg=corCinza,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button7.place(x=0,y=102)
button8 = Button(frame_corpo,command= lambda: input_valores('5'), text="5", width=5, height=2, bg=corCinza,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button8.place(x=59,y=102)
button9 = Button(frame_corpo,command= lambda: input_valores('6'), text="6", width=5, height=2, bg=corCinza,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button9.place(x=118,y=102)
buttonSubtrair = Button(frame_corpo,command= lambda: input_valores('-'), text="-", width=5, height=2,bg=corAzul,fg=corBranca,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonSubtrair.place(x=177,y=102)

button10 = Button(frame_corpo,command= lambda: input_valores('1'), text="1", width=5, height=2, bg=corCinza,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button10.place(x=0,y=152)
button11 = Button(frame_corpo,command= lambda: input_valores('2'), text="2", width=5, height=2, bg=corCinza,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button11.place(x=59,y=152)
button12 = Button(frame_corpo,command= lambda: input_valores('3'), text="3", width=5, height=2, bg=corCinza,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button12.place(x=118,y=152)
buttonSomar = Button(frame_corpo,command= lambda: input_valores('+'), text="+", width=5, height=2,bg=corAzul,fg=corBranca,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonSomar.place(x=177,y=152)

button13 = Button(frame_corpo,command= lambda: input_valores('0'), text="0", width=11, height=2, bg=corCinza,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button13.place(x=0,y=205)
button14 = Button(frame_corpo,command= lambda: input_valores('.'), text=".", width=5, height=2, bg=corCinza,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button14.place(x=118,y=204)
buttonResultado = Button(frame_corpo,command= calcular, text="=", width=5, height=2,bg=corAzul,fg=corBranca,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonResultado.place(x=177,y=204)

janela.mainloop()
