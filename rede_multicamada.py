# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 19:55:18 2018

@author: marce
"""

import numpy as np

#função de ativação SIGMOIDE
def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerviada(sig):
    return sig * (1 - sig)


entradas = np.array([[0,0],
                     [0,1],
                     [1,0],
                     [1,1]])
        
saidas = np.array([[0],[1],[1],[0]])

pesos0 = np.array([[-0.424, -0.740, -0.961],
                   [0.358, -0.577, -0.469]])
    
pesos1 = np.array([[-0.017],[-0.893],[0.148]])

epocas = 100 #training time -> indica quantas rodadas o algoritmo fará para ajustar os pesos

taxaAprendizagem = 0.3
momento = 1 

for j in range(epocas): 
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada,pesos0) #dot product efetua função soma
    camadaOculta = sigmoid(somaSinapse0) #efetua função sigmoid
    
    somaSinapse1 = np.dot(camadaOculta,pesos1) #dot product efetua função soma
    camadaDeSaida = sigmoid(somaSinapse1) #efetua função sigmoid
    
    erroCamadaSaida = saidas - camadaDeSaida #efetua calculo do array e matriz
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida)) #abs = valor absoluto (sem sinal) - mean = média
    
    derivadaSaida = sigmoidDerviada(camadaDeSaida) 
    deltaSaida = erroCamadaSaida * derivadaSaida
    
    pesos1Transposta = pesos1.T # .T deixa a matriz transposta
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta =  deltaSaidaXPeso * sigmoidDerviada(camadaOculta)
    
    camadaOcultaTransposta = camadaOculta.T
    pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem)

    camadaEntradaTransposta = entradas.T
    pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)    
    pesos0 = (pesos0 * momento) + (pesosNovo0 * taxaAprendizagem)