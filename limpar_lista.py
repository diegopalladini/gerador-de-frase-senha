import unicodedata

def remover_acentos(texto):
    # Transformar ç em c e â em a, por exemplo
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

# Abre o arquivo palavras.txt
with open('palavras.txt', 'r', encoding='utf-8') as f:
    palavras = f.readlines()

# LIMPEZA E FILTRO:
# 1. strip().lower() -> limpa espaços e deixa minúsculo
# 2. remover_acentos -> tira ç, á, ê...
# 3. if len(palavra_limpa) >= 4 -> só add se tiver 4 ou mais letras
palavras_limpas = []
for p in palavras:
    palavra_limpa = remover_acentos(p.strip().lower())
    if len(palavra_limpa) >= 3:  
        palavras_limpas.append(palavra_limpa)

# Remove duplicatas e ordena
palavras_final = sorted(set(palavras_limpas))

# Salva de volta o arquivo
with open('palavras.txt', 'w', encoding='utf-8') as f:
    for p in palavras_final:
        f.write(p + '\n')

print(f"Pronto! Agora temos {len(palavras_final)} palavras únicas, sem acento e com no mínimo 4 letras.")