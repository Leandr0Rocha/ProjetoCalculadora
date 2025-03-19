from tkinter import Tk, Entry, Button, StringVar
import math

class Calculadora:
    def __init__(self, master):
        master.title('Calculadora')
        master.geometry('400x650+0+0')
        master.config(bg='light cyan')
        master.resizable(False, False)

        self.equacao = StringVar()
        self.valor_entrada = ''
        Entry(width=23, border=5, font=('Cambria', 20), textvariable=self.equacao).place(x=20, y=10)

        # Espaçamento entre os botões
        espaco_x = 20
        espaco_y = 20
        largura_botao = 80
        altura_botao = 80

        # Primeira linha de botões
        Button(width=11, height=4, text='±', relief='flat', bg='white', command=self.negativo).place(x=espaco_x, y=70)
        Button(width=11, height=4, text='1/x', relief='flat', bg='white', command=self.fraçao).place(x=espaco_x + largura_botao + espaco_x, y=70)
        Button(width=11, height=4, text='x²', relief='flat', bg='white', command=self.potencia).place(x=espaco_x + 2 * (largura_botao + espaco_x), y=70)
        Button(width=11, height=4, text='√', relief='flat', bg='white', command=self.raiz).place(x=espaco_x + 3 * (largura_botao + espaco_x), y=70)

        # Segunda linha de botões
        Button(width=11, height=4, text='C', relief='flat', bg='snow3', command=self.limpar).place(x=espaco_x, y=70 + altura_botao + espaco_y)
        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.mostrar('(')).place(x=espaco_x + largura_botao + espaco_x, y=70 + altura_botao + espaco_y)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.mostrar(')')).place(x=espaco_x + 2 * (largura_botao + espaco_x), y=70 + altura_botao + espaco_y)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.mostrar('%')).place(x=espaco_x + 3 * (largura_botao + espaco_x), y=70 + altura_botao + espaco_y)

        # Terceira linha de botões
        Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.mostrar('7')).place(x=espaco_x, y=70 + 2 * (altura_botao + espaco_y))
        Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.mostrar('8')).place(x=espaco_x + largura_botao + espaco_x, y=70 + 2 * (altura_botao + espaco_y))
        Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.mostrar('9')).place(x=espaco_x + 2 * (largura_botao + espaco_x), y=70 + 2 * (altura_botao + espaco_y))
        Button(width=11, height=4, text='*', relief='flat', bg='white', command=lambda: self.mostrar('*')).place(x=espaco_x + 3 * (largura_botao + espaco_x), y=70 + 2 * (altura_botao + espaco_y))

        # Quarta linha de botões
        Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.mostrar('4')).place(x=espaco_x, y=70 + 3 * (altura_botao + espaco_y))
        Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.mostrar('5')).place(x=espaco_x + largura_botao + espaco_x, y=70 + 3 * (altura_botao + espaco_y))
        Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.mostrar('6')).place(x=espaco_x + 2 * (largura_botao + espaco_x), y=70 + 3 * (altura_botao + espaco_y))
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.mostrar('-')).place(x=espaco_x + 3 * (largura_botao + espaco_x), y=70 + 3 * (altura_botao + espaco_y))

        # Quinta linha de botões
        Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.mostrar('1')).place(x=espaco_x, y=70 + 4 * (altura_botao + espaco_y))
        Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.mostrar('2')).place(x=espaco_x + largura_botao + espaco_x, y=70 + 4 * (altura_botao + espaco_y))
        Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.mostrar('3')).place(x=espaco_x + 2 * (largura_botao + espaco_x), y=70 + 4 * (altura_botao + espaco_y))
        Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.mostrar('+')).place(x=espaco_x + 3 * (largura_botao + espaco_x), y=70 + 4 * (altura_botao + espaco_y))

        # Sexta linha de botões
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.mostrar('.')).place(x=espaco_x, y=70 + 5 * (altura_botao + espaco_y))
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.mostrar('0')).place(x=espaco_x + largura_botao + espaco_x, y=70 + 5 * (altura_botao + espaco_y))
        Button(width=11, height=4, text='=', relief='flat', bg='steel blue', command=self.calcular).place(x=espaco_x + 2 * (largura_botao + espaco_x), y=70 + 5 * (altura_botao + espaco_y))

    def mostrar(self, valor):
        'Mostra o valor do botão na tela'
        self.valor_entrada += str(valor)
        self.equacao.set(self.valor_entrada)

    def limpar(self):
        'Limpa a tela'
        self.valor_entrada = ''
        self.equacao.set('')

    def limpar_entrada(self):
        'Limpa apenas a entrada atual'
        self.valor_entrada = self.valor_entrada[:-1]
        self.equacao.set(self.valor_entrada)

    def calcular(self):
        'Calcula a expressão matemática'
        try:
            resultado = str(eval(self.valor_entrada))
            self.equacao.set(resultado)
        except:
            self.equacao.set('ERRO')
            self.valor_entrada = ''

    def negativo(self):
        'Transforma o número atual em negativo ou positivo'
        if self.valor_entrada:
            if self.valor_entrada.startswith('-'):
                self.valor_entrada = self.valor_entrada[1:]
            else:
                self.valor_entrada = '-' + self.valor_entrada
            self.equacao.set(self.valor_entrada)

    def fraçao(self):
        'Calcula o inverso do número atual'
        try:
            resultado = str(1 / eval(self.valor_entrada))
            self.equacao.set(resultado)
            self.valor_entrada = resultado
        except:
            self.equacao.set('ERRO')

    def potencia(self):
        'Calcula o quadrado do número atual'
        try:
            resultado = str(eval(self.valor_entrada) ** 2)
            self.equacao.set(resultado)
            self.valor_entrada = resultado
        except:
            self.equacao.set('ERRO')

    def raiz(self):
        'Calcula a raiz quadrada do número atual'
        try:
            resultado = str(math.sqrt(eval(self.valor_entrada)))
            self.equacao.set(resultado)
            self.valor_entrada = resultado
        except:
            self.equacao.set('ERRO')

raiz = Tk()
Calculadora(raiz)
raiz.mainloop()