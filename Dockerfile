# Usando uma imagem base do Python
FROM python:3.12

# Definindo o diretório de trabalho no container
WORKDIR /.

# Copiando todos os arquivos do diretório atual para o diretório de trabalho do container
COPY . .

# Instalando as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Expondo a porta 8888
EXPOSE 8888

# Definindo o comando para rodar o Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
