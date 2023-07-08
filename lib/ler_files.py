import re

from lib.convert_text_to_voice import convert_text_to_voice
from lib.limpa_tela import clear


def remove_trecho(texto_original, *trechos):
    texto = texto_original
    for trecho in trechos:
        old_t, new_t = trecho
        texto = re.sub(old_t, new_t, texto)
    return texto

def formata_texto(texto):
    return remove_trecho(
            texto, [r'\({0,1}Vigência\){0,1}', ''], [r'\((Red|Inclu).*\)', ''], [r'\((Red|Inclu).*\s*.*\)', ''],
            [r'\(Revogado.*\)', ''], [r'[Aa]rt.', 'Artigo'], [r'§', 'Inciso'], [r'VET ADO', 'VETADO'], 
            [r"XIX - ", "19º - "], [r"XX - ", "20º - "], [r"XVIII - ", "18º - "], [r"XVII - ", "17º - "], [r"XVI - ", "16º - "], 
            [r"XV - ", "15º - "], [r"XIV - ", "14º - "], [r"XIII - ", "13º - "], [r"XII - ", "12º - "], [r"XI - ", "11º - "], 
            [r"IX - ", "9º - "], [r"X - ", "10º - "], [r"VIII - ", "8º - "], [r"VII - ", "7º - "], [r"VI - ", "6º - "], 
            [r"IV - ", "4º - "], [r"V - ", "5º - "], [r"III - ", "3º - "], [r"II - ", "2º - "], [r"I - ", "1º - "]
        )

def ler_pages(pages):
    try:
        inicial = int(input("Deseja começar de qual página?(Enter para iniciar na primeira) ")) - 1
    except:
        inicial = 0

    for i in range(inicial, len(pages)):
        msg = f"Fim da página {(i+1)} de {len(pages)}, deseja continuar? "
        texto = formata_texto(pages[i])

        print(pages[i])
        convert_text_to_voice(texto)

        if i < len(pages)-1:
            convert_text_to_voice(msg)

            if not "s" in input(msg).lower():
                exit()
            else:
                clear()
