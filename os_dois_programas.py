def separa_4_primeiros_bits(entrada):# Pede ao usuário uma string de 16 bits e retorna os 4 .
    
   
    # Pega os 4 primeiros bits (posições 0, 1, 2 e 3)
    quatro_primeiros = entrada[:4]
    quatro_em_diante = entrada[4:].strip() #remove os espaços do final e inicio
    

    return quatro_primeiros, quatro_em_diante

# esse código pega a segunda parte da entrada binaria e da como saida um valor inteiro
# exp: 0011 000000110010 segunda parte --> 000000110010 = 50
def trocar_base(entrada,base,potencia):
  vetor = list(entrada)

  lista=[]
  i=0
  while i <len(vetor):
    lista.append(int(vetor[i]))
    i+=1

  x=0 
  soma = 0

  while x < len(lista):
    bit = lista[x]
    pot = bit*(base**potencia)
    soma = soma + pot

    x+=1
    potencia = potencia - 1
    
  return soma

 
funcao=[]
decimal = []
entradas = open("entrada.txt",'r')
linha = entradas.readline()
while linha:
  quatroBit,dozeBit=separa_4_primeiros_bits(linha)
  funcao.append("FUNÇAO QUE RETORNA A STRING COM O NOME DA FUNÇÃO")
  decimal.append(trocar_base(dozeBit,2,12))
  
  linha = entradas.readline()
