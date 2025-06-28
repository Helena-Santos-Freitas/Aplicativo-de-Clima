# App de Clima com Tkinter e OpenWeatherMap

## Descrição

Este aplicativo de clima exibe informações meteorológicas de forma simples e clara. A interface mostra:

- O nome da cidade,
- A temperatura atual,
- Uma descrição do clima (ex: "Nublado"),
- O ícone representando o clima atual,
- E as próximas previsões (a cada 3 horas) com temperatura e descrição.

Além disso, o código trata possíveis erros, como cidade não encontrada, falta de conexão à internet ou timeout na requisição, garantindo uma boa experiência para o usuário.

## Funcionalidades

- Consulta do clima atual de qualquer cidade do mundo.
- Exibição da temperatura, descrição e ícone do clima atual.
- Mostra a previsão do tempo para as próximas horas (a cada 3 horas).
- Tratamento de erros para entrada inválida, problemas de conexão e timeout.

## Pré-requisitos

- Python 3.x
- Bibliotecas Python:
  - `tkinter` (normalmente já vem com Python)
  - `requests`
  - `Pillow` (PIL)

## Instalação

1. Clone este repositório ou copie o código.
2. Instale as dependências com pip:

```bash
pip install requests Pillow
