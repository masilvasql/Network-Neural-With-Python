# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 23:26:19 2018

@author: marce
"""

import numpy as np
#Idade, SPC, tempo de cliente, refComercial
entradas = np.array([[25,2500,5,6],[18,980,0,0],[2,3000,4,0]])
saidas = np.array([1,0,1])
pesos = np.array([0.0,0.0,0.0,0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    if(soma >=1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    erroTotal = -1
    while(erroTotal != 1):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('PESO ATUALIZADO ' + str(pesos[j]))
            print('TOTAL DE ERROS: ' +str(erroTotal))
treinar()

