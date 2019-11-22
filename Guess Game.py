# coding=utf-8
from tkinter import *
from tkinter import messagebox as msg
from tkinter import font
import random as r



# Lista para salvar as jogadas anteriores
jogadas = []
# Lista para salvar as distâncias
sup = []
# Variável utilizada na montagem dos números que já foram chutados
temp = ''
# Número sorteado
sorteado = r.randint(1, 101)


# Function Creation
# ----------------------------------------------------------------------------------------------------
def resetar():
    # Função para resetar o jogo
    global jogadas, sorteado, temp, sup
    temp = ''
    sorteado = r.randint(1, 101)
    jogadas = []
    sup = []
    dica.set('')
    usados.set('')
# ----------------------------------------------------------------------------------------------------


def no_intervalo(n):
    # Função para verificar se o número está no intervalo certo.
    n = int(n)
    if 1 <= n <= 100:
        return True
    else:
        return False
# ----------------------------------------------------------------------------------------------------


def distancia(n1, n2):
    # Calcular a distância entre o chute e o nº sorteado
    global dist
    if n1 > n2:
        dist = n1 - n2
    else:
        dist = n2 - n1
    return dist
# ----------------------------------------------------------------------------------------------------


def situation_1(d):
    # Faz a primeira checagem da distância entre os Nºs
    # Retornará um tuple para ajudar na utilização da 2º função
    if 1 <= d <= 2:
        return 'Está Fervendo !!!', 1
    elif d == 3:
        return 'Está Muito Quente !!!', 2
    elif 3 < d < 6:
        return 'Está quente', 3
    elif 6 <= d <= 7:
        return 'Está Morno', 4
    elif 7 < d <= 9:
        return 'Está Frio', 5
    elif 10 <= d <= 12:
        return 'Está Muito Frio !!!', 6
    elif d > 12:
        return 'Está Congelando !!!', 7
# ----------------------------------------------------------------------------------------------------


def situation_2(d, p1, bol):
    # Diz se está mais próximo ou distante do Nº sorteado
    # Primeiro verifica a nova distância e depois compara com a situação anterior
    if 1 <= d <= 2:
        p2 = 1
        if p2 == p1:
            if bol == 1:
                return 'Continua Fervendo. Mas Esfriou Um Pouco', 1
            elif bol == 2:
                return 'Continua Fervendo. Mas Esquentou Um Pouco', 1
            else:
                return 'Continua Fervendo.', 1
        else:
            t = p1 - p2
            if t == 1:
                return 'Esquentou mais um pouco. Agora Fervendo!!!', 1
            elif t == 2:
                return 'Esquentou mais um pouco. Agora Fervendo!!!', 1
            elif t == 3:
                return 'Esquentou mais. Agora Fervendo!!!', 1
            elif t == 4:
                return 'Um Bom Chute. Agora Fervendo', 1
            elif t == 5:
                return 'Esquentou bastante. Agora Fervendo!!!', 1
            elif t == 6:
                return 'Descongelou Legal. Está Fervendo!!', 1
    # ----------------------------------------------------------------------------------------------------
    elif d == 3:
        p2 = 2
        if p2 == p1:
            if bol == 1:
                return 'Continua Muito Quente. Mas Esfriou Um Pouco', 2
            elif bol == 2:
                return 'Continua Muito Quente. Mas Esquentou Um Pouco', 2
            else:
                return 'Continua Muito Quente. Mas Esquentou Um Pouco', 2
        else:
            t = p1 - p2
            if t == -1:
                return 'Esfriou Bem Pouco. Ainda Muito Quente.', 2
            elif t == 1:
                return 'Esquentou. Agora Ficou Muito Quente', 2
            elif t == 2:
                return 'Teve Uma Esquentada Considerável. Agora Muito Quente', 2
            elif t == 3:
                return 'Opa. Ficou Muito Quente', 2
            elif t == 4:
                return 'Esquentou Bastante. Agora Muito Quente', 2
            elif t == 5:
                return 'Está No Caminho Certo. Ficou Muito Quente', 2
    # ----------------------------------------------------------------------------------------------------
    elif 3 < d < 6:
        p2 = 3
        if p2 == p1:
            if bol == 1:
                return 'Continua Quente. Mas Esfriou Um Pouco', 3
            elif bol == 2:
                return 'Continua Quente. Mas Esquentou Um Pouco', 3
            else:
                return 'Continua Quente', 3
        else:
            t = p1 - p2
            if t == -2:
                return 'Volte Atrás!! Esfriou E Agora Está Quente', 3
            elif t == -1:
                return 'Leve Esfriada, Ainda Quente', 3
            elif t == 1:
                return 'Leve Esquentada. Agora Ficou Quente', 3
            elif t == 2:
                return 'Melhorando. Quente Agora', 3
            elif t == 3:
                return 'Tá No Caminho Certo. Encontra-se Quente Agora', 3
            elif t == 4:
                return 'Descongelou Consideravelmente, Agora Está Quente', 3
    # ----------------------------------------------------------------------------------------------------
    elif 6 <= d <= 7:
        p2 = 4
        if p2 == p1:
            if bol == 1:
                return 'Continua Morno. Mas Esfriou Um Pouco', 4
            elif bol == 2:
                return 'Continua Morno. Mas Esquentou Um Pouco', 4
            else:
                return 'Continua Morno.', 4
        else:
            t = p1 - p2
            if t == -3:
                return 'Esfriou Bastante. Agora Ficou Morno.', 4
            elif t == -2:
                return 'Deu Uma Esfriada Está Apenas Morno.', 4
            elif t == -1:
                return 'Antes Quente. Agora Morno.', 4
            elif t == 1:
                return 'Esquentou Um Pouco. Morno Agora.', 4
            elif t == 2:
                return 'Deu Uma Esquentada. Agora Morno.', 4
            elif t == 3:
                return 'Descongelou Um Pouco. Agora Morno.', 4
    # ----------------------------------------------------------------------------------------------------
    elif 7 < d <= 9:
        p2 = 5
        if p2 == p1:
            if bol == 1:
                return 'Continua Frio. Mas Esfriou Um Pouco', 5
            elif bol == 2:
                return 'Continua Frio. Mas Esquentou Um Pouco', 5
            else:
                return 'Continua Frio.', 5
        else:
            t = p1 - p2
            if t == -4:
                return 'Esfriou. Ficou Frio Agora', 5
            elif t == -3:
                return 'Deu Uma Esfriada. Ficou Frio', 5
            elif t == -2:
                return 'Agora Ficou Frio', 5
            elif t == -1:
                return 'Uma Pequena Esfriada. Ficou Frio', 5
            elif t == 1:
                return 'Leve Melhorada Ficou Frio', 5
            elif t == 2:
                return 'Esse É O Caminho. Ficou Frio Agora', 5
    # ----------------------------------------------------------------------------------------------------
    elif 10 <= d <= 12:
        p2 = 6
        if p2 == p1:
            if bol == 1:
                return 'Continua Muito Frio. Mas Esfriou Um Pouco', 6
            elif bol == 2:
                return 'Continua Muito Frio. Mas Esquentou Um Pouco', 6
            else:
                return 'Continua Muito Frio. Mas Esquentou Um Pouco', 6
        else:
            t = p1 - p2
            if t == -5:
                return 'Cuidado. Ficou Muito Frio.', 6
            elif t == -4:
                return 'Esfriou Bastante. Agora Ficou Muito Frio', 6
            elif t == -3:
                return 'Esfriou... Muito Frio', 6
            elif t == -2:
                return 'Agora Ficou Muito Frio', 6
            elif t == -1:
                return 'Leve Esfriada... Ficou Muito Frio', 6
            elif t == 1:
                return 'Descongelou Quase Nada. Ainda Muito Frio', 6
    # ----------------------------------------------------------------------------------------------------
    elif d > 12:
        p2 = 7
        if p2 == p1:
            if bol == 1:
                return 'Continua Congelando. Mas Esfriou Um Pouco', 7
            elif bol ==2:
                return 'Continua Congelando. Mas Esquentou Um Pouco', 7
            else:
                return 'Continua Congelando.', 7
        else:
            t = p1 - p2
            if t == -6:
                return 'Opa Volte Atrás! Agora Está Congelando', 7
            elif t == -5:
                return 'Esfriou Tanto Que Congelou', 7
            elif t == -4:
                return 'Esfriou Muito. Está Congelado', 7
            elif t == -3:
                return 'Deu Uma Esfriada. Agora Está Congelado', 7
            elif t == -2:
                return 'Esfriou... Agora Está Congelado', 7
            elif t == -1:
                return 'Leve Esfriada. Agora Está Congelado', 7
# ----------------------------------------------------------------------------------------------------


def existe(p=0, lst=[]):
    # Verifica se o palpite já foi feito anteriormente
    if p in lst:
        return True
    else:
        return False
# ----------------------------------------------------------------------------------------------------


def chute(c=0):
    # Função principal que analisa o chute
    # ----------------------------------------------------------------------------------------------------
    # Limpa o visor de Dicas
    dica.set('')
    # Pega o N° chutado pelo jogador
    global palpite, jogadas, temp, sorteado, tela, j, sup
    palpite = info_2.get()
    info_2.delete(0, END)
    # ----------------------------------------------------------------------------------------------------
    # Ter certeza que só inteiros serão aceitos
    try:
        int(palpite)
        # Verifica se o palpite não está acima de 100
        if not no_intervalo(int(palpite)):
            msg.showerror('Error', 'Você colocou um número acima de 100\ntente outro')
            return
    except ValueError:
        # Se o jogador esquecer de digitar
        if len(palpite) == 0:
            msg.showerror('Error', 'Você Esqueceu de Digitar')
        # Se o jogador colocar string ao invés de inteiro
        else:
            msg.showerror('Error', 'Entrada Inválida!!!')
        return
    # ----------------------------------------------------------------------------------------------------
    if int(palpite) == sorteado:
        msg.showinfo('Parabéns!!!', 'Você acertou o número sorteado!!!')
        # Pergunta se o jogador quer jogar de novo
        if msg.askyesno('Guess Game', 'Quer continuar jogando'):
            jogadas = []
            sup = []
            dica.set('')
            usados.set('')
            temp = ''
            sorteado = r.randint(1, 101)
            return
        else:
            # Fecha o aplicativo
            tela.destroy()
            return
    # ----------------------------------------------------------------------------------------------------
    # Verifica se o palpite já existe
    elif existe(palpite, jogadas):
            msg.showinfo('Tente Outro', 'Você já fez esse palpite anteriormente!!!')
            return
    # Adiciona o novo palpite e informa a situação
    # ----------------------------------------------------------------------------------------------------
    else:
        d_ = distancia(int(palpite), sorteado)
        sup.append(d_)
        jogadas.append(palpite)
        # Lógica para a primeira jogada
        if len(jogadas) == 1:
            tip, j = situation_1(d_)
            dica.set(tip)
        # Lógica para a segunda jogada em diante
        # ----------------------------------------------------------------------------------------------------
        else:
            if d_ > sup[-2]:
                tip, k = situation_2(d_, j, 1)
            elif d_ < sup[-2]:
                tip, k = situation_2(d_, j, 2)
            else:
                tip, k = situation_2(d_, j, 3)
            dica.set(tip)
            j = k
        if len(temp) == 0:
            temp = jogadas[-1]
        elif len(jogadas) > 9:
            # Quando esgota o número de tentativas
            # ----------------------------------------------------------------------------------------------------
            # Dizendo o desempenho no jogo
            y = min(sup)
            indice = sup.index(y)
            melhor_jogada = jogadas[indice]
            # Pop up para dizer o desempenho do jogador
            msg.showinfo('Que Pena', 'Seu melhor chute foi ' + str(melhor_jogada) + '\no n° sorteado era: ' + str(sorteado))
            if msg.askyesno('Fim de Linha!', 'Você não conseguiu acertar!\nQuer jogar de novo?'):
                jogadas = []
                sup = []
                dica.set('')
                usados.set('')
                temp = ''
                sorteado = r.randint(1, 101)
            else:
                tela.destroy()
        else:
            temp = temp + ' - ' + jogadas[-1]
        usados.set(temp)
# ----------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------


# Criação da interface
tela = Tk()
tela.title('Guess Game')
# ----------------------------------------------------------------------------------------------------

# Gerando as Frames
frame1 = Frame(tela)
frame2 = Frame(tela)
frame3 = Frame(tela)
frame4 = Frame(tela)
frame5 = Frame(tela)
# ----------------------------------------------------------------------------------------------------

# Packing all the frames
frame1.pack(fill=BOTH)
frame2.pack(fill=BOTH)
frame3.pack(fill=BOTH)
frame4.pack(fill=BOTH)
frame5.pack(fill=BOTH)
# ----------------------------------------------------------------------------------------------------

titulo = Label(frame1, text='Guess Game', font=('Comic Sans MS', 20, 'bold')
               , relief=RAISED, bg='#3737FF',  fg='white', bd=18)
titulo.pack(fill=BOTH)
sublinhar = font.Font(titulo, titulo.cget('font'))
sublinhar.configure(underline=True)
titulo.configure(font=sublinhar)
# ----------------------------------------------------------------------------------------------------

info_1 = Label(frame2, text=2*' ' + '↓ Chute Aqui ↓ ' + 15*' '+ '|' + 6*'---' + ' '
               'Palpites ' + 6*'---' + '|', font=('Palatino Linotype', 14),
               bg='#3737FF', anchor='w', fg='white')
info_1.pack(fill=BOTH)
# ----------------------------------------------------------------------------------------------------

info_2 = Entry(frame3, font=('Comic Sans MS', 15, 'bold'), bg='yellow',
               fg='black', bd=30, width=8, justify=CENTER
               )
info_2.bind('<Return>', chute)
info_2.pack(side=LEFT, fill=BOTH)
# ----------------------------------------------------------------------------------------------------

usados = StringVar()
utilizados = Label(frame3, textvariable=usados,
                   font=('Palatino Linotype', 15, 'bold'), fg='#FFFF2B', anchor='c',
                   bg='#3737FF', relief=SUNKEN, bd=10)
utilizados.pack(fill=BOTH)
# ----------------------------------------------------------------------------------------------------

info_3 = Label(frame4, text='Dica →', font=('Palatino Linotype', 15),
               bg='#3737FF', fg='white', width=10)
info_3.pack(fill=BOTH, side=LEFT)
# ----------------------------------------------------------------------------------------------------

dica = StringVar()
dicas = Label(frame4, textvariable=dica, font=('Palatino Linotype', 15, 'bold')
              , bd=20, relief=SUNKEN, bg='#3737FF', fg='white',
              anchor='c', justify=LEFT)
dicas.pack(fill=BOTH)
# ----------------------------------------------------------------------------------------------------

checar = Button(frame3, text='Chutar', command=lambda: chute(), bd=5,
                fg='yellow', bg='#3737FF', width=18,
                font=('Palatino Linotype', 15, 'bold'))
checar.pack(side=LEFT, fill=Y)
# ----------------------------------------------------------------------------------------------------

resetar = Button(frame3, text='Reset', command=resetar
                 , bd=5, fg='yellow', bg='#3737FF',
                 width=18, font=('Palatino Linotype', 15, 'bold'))
resetar.pack(fill=Y, side=LEFT)
# ----------------------------------------------------------------------------------------------------


regras = Label(frame5, text=50*' '+ 'Regras:\n'  '→ Você tem 10 tentativas '
                'para acertar ' 'um' ' número entre (1-100);\n' '→ Receberá dicas '
                'se está perto ou longe;'  '\n→ Não poderá repetir N°s que '
                'já foram chutados;', font=('Palatino Linotype', 15, 'bold'),
               justify=LEFT,  bg='yellow', bd=10, fg='black', anchor='w',
               relief=SUNKEN)
regras.pack(fill=BOTH)
# ----------------------------------------------------------------------------------------------------

# End
tela.resizable(width=False, height=False)
tela.mainloop()

