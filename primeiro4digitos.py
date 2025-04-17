def separa_4_primeiros_bits(entrada):# Pede ao usuário uma string de 16 bits e retorna os 4 .
    
   
    # Pega os 4 primeiros bits (posições 0, 1, 2 e 3)
    quatro_primeiros = entrada[:4]
    quatro_em_diante = entrada[4:].strip() #remove os espaços do final e inicio
    
    
    print(f"Bits digitados: {entrada}")
    print("Os 4 primeiros bits são:", quatro_primeiros)
    print(f"12 ultimos digitos: {quatro_em_diante}")
    return quatro_primeiros, quatro_em_diante

# Executa o programa
entrada = input()
separa_4_primeiros_bits(entrada)