def extrairDados(corpoTabela,colunaUm,colunaDois):
    #retorna os dados em formato de dicionário

    dados =[]
    
    for indice, linha in enumerate(corpoTabela):
        if(indice % 2 == 0):
            dadosLinha = {
                colunaUm : corpoTabela[indice].text,
                colunaDois : corpoTabela[indice+1].text
            }
            dados.append(dadosLinha)

    return dados