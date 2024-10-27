from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import functions as fn
from datetime import datetime
import requests
from bs4 import BeautifulSoup

@api_view(['GET'])
def instrucoes(request):
    # Rota inicial da api. Instruir o desenvolvedor a solicitar corretamente os dados  
    if request.method == 'GET':
        return Response({"msg":"Siga o exemplo da query parameters /dados?data=AAAA-MM-DD&slcTaxa=EUR para obter informações sobre as taxas de referência!"})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def buscaDados(request):
    # pega os query parameters da url
    data = request.GET.get('data')
    slcTaxa = request.GET.get('slcTaxa')

    if data and slcTaxa:
        try:
            # verifica a validade da data inserida 
            data = datetime.strptime(data,'%Y-%m-%d').date()            
            data1 = str(data)
            data = data.strftime('%m/%d/%Y')            
            data1 = data1.replace('-','')
            #print(data, data1)  

        except:
            return Response({"error": "O formato da data está incorreto ",
                             "data":"use AAAA-MM-DD",
                             "exemplo":"2024-12-31"}, status=400)
        
        
        url = f'https://www2.bmf.com.br/pages/portal/bmfbovespa/lumis/lum-taxas-referenciais-bmf-enUS.asp?Data={data}&Data1={data1}&slcTaxa={slcTaxa}'
        #?Data=08/08/2024&Data1=20241025&slcTaxa=EUR
        #?Data={dataFormatada}&Data1={data1}&slcTaxa={slcTaxa}
        try:
            #responsável por fazer a requisição ao site da url
            data = {
                "slcTaxa": slcTaxa,
                "Data1": data1,
                "Data": data,
                "convertexls1": "",
                "nomexls": "",
                "lQtdTabelas": "",
                "IDIOMA": 2
            }           
            
            response = requests.post(url, data=data, timeout=10)
            #tenta evitar erros por conexão lenta
            if not response:
                contador = 3
                while contador > 0:
                    response = requests.post(url, data=data, timeout=10)
                    contador -=1

            #retorna a estrutura HTML da página
            pagina = BeautifulSoup(response.text, 'html.parser')
            #print(pagina)
        except requests.exceptions.RequestException as e:
            return Response({"msg":"Tempo de requisição excedido. Tente novamente!"},status=504)

        tabela = pagina.find('table')        
        
        if not tabela:
            return Response({"titulo":"Os dados não foram encontrados!",
                             "msg":"parâmetro de busca inválido ou sem informações para o período escolhido!"},status=400)
        
        #extração das informações da página.
        cabecalho = tabela.find_all('th')
        if(len(cabecalho) == 3):        
            calendario = cabecalho[0].text.strip()
            taxaReferencia = cabecalho[1].text.strip()                              
            periodo = cabecalho[2].text.strip()
            #print(calendario, taxaReferencia,periodo)          
            
            corpoTabela = pagina.find_all('td')
            #agrupando os dados para retorno da requisição
            dados = fn.extrairDados(corpoTabela=corpoTabela,calendario=calendario,taxaReferencia=taxaReferencia,periodoUm=periodo)        
        elif(len(cabecalho) == 4):
            calendario = cabecalho[0].text.strip()
            taxaReferencia = cabecalho[1].text.strip()                              
            periodo = cabecalho[2].text.strip()
            periodoDois = cabecalho[3].text.strip()
            #print(calendario, taxaReferencia,periodo)           
            corpoTabela = pagina.find_all('td')
            #agrupando os dados para retorno da requisição
            dados = fn.extrairDados(corpoTabela=corpoTabela,calendario=calendario,taxaReferencia=taxaReferencia,periodoUm=periodo,periodoDois=periodoDois)        
        else:
            dados = "Desculpe ainda não foi implementado uma logica para tabelas com quatro colunas"    

        informacaoData = datetime.strptime(data1,'%Y%m%d').date() 
        dadosTaxa = {
            "Data": informacaoData,
            "Dados da taxa de referência para o período":dados
        }
        
        return Response(dadosTaxa,status=200)
    else:
        return Response({"msg": "Parâmetros 'data' e 'slcTaxa' são obrigatórios"}, status=400)

