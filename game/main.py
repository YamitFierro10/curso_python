#analisis de textos en positivo, neutro y negativo
from  textblob import TextBlob

class AnalizadorDeSentiemientos:
    def analizar_sentimientos(self, texto):
        analisis= TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutro"
        else:
            return "negativo"

texto_analizar=input("¿Como estas Hoy en ingles?   ")      
analizador=AnalizadorDeSentiemientos()
resultado=analizador.analizar_sentimientos(texto_analizar)
print(resultado)    