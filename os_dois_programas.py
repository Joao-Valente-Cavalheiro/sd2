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
  

def comparacao(hexa):
  if hexa == 0: 
    return "JnS"
  elif hexa == 1:
    return "Load"
  elif hexa == 2:
    return "Store"
  elif hexa == 3:
    return "Add"  
  elif hexa == 4:
    return "Subt"
  elif hexa == 5:
    return "Input"
  elif hexa == 6:
    return "Output"
  elif hexa == 7:
    return "Halt" #esse halt teria que parar o programa, dai nao sei como prosseguir, se colocar ele no final do txt da o return " " , se ele tiver no meio tem que desconsiderar as outras entradas, sacou? saquei
  elif hexa == 8:
    return "Skipcond"
  elif hexa == 9:
    return "Jump"
  elif hexa == 10:
    return f"LoadImmi {ultimos}\nClear" #LoadImmi não aparece no ava mas ta na tabela do git, no ava só tem Load e LoadI R: mas se tem no git tem que ter no codigo
  # elif hexa == 10:
  #     return "Clear"
  elif hexa == 11:
      return "AddI"
  elif hexa == 12:
      return "JumpI"
  elif hexa == 13:
    return "LoadI"
  elif hexa == 14:
    return "StoreI"
  

 

funcao=[]
decimal = []
entradas = open("entrada.txt",'r')
linha = entradas.readline()
while linha:
  quatroBit,dozeBit=separa_4_primeiros_bits(linha)
  hexa = trocar_base(quatroBit,16,4)
  funcao.append(comparacao(hexa))
  decimal.append(trocar_base(dozeBit,2,12))
  
  linha = entradas.readline()

