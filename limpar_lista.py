import unicodedata

def remover_acentos(texto):
    # Transformar ç em c e â em a, por exemplo
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

# Abre o arquvo palavras.txt
with open('palavras.txt', 'r', encoding='utf-8') as f:
    palavras = f.readlines()

# Liimpa cada palavra
palavras_limpas = [remover_acentos(p.strip().lower()) for p in palavras]

palavras_final = sorted(set(palavras_limpas))

# Salva de volta o arquivo
with open('palavras.txt', 'w', encoding='utf-8') as f:
    for p in palavras_final:
        f.write(p + '\n')



print(f"Pronto! Agora temos {len(palavras_final)} palavras únicas e sem acento.")