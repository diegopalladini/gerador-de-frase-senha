from flask import Flask, render_template, request
import secrets

app = Flask(__name__)


def carregar_palavras():
    lista = []
    with open('palavras.txt', 'r', encoding='utf-8') as f:
        for linha in f.readlines():
            palavra_limpa = linha.strip()
            if palavra_limpa:
                lista.append(palavra_limpa)  
    return lista

PALAVRAS = carregar_palavras()  # Função para carregar palavras de um arquivo ou definir uma lista fixa


def gerar_frase(qtd=4):
    if len(PALAVRAS) < qtd:
        raise ValueError("A quantidade de palavras solicitada é maior do que a lista disponível.")
    # Escolhe palavras da lista sem repetir na mesma senha e junta com hífen
    escolhidas = secrets.SystemRandom().sample(PALAVRAS, k=qtd)
    return '-'.join(escolhidas)

@app.route('/', methods=['GET', 'POST'])
def index():
    frase_gerada = ''
    quantidade = 4 # Valor padrão

    if request.method == 'POST':
        quantidade = int(request.form.get('quantidade', 4)) # Pega a quantidade do formulário ou usa o padrão
        frase_gerada = gerar_frase(quantidade)

    return render_template('index.html', frase=frase_gerada, qtd_selecionada=quantidade)

if __name__ == '__main__':
    app.run(debug=True)