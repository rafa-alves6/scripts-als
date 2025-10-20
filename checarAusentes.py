import os

def encontrar_pdfs_ausentes(diretorio, inicio, fim):
    """
    Verifica quais arquivos PDF estão ausentes em um intervalo numérico.

    Args:
        diretorio (str): O caminho para o diretório com os arquivos PDF.
        inicio (int): O número inicial do intervalo a ser verificado.
        fim (int): O número final do intervalo a ser verificado.

    Returns:
        list: Uma lista com os números dos arquivos PDF que estão faltando.
    """
    arquivos_ausentes = []
    
    # Lista todos os arquivos no diretório para uma verificação mais eficiente
    arquivos_existentes = {f.split('.')[0] for f in os.listdir(diretorio) if f.endswith('.pdf')}
    
    for numero in range(inicio, fim + 1):
        # Verifica se o arquivo com o número existe, incluindo variações como '-A'
        encontrado = False
        if str(numero) in arquivos_existentes:
            encontrado = True
        else:
            for nome_arquivo in arquivos_existentes:
                if nome_arquivo.startswith(str(numero) + '-'):
                    encontrado = True
                    break
        
        if not encontrado:
            arquivos_ausentes.append(numero)
            
    return arquivos_ausentes
# --- Exemplo de uso ---

# Substitua 'C:\\sua\\pasta\\aqui' pelo caminho real da sua pasta de PDFs
caminho_da_pasta = r'Z:\CARTORIO DE SIMAO DIAS\LIVRO 2-AA - REGISTRO DE IMÓVEIS\PDF'
numero_inicial = 7107
numero_final = 7404

# Verificando se o diretório existe
if not os.path.isdir(caminho_da_pasta):
    print(f"Erro: O diretório '{caminho_da_pasta}' não foi encontrado.")
else:
    pdfs_ausentes = encontrar_pdfs_ausentes(caminho_da_pasta, numero_inicial, numero_final)

    if pdfs_ausentes:
        print("Os seguintes PDFs estão faltando no intervalo de "
              f"{numero_inicial} a {numero_final}:")
        for i in pdfs_ausentes:
              print(f"{i}\n")
        print(f"Faltam {len(pdfs_ausentes)} matrículas ao todo.")      
    else:
        print(f"Todos os PDFs do intervalo de {numero_inicial} a {numero_final} estão presentes.")