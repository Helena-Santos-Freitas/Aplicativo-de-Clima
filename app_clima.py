import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from datetime import datetime
from io import BytesIO

API_KEY = '494451670fc619f5935f20d6a0264cdd'

def buscar_clima(event=None):
    cidade = entrada_cidade.get()
    if not cidade:
        messagebox.showwarning("Atenção", "Digite o nome de uma cidade.")
        return

    url_atual = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt&units=metric'
    url_previsao = f'https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={API_KEY}&lang=pt&units=metric'

    try:
        resposta_atual = requests.get(url_atual, timeout=10)
        resposta_previsao = requests.get(url_previsao, timeout=10)

        if resposta_atual.status_code == 200 and resposta_previsao.status_code == 200:
            dados_atual = resposta_atual.json()
            dados_previsao = resposta_previsao.json()

            nome = dados_atual.get('name', cidade)
            temp_atual = dados_atual['main']['temp']
            desc_atual = dados_atual['weather'][0]['description'].capitalize()
            icone_atual = dados_atual['weather'][0]['icon']

            # Baixar e exibir o ícone do clima atual
            url_icone = f"http://openweathermap.org/img/wn/{icone_atual}@2x.png"
            print("URL do ícone:", url_icone)  # Adicione esta linha para depurar
            try:
                resposta_icone = requests.get(url_icone, timeout=5)
                imagem_icone = Image.open(BytesIO(resposta_icone.content))
                imagem_icone = imagem_icone.resize((60, 60), Image.LANCZOS)
                icone_tk = ImageTk.PhotoImage(imagem_icone)
                label_icone.config(image=icone_tk)
                label_icone.image = icone_tk
            except Exception as erro:
                print("Erro ao carregar ícone:", erro)  # Adicione esta linha para depurar
                label_icone.config(image='')
                label_icone.image = None

            texto_previsao = ""
            for previsao in dados_previsao['list'][:5]:
                dt_txt = previsao['dt_txt']
                temp = previsao['main']['temp']
                desc = previsao['weather'][0]['description'].capitalize()
                hora = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S').strftime('%d/%m %H:%M')
                texto_previsao += f"{hora}: {desc}, {temp}°C\n"

            resultado['text'] = (
                f"Clima atual em {nome}:\n{desc_atual}\nTemperatura: {temp_atual}°C\n\n"
                f"Próximas previsões (a cada 3 horas):\n{texto_previsao}"
            )
            entrada_cidade.delete(0, tk.END)  # Limpa o campo de entrada

        else:
            try:
                dados_atual = resposta_atual.json()
                mensagem_erro = dados_atual.get('message', 'Cidade não encontrada.')
            except Exception:
                mensagem_erro = 'Erro desconhecido.'
            resultado['text'] = f"Erro: {mensagem_erro.capitalize()}"
            label_icone.config(image='')
            label_icone.image = None

    except requests.exceptions.Timeout:
        resultado['text'] = "Erro: Tempo de resposta excedido."
        label_icone.config(image='')
        label_icone.image = None
    except requests.exceptions.ConnectionError:
        resultado['text'] = "Erro: Sem conexão com a internet."
        label_icone.config(image='')
        label_icone.image = None
    except Exception as e:
        resultado['text'] = f"Erro ao buscar dados: {e}"
        label_icone.config(image='')
        label_icone.image = None

# Interface Tkinter
janela = tk.Tk()
janela.title("App de Clima")
janela.geometry("400x500")
janela.configure(bg="#e0f7fa")

tk.Label(janela, text="Digite a cidade:", bg="#e0f7fa", font=("Arial", 12)).pack(pady=10)
entrada_cidade = tk.Entry(janela, font=("Arial", 12))
entrada_cidade.pack()
entrada_cidade.bind("<Return>", buscar_clima)  # Permite buscar com Enter

btn_buscar = tk.Button(janela, text="Buscar Clima", command=buscar_clima, bg="#0288d1", fg="white", font=("Arial", 12))
btn_buscar.pack(pady=10)

label_icone = tk.Label(janela, bg="#e0f7fa")
label_icone.pack(pady=5)

resultado = tk.Label(janela, text="", bg="#e0f7fa", font=("Arial", 12), wraplength=380, justify="center")
resultado.pack(pady=20)

janela.mainloop()