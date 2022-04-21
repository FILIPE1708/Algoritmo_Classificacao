import pickle

modelo = pickle.load(open('modelo.sav', 'rb'))

print('TRIAGEM CORONA VIRUS')
print('')
print('')
print('Respostas e perguntas com 0 para não e 1 para sim')
print('')

feb = int(input('Apresenta Febre? '))
cans = int(input('Apresenta Cansaço? '))
tos = int(input('Apresenta Tosse Seca? '))
esp = int(input('Apresenta Espirro? '))
dcor = int(input('Apresenta Dores No Corpo? '))
cori = int(input('Está corizando? '))
dgar = int(input('Apresenta Dor De Garganta? '))
diar = int(input('Apresenta Diarreia? '))
dcab = int(input('Apresenta Dor De Cabeça? '))
faltAr = int(input('Apresenta Falta De Ar? '))


novoModelo = [[
    feb, cans, tos, esp, dcor, cori, dgar, diar, dcab, faltAr
]]

resultado = modelo.predict(novoModelo)

if(resultado == 1):
    print('')
    print('Resposta:')
    print('Recomenda-se fazer o teste de corona vírus')

elif(resultado == 0):
    print('')
    print('Resposta:')
    print('Paciente não apresenta sintomas de corona vírus')