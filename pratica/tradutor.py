from translate import Translator
#Configurando a tradução
frase = Translator(from_lang='english', to_lang='pt-br')

#Traduzindo o texto
traducao = frase.translate('Good Morning')

print(traducao)
