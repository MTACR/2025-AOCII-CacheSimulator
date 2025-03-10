import sys

from cache import Cache


def main():
    # verifica os argumentos passados na linha de comando
    if len(sys.argv) != 7:
        print("Número de argumentos incorreto. Utilize:")
        print("python3 cache_simulator.py <nsets> <bsize> <assoc> <substituição> <flagOut> <arquivo_de_entrada>")
        exit(1)

    nsets = int(sys.argv[1]) # Número de conjuntos da cache
    bsize = int(sys.argv[2]) # Tamanho do bloco
    assoc = int(sys.argv[3]) # Grau de associatividade
    subst = sys.argv[4][0] # Política de substituição
    flagOut = int(sys.argv[5]) # Define o modo de saída
    arquivoEntrada = sys.argv[6]

    # Imprime os parâmetros
    print("nsets =", nsets)
    print("bsize =", bsize)
    print("assoc =", assoc)
    print("subst =", subst)
    print("flagOut =", flagOut)
    print("file =", arquivoEntrada)

    # Inicializa a lista de estatísticas:
    # stats[0] -> hits
    # stats[1] -> miss compulsório
    # stats[2] -> miss de capacidade
    # stats[3] -> miss de conflito
    stats = [0, 0, 0, 0]
    cont = 0 # Contador de acessos totais

    # Cria uma instância da cache com os parâmetros fornecidos
    cache = Cache(nsets, bsize, assoc, subst)

    try:
        # Abre o arquivo binário de entrada para leitura
        with open(arquivoEntrada, 'rb') as bin_file:
            while True:
                addresses = bin_file.read(4)  # Lê 4 bytes por vez (endereço de memória de 32 bits)
                if not addresses:
                    break
                end = int.from_bytes(addresses, byteorder='big') # Converte os 4 bytes lidos para um inteiro (endereço de memória)
                response = cache.load(end) # Chama a função load da cache para verificar se o endereço já estava armazenado

                if response == 2: # Se a resposta for 2 (miss de capacidade), verifica se a cache está cheia
                    if not cache.is_full():
                        response = 3 # Se não estiver cheia, trata como um miss de conflito

                stats[response] += 1  # Atualiza a estatística correspondente
                cont += 1 # Incrementa o total de acessos

        t_miss = stats[1] + stats[2] + stats[3] # Calcula o total de misses
        if flagOut == 1:
            print(f"\n{cont} {stats[0] / cont:.4f} {t_miss / cont:.4f} {stats[1] / t_miss:.2f} {stats[2] / t_miss:.2f} {stats[3] / t_miss:.2f}")
        elif flagOut == 0:
            print(f"\nNome do Arquivo:\t\t{arquivoEntrada}"
                  f"\nTotal de Acessos:\t\t{cont}"
                  f"\nTotal de Hit:\t\t\t{stats[0]}"
                  f"\nTaxa de Hit:\t\t\t{(stats[0] / cont) * 100:.2f}%"
                  f"\nTotal de Miss:\t\t\t{t_miss}"
                  f"\nTaxa de Miss:\t\t\t{(t_miss / cont) * 100:.2f}%"
                  f"\nTotal de Miss Compulsório:\t{stats[1]}"
                  f"\nTaxa de Miss Compulsório:\t{(stats[1] / t_miss) * 100:.2f}%"
                  f"\nTotal de Miss de Capacidade:\t{stats[2]}"
                  f"\nTaxa de Miss de Capacidade:\t{(stats[2] / t_miss) * 100:.2f}%"
                  f"\nTotal de Miss de Conflito:\t{stats[3]}"
                  f"\nTaxa de Miss de Conflito:\t{(stats[3] / t_miss) * 100:.2f}%")

    except FileNotFoundError as ex: #arquivo de entrada não encontrado
        print(f"Erro: {ex}")
    except IOError as ex:  #problema na leitura do arquivo
        print(f"Erro: {ex}") 


if __name__ == "__main__":
    main()
