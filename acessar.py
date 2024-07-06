import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk



def plot_data1():
    #  ler CSV file
    data = pd.read_csv('pandas/dados.csv')

    # Extrair data
    anos = data['ano']
    vendas = data['vendas']

    # Criar a figura
    fig, grafico = plt.subplots()
    grafico.plot(anos, vendas, marker='o', linestyle='-', color='b')


    # add as labels
    grafico.set_xlabel('Ano')
    grafico.set_ylabel('Meses')
    grafico.set_title('Vendas Anuais')

    # mostrar o grafico
    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


def plot_data2():
    #  ler CSV file
    data = pd.read_csv('pandas/dados.csv')

    # Extrair data
    anos = data['ano']
    vendas = data['vendas']

    # Criar a figura
    fig, grafico = plt.subplots()
    grafico.bar(anos, vendas, color='b')


    # add as labels
    grafico.set_xlabel('Ano')
    grafico.set_ylabel('Meses')
    grafico.set_title('Vendas Anuais')

    # mostrar o grafico
    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


def plot_data3():
    #  ler CSV file
    data = pd.read_csv('pandas/dados.csv')

    # Extrair data
    anos = data['ano']
    vendas = data['vendas']

    # Criar a figura
    fig, grafico = plt.subplots()
    grafico.pie(vendas, labels = anos, autopct='%.2f')


    # add as labels
    grafico.set_xlabel('Ano')
    grafico.set_ylabel('Meses')
    grafico.set_title('Vendas Anuais')

    # mostrar o grafico
    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True) 

def  ESTATISTICA():
     data = pd.read_csv('pandas/dados.csv')
     anos = data['ano']
     vendas = data['vendas']     
     moda  = np.mean(vendas)
     mediana = np.median(vendas)
     media  =  np.var(vendas)
     desvio = np.std(vendas)
     mostrar_sta.config(text = f'''
                        MODA - {moda}
                        MEDIA -  {media}
                        MEDIANA {mediana}
                        DESVIO PADRÃO{desvio}
                                ''')

    




# janela tkinter
janela = tk.Tk()
janela.title('Gráfico de Vendas')

# button
botao = tk.Button(janela, text='Gráfico de linhas', command=plot_data1)
botao.pack(padx = 10, pady=10)

botao = tk.Button(janela, text='Gráfico de barras', command=plot_data2)
botao.pack(padx = 20, pady=10)

botao = tk.Button(janela, text='Gráfico Pizza', command=plot_data3)
botao.pack(padx = 25, pady=10)

btn_estatistica =  tk.Button(janela, text='Estatistica', command=ESTATISTICA)
btn_estatistica.pack(padx = 30, pady=10)

mostrar_sta = tk.Label(janela, text = '', bg='black', fg='white')
mostrar_sta.pack(pady=10)


# loop tkinter
janela.mainloop()



























# import pandas as pd
# import matplotlib.pyplot as plt
# import tkinter as tk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# def mostrar():
#     notas  = medias
#     nome = nomes
#     label_mostrar.config(text=f'Nomes:{nome}')
#     label2_mostrar.config(text=f'Notas:{notas}')
    


# j = tk.Tk()
# j.title('DADOS')


# dados  =  pd.read_json('pandas/alunos.json')

# lista  =  []
# n = dados['alunos']
# medias = []
# nomes = []
# medias.append(n[0]['Media'])
# medias.append(n[1]['Media'])
# nomes.append(n[0]['Nome'])
# nomes.append(n[1]['Nome'])
# print( 'Medias: ', medias )
# print('Nomes:', nomes)
# # plt.bar(nomes,medias)

# # plt.show()

# btn = tk.Button(j,text='Clique aqui', command = mostrar )
# # btn.pack()

# label_mostrar =  tk.Label(j, text='')
# label_mostrar.pack()

# label2_mostrar =  tk.Label(j, text='')
# label2_mostrar.pack()



# j.mainloop()


