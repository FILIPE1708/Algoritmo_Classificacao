from sklearn.naive_bayes import GaussianNB
import pickle
import dados

modelo = GaussianNB()
modelo.fit(dados.atributos, dados.resultados)
pickle.dump(modelo, open('modelo.sav', 'wb'))