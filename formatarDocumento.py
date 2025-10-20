import re
import pyperclip
import keyboard

# Função para validar e formatar CPF
def formatar_cpf(cpf: str) -> str:
    # Remove qualquer caracter não numérico
    cpf = re.sub(r'\D', '', cpf)

    # Verifica se tem exatamente 11 dígitos
    if len(cpf) == 11:
        # Formata o CPF no formato xxx.xxx.xxx-xx
        cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
        return cpf_formatado
    return None

# Função para validar e formatar CNPJ
def formatar_cnpj(cnpj: str) -> str:
    # Remove qualquer caracter não numérico
    cnpj = re.sub(r'\D', '', cnpj)

    # Verifica se tem exatamente 14 dígitos
    if len(cnpj) == 14:
        # Formata o CNPJ no formato xx.xxx.xxx/xxxx-xx
        cnpj_formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
        return cnpj_formatado
    return None

# Função principal que será chamada após apertar F2
def processar_area_transferencia():
    # Captura o conteúdo da área de transferência (CTRL+C)
    texto = pyperclip.paste()

    # Verifica se o texto é um CPF ou CNPJ
    cpf_formatado = formatar_cpf(texto)
    if cpf_formatado:
        pyperclip.copy(cpf_formatado)  # Atualiza a área de transferência com o CPF formatado
        print(f"CPF formatado: {cpf_formatado}")
        return

    cnpj_formatado = formatar_cnpj(texto)
    if cnpj_formatado:
        pyperclip.copy(cnpj_formatado)  # Atualiza a área de transferência com o CNPJ formatado
        print(f"CNPJ formatado: {cnpj_formatado}")
        return

    print("O conteúdo da área de transferência não é um CPF ou CNPJ válido!")

# Loop que fica esperando o pressionamento da tecla F2 até que a tecla 0 seja pressionada
print("Aperte F2 para processar o conteúdo da área de transferência. Aperte 0 para sair.")
while True:
    if keyboard.is_pressed('F2'):
        processar_area_transferencia()
    elif keyboard.is_pressed('F1'):
        print("Saindo do programa...")
        break
