import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.google.com')
except urllib.error.URLError:
    print('O site do Google não está disponível no momento !')
else:
    print('O site do Google está sendo acessado com sucesso !')
    #print(site.read())
