def extrairDados(corpoTabela,calendario,taxaReferencia,periodoUm,periodoDois=0):
    
    dados =[]

    if(periodoDois == 0):
        for indice, linha in enumerate(corpoTabela):
            if(indice % 2 == 0):
                dadosLinha = {
                    calendario : corpoTabela[indice].text,
                    "Taxa de Referencia": taxaReferencia,
                    periodoUm : corpoTabela[indice+1].text
                }
                dados.append(dadosLinha)
    else:        
        for indice in range(0,len(corpoTabela),3):            
            dadosLinha = {
                calendario : corpoTabela[indice].text,
                "Taxa de Referencia": taxaReferencia,
                periodoUm : corpoTabela[indice+1].text,
                periodoDois : corpoTabela[indice+2].text
            }
            dados.append(dadosLinha)
        
    
    
    return dados

    
    
    