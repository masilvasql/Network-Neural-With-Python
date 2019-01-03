# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:11:28 2018

@author: marce
"""
import numpy as np
#and
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0,0,0,1])

#or
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0,1,1,1])

#XOR
entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([0,1,1,0])

pesos = np.array([0.0,0.0])
taxaAprendizagem =0.1

def stepFunction(soma):
    if(soma >=1):
        return 1
    return 0
    
def calculaSaida(registro):
    s = registro.dot(pesos) #dot fara 1ª entrada * 1º peso + 2ª entrada * 1º peso
    return stepFunction(s)

def treinar():
    erroTotal = 1
    while(erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i]- saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('PESO ATUALIZADO: ' +str(pesos[j]))
        print('TOTAL DE ERROS: ' + str(erroTotal))

treinar()
print("REDE NEURAL TREINADA")
print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))