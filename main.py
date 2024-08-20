###################################################################################################################################################################
# Código escrito por Tefim04
###################################################################################################################################################################

# Importando tkinter
from tkinter import *
from tkinter import ttk
from datetime import datetime

# Criando cores
cor_1 = '#3b3b3b' # preto
cor_2 = '#feffff' # branco
cor_3 = '#38576b' # azul carregado
cor_4 = '#ECEFF1' # cizenta
cor_5 = '#FFAB40' # laranja

# Função para atualizar data e hora
def atualizar_data_hora():
    agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    data_hora_label.config(text=agora)
    data_hora_label.after(1000, atualizar_data_hora)  # Atualiza a cada 1 segundo

# Criando janela
janela = Tk()
janela.title('Calculadora do Herói')
janela.geometry('280x310')
janela.config(bg=cor_1)

# Criando Frame
frame_tela = Frame(janela, width=280, height=50, bg=cor_3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=280, height=268)
frame_corpo.grid(row=1, column=0)

# Criando Label para o display
app_label = Label(frame_tela, text='123456789', width=16, height=2, padx=4, relief=FLAT, anchor="e", justify=RIGHT, font='Ivy 22', bg=cor_3, fg=cor_2)
app_label.place(x=0, y=0)

# Criando Label para data e hora
data_hora_label = Label(frame_tela, text='', font=('Ivy 8'), bg=cor_3, fg=cor_2, anchor='w', padx=5)
data_hora_label.place(x=5, y=30)  # Posiciona a data e hora na parte inferior esquerda

# Atualiza data e hora
atualizar_data_hora()

# Criando botões
b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%", width=8, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_corpo, text="/", width=6, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=210, y=0)

b_4 = Button(frame_corpo, text="7", width=6, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, text="8", width=6, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=70, y=52)
b_6 = Button(frame_corpo, text="9", width=6, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=140, y=52)
b_7 = Button(frame_corpo, text="*", width=6, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=210, y=52)

b_8 = Button(frame_corpo, text="4", width=6, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, text="5", width=6, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=70, y=104)
b_10 = Button(frame_corpo, text="6", width=6, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=140, y=104)
b_11 = Button(frame_corpo, text="-", width=6, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=210, y=104)

b_12 = Button(frame_corpo, text="1", width=6, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, text="2", width=6, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=70, y=156)
b_14 = Button(frame_corpo, text="3", width=6, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=140, y=156)
b_15 = Button(frame_corpo, text="+", width=6, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=210, y=156)

b_16 = Button(frame_corpo, text="0", width=11, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, text=".", width=8, height=2, bg=cor_4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=208)
b_18 = Button(frame_corpo, text="=", width=6, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=210, y=208)

# Executa o loop principal do Tkinter
janela.mainloop()

###################################################################################################################################################################
# Fim do código escrito por Tefim04
###################################################################################################################################################################
