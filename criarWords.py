import os
import shutil

# --- CONFIGURAÇÃO ---
arquivo_modelo = "Z:\\CARTORIO DE SIMAO DIAS\\LIVRO 2-AA - REGISTRO DE IMÓVEIS\\modelo.docx"

# Coloque o caminho completo para a pasta que contém os arquivos DOCX

pasta_destino = "Z:\\CARTORIO DE SIMAO DIAS\\LIVRO 2-AD - REGISTRO DE IMÓVEIS\\Words"

# --- FIM DA CONFIGURAÇÃO ---


def main():
    """
    Função principal que executa a lógica de cópia.
    """
    # 1. Validação inicial: verificar se o modelo e a pasta existem
    if not os.path.isfile(arquivo_modelo):
        print(f"ERRO: O arquivo modelo não foi encontrado em '{arquivo_modelo}'")
        return

    if not os.path.isdir(pasta_destino):
        print(f"ERRO: A pasta de destino não foi encontrada em '{pasta_destino}'")
        return

    print(f"Usando o modelo: '{os.path.basename(arquivo_modelo)}'")
    print(f"Na pasta destino: '{pasta_destino}'\n")

    # 2. Percorrer todos os arquivos na pasta de destino
    arquivos_modificados = 0
    for nome_arquivo_destino in os.listdir(pasta_destino):
        # Construir o caminho completo do arquivo de destino
        caminho_completo_destino = os.path.join(pasta_destino, nome_arquivo_destino)

        # 3. Verificar se o arquivo é um .docx e não é o próprio arquivo modelo
        if nome_arquivo_destino.lower().endswith('.docx') and os.path.normpath(caminho_completo_destino) != os.path.normpath(arquivo_modelo):
            try:
                # 4. Copiar o arquivo modelo SOBRE o arquivo de destino.
                # shutil.copy() copia o conteúdo do primeiro arquivo para o segundo.
                # Se o segundo já existe, ele será sobrescrito.
                shutil.copy(arquivo_modelo, caminho_completo_destino)
                print(f"[OK] Conteúdo de '{nome_arquivo_destino}' foi substituído com sucesso.")
                arquivos_modificados += 1
            except Exception as e:
                print(f"[ERRO] Falha ao substituir '{nome_arquivo_destino}': {e}")

    print(f"\nProcesso concluído. {arquivos_modificados} arquivo(s) foram modificados.")


if __name__ == "__main__":
    main()