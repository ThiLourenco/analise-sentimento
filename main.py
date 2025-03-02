import re
import unicodedata

def normalizar_texto(texto):
    return unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("utf-8").lower()

def analise_sentimento(comentario):
    comentario = normalizar_texto(comentario)  
    palavras = set(re.findall(r'\b\w+\b', comentario)) 

    positivas = {
        "bom", "boa", "otimo", "excelente", "maravilhoso", "gostei", "incrivel", "amei", "amo", "fantastico", 
        "feliz", "alegre", "satisfeito", "adoro", "perfeito", "perfeita", "positivo", "agradavel", "espetacular", 
        "magnifico", "encantador", "fascinante", "sensacional", "emocionante", "brilhante", "fenomenal",
        "radiante", "divertido", "genuino", "bem", "forte", "esperanca", "confianca", "sucesso", "prospero",
        "animado", "otimismo", "triunfo", "vitoria", "agradavel", "entusiasmado"
    }
    
    negativas = {
        "ruim", "pessimo", "horrivel", "terrivel", "odeio", "triste", "chateado", "lamentavel", "desagradavel", 
        "fraco", "negativo", "insuportavel", "decepcionante", "desastroso", "irritante", "tedioso", 
        "desanimador", "frustrante", "infeliz", "lastimavel", "desmotivado", "nervoso", "cansado",
        "desastroso", "sofrimento", "desespero", "fracasso", "horrendo", "critico", "pavoroso",
        "sinistro", "aterrorizante"
    }

    count_positivo = sum(1 for palavra in palavras if palavra in positivas)
    count_negativo = sum(1 for palavra in palavras if palavra in negativas)

    if count_positivo > count_negativo:
        return "Positivo"
    elif count_negativo > count_positivo:
        return "Negativo"
    else:
        return "Neutro"

if __name__ == "__main__":
    comentario = input("Insira sua mensagem: ")
    sentimento = analise_sentimento(comentario)
    print("Sentimento:", sentimento)
