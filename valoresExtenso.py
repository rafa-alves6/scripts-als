import re
import pyperclip
import keyboard
import unidecode

# Mapeamento das moedas para nomes por extenso
MOEDAS = {
    "R$": "reais",
    "CR$": "cruzeiros reais",
    "Cr$": "cruzeiros",
    "Cz$": "cruzados",
    "NCz$": "cruzados novos",
}

def extrair_valor_moeda(texto):
    """
    Extrai o primeiro valor monetário e seu símbolo da string, como 'R$ 5.000,00'
    """
    padrao = r"(?i)\b(R\$|CR\$|Cr\$|Cz\$|NCz\$)\s*([\d\.\,]+)"
    match = re.search(padrao, texto)
    if match:
        simbolo_moeda = match.group(1)
        valor_str = match.group(2)

        # Tratamento regional: converte 1.234,56 → 1234.56
        if ',' in valor_str:
            valor_str = valor_str.replace('.', '').replace(',', '.')
        else:
            valor_str = valor_str.replace('.', '')  # Apenas milhar, sem centavos

        try:
            valor_float = float(valor_str)
            return simbolo_moeda, valor_float
        except ValueError:
            print("❌ Erro ao converter valor:", valor_str)
            return None, None
    return None, None



def numero_por_extenso(valor):
    """
    Converte número para texto por extenso em português
    """
    unidades = [
        "", "um", "dois", "três", "quatro", "cinco",
        "seis", "sete", "oito", "nove", "dez", "onze",
        "doze", "treze", "quatorze", "quinze", "dezesseis",
        "dezessete", "dezoito", "dezenove"
    ]
    dezenas = [
        "", "", "vinte", "trinta", "quarenta", "cinquenta",
        "sessenta", "setenta", "oitenta", "noventa"
    ]
    centenas = [
        "", "cem", "duzentos", "trezentos", "quatrocentos",
        "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"
    ]

    def extenso(n):
        if n == 0:
            return "zero"
        elif n < 20:
            return unidades[n]
        elif n < 100:
            dez = dezenas[n // 10]
            uni = unidades[n % 10]
            return dez + (f" e {uni}" if uni else "")
        elif n < 1000:
            if n == 100:
                return "cem"
            else:
                cen = centenas[n // 100]
                resto = extenso(n % 100)
                return cen + (f" e {resto}" if n % 100 != 0 else "")
        elif n < 1_000_000:
            mil = n // 1000
            resto = n % 1000
            parte_mil = "mil" if mil == 1 else extenso(mil) + " mil"
            parte_resto = extenso(resto)
            if resto == 0:
                return parte_mil
            else:
                return f"{parte_mil} e {parte_resto}"
        else:
            return "valor muito alto"

    return extenso(valor)

def valor_monetario_por_extenso(valor, moeda_nome):
    reais = int(valor)
    centavos = int(round((valor - reais) * 100))
    
    texto = ""
    if reais > 0:
        texto += f"{numero_por_extenso(reais)} {moeda_nome}"
        if reais == 1:
            texto = texto.replace("reais", "real")
    if centavos > 0:
        if texto:
            texto += " e "
        texto += f"{numero_por_extenso(centavos)} centavos"
    if not texto:
        texto = "zero " + moeda_nome
    return texto

def processar_clipboard():
    texto = pyperclip.paste().strip()
    texto = texto.replace('\n', ' ').replace('\r', '')
    simbolo, valor = extrair_valor_moeda(texto)
    if simbolo and valor is not None:
        moeda_extenso = MOEDAS.get(simbolo.upper(), "reais")
        extenso = valor_monetario_por_extenso(valor, moeda_extenso)
        pyperclip.copy(extenso.capitalize())
        print(f"✅ Copiado por extenso: {extenso}")
    else:
        print("❌ Nenhum valor monetário reconhecido no clipboard.")


def main():
    hotkey = 'f9'
    print(f"Aperte {hotkey} para converter valor monetário selecionado para texto por extenso.")
    keyboard.add_hotkey(hotkey, processar_clipboard)
    print("Pressione ESC para sair.")
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
