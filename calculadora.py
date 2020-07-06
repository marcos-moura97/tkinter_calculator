from tkinter import *
import tkinter.messagebox
from math import sin,cos,tan,sqrt,pi

calc = Tk()
calc.geometry("450x450")

calc_label = Label(calc,text="CALCULADORA",bg='dark gray',font=("Times", 30, "bold"))
calc_label.pack(side=TOP)
calc.config(background='Dark gray')

texto_entrada = StringVar()
operador=""

## Adiciona os botões
def click_botao(numero):
    global operador
    operador = operador+str(numero)
    texto_entrada.set(operador)

## Quando aperta igual, vamos a mágida
def botao_igual():
    global operador
    ## Se o primeiro algarismo for um operador que não devia estar lá, retorno uma mensagem de erro.
    # Exemplo: /2 em qualquer calculadora dá erro
    # Nesse caso aparece uma messagebox de erro e saio da função
    if operador[0] == '+' or operador[0] == '/' or operador[0] == '*' or operador[0] == '**':
        tkinter.messagebox.showerror('Operação inválida!','Eu sou uma calculadora burra pow. Não entendi o que quis dizer.')
        return

    add = str(eval(operador))
    texto_entrada.set(add)
    operador=""


## Quando apertar o botão CE, apaga tudo o que ta escrito, além da variável que guarda os valores
def botao_limpa():
    global  operador
    operador = ""
    texto_entrada.set("")

calc_texto = Entry(calc,font=("Courier New",12,'bold'),textvar= texto_entrada,width=25,bd=5,bg='powder blue')
calc_texto.pack()

################################################
#################### Botoes ####################
################################################

#### Números
b1 = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao(1),text='1',font=("Courier New",16,'bold'))
b1.place(x=10,y=100)

b2 = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao(2),text='2',font=("Courier New",16,'bold'))
b2.place(x=10,y=170)

b3 = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao(3),text='3',font=("Courier New",16,'bold'))
b3.place(x=10,y=240)

b4 = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao(4),text='4',font=("Courier New",16,'bold'))
b4.place(x=75,y=100)

b5 = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao(5),text='5',font=("Courier New",16,'bold'))
b5.place(x=75,y=170)

b6 = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao(6),text='6',font=("Courier New",16,'bold'))
b6.place(x=75,y=240)

b7 = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao(7),text='7',font=("Courier New",16,'bold'))
b7.place(x=140,y=100)

b8 = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao(8),text='8',font=("Courier New",16,'bold'))
b8.place(x=140,y=170)

b9 = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao(9),text='9',font=("Courier New",16,'bold'))
b9.place(x=140,y=240)

b0 = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao(0),text='0',font=("Courier New",16,'bold'))
b0.place(x=10,y=310)

#### Operadores básicos
bponto = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao("."),text='.',font=("Courier New",16,'bold'))
bponto.place(x=75,y=310)

bsoma = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao("+"),text='+',font=("Courier New",16,'bold'))
bsoma.place(x=205,y=100)

bmenos = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao("-"),text='-',font=("Courier New",16,'bold'))
bmenos.place(x=205,y=170)

bmult = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao("*"),text='x',font=("Courier New",16,'bold'))
bmult.place(x=205,y=240)

bdiv = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao("/"),text='/',font=("Courier New",16,'bold'))
bdiv.place(x=205,y=310)

bpar1 = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao("("),text='(',font=("Courier New",16,'bold'))
bpar1.place(x=270,y=100)

bpar1 = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao(")"),text=')',font=("Courier New",16,'bold'))
bpar1.place(x=345,y=100)


###### Trigonométria
bsin = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao("sin("),text='sen',font=("Courier New",16,'bold'))
bsin.place(x=335,y=170)

bcos = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao("cos("),text='cos',font=("Courier New",16,'bold'))
bcos.place(x=335,y=240)

btan = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao("tan("),text='tan',font=("Courier New",16,'bold'))
btan.place(x=335,y=310)

bpi = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao("pi"),text='π',font=("Courier New",16,'bold'))
bpi.place(x=270,y=170)


###### Quadrado e Potência
bquad = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao("**(2)"),text='^2',font=("Courier New",16,'bold'))
bquad.place(x=270,y=240)

braiz = Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:click_botao("sqrt("),text='√',font=("Courier New",16,'bold'))
braiz.place(x=270,y=310)

###### Limpa a Tela
blimpa = Button(calc,padx=14,pady=14,bd=4,bg='white',command=botao_limpa,text='CE',font=("Courier New",16,'bold'))
blimpa.place(x=140,y=310)

###### Igual
bigual = Button(calc,padx=130,pady=14,bd=4,bg='white',command=botao_igual,text='=',font=("Courier New",16,'bold'))
bigual.place(x=10,y=380)

calc.mainloop()
