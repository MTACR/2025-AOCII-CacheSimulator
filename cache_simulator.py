import sys

from cache import Cache


def main():
    # verifica os argumentos passados na linha de comando
    if len(sys.argv) != 7:
        print("Número de argumentos incorreto. Utilize:")
        print("python3 cache_simulator.py <nsets> <bsize> <assoc> <substituição> <flagOut> <arquivo_de_entrada>")
        exit(1)

    nsets = int(sys.argv[1])
    bsize = int(sys.argv[2])
    assoc = int(sys.argv[3])
    subst = sys.argv[4][0]
    flagOut = int(sys.argv[5])
    arquivoEntrada = sys.argv[6]

    # verifica apenas nsets e bsize
    if not (Cache.is_power_of_2(nsets) and Cache.is_power_of_2(bsize)):
        print("Erro: nsets e bsize devem ser potências de 2.")
        exit(1)

    # verifica se subst é 'R', 'F' ou 'L'
    if subst not in ['R', 'F', 'L']:
        print("Erro: A política de substituição deve ser 'R' (Random), 'F' (FIFO) ou 'L' (LRU).")
        exit(1)

    # verifica se a flag de saída é 0 ou 1
    if flagOut not in [0, 1]:
        print("Erro: flagOut deve ser 0 ou 1.")
        exit(1)

    # imprime os parâmetros
    print("nsets =", nsets)
    print("bsize =", bsize)
    print("assoc =", assoc)
    print("subst =", subst)
    print("flagOut =", flagOut)
    print("file =", arquivoEntrada)

    # stats[0] -> hits
    # stats[1] -> miss compulsório
    # stats[2] -> miss de capacidade
    # stats[3] -> miss de conflito
    stats = [0, 0, 0, 0]
    cont = 0  # contador de acessos totais

    # cria uma instância da cache com os parâmetros fornecidos
    cache = Cache(nsets, bsize, assoc, subst)

    try:

        with open(arquivoEntrada, 'rb') as bin_file:
            while True:
                addresses = bin_file.read(4)  # lê 4 bytes por vez
                if not addresses:
                    break
                ad = int.from_bytes(addresses, byteorder='big')
                response = cache.load(ad)

                if response == 2:  # miss de capacidade
                    if not cache.is_full():
                        response = 3  # miss de conflito

                stats[response] += 1
                cont += 1

        t_miss = stats[1] + stats[2] + stats[3]

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

    except FileNotFoundError as ex:
        print(f"Erro: {ex}")
    except IOError as ex:
        print(f"Erro: {ex}")


if __name__ == "__main__":
    main()
