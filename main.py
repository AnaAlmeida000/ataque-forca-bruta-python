import itertools
import time

def quebrar_senha_forca_bruta(senha_alvo, caracteres_disponiveis):
    """
    Função que realiza um ataque de força bruta testando combinações
    de até 3 caracteres e exibindo o progresso em tempo real.
    """
    print(f"--- Iniciando ataque de força bruta ---")
    print(f"Senha alvo: {senha_alvo}")
    
    total_tentativas = 0
    inicio_tempo = time.time()
    
    # Testa comprimentos de senha de 1 até 3 caracteres
    for comprimento in range(1, 4):
        print(f"\n[!] Testando combinações com tamanho: {comprimento}")
        
        # Dica 2: itertools.product gera as combinações em formato de tupla
        for combinacao in itertools.product(caracteres_disponiveis, repeat=comprimento):
            total_tentativas += 1
            
            # Dica 3: Transforma a tupla de caracteres em uma palavra (string)
            senha_testada = "".join(combinacao)
            
            # Mostra o progresso na mesma linha usando end="\r"
            print(f"Tentativa nº {total_tentativas}: {senha_testada}", end="\r")
            
            # Verifica se a senha testada é igual à senha alvo
            if senha_testada == senha_alvo:
                fim_tempo = time.time()
                tempo_total = fim_tempo - inicio_tempo
                
                print(f"\n\n[SUCESSO] Senha descoberta: '{senha_testada}'")
                print(f"Total de tentativas necessárias: {total_tentativas}")
                print(f"Tempo total gasto: {tempo_total:.4f} segundos")
                return True
                
    print("\n\n[FALHA] A senha não foi encontrada nas combinações de até 3 caracteres.")
    return False

# --- Configurações do seu teste ---
# Dica 1: Conjunto pequeno de caracteres e senha curta para não demorar
caracteres = "abc123"
senha_secreta = "b2c"

# Executa o desafio
quebrar_senha_forca_bruta(senha_secreta, caracteres)
