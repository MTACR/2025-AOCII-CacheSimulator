import sys

from cache import Cache


def main():
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

    print("nsets =", nsets)
    print("bsize =", bsize)
    print("assoc =", assoc)
    print("subst =", subst)
    print("flagOut =", flagOut)
    print("file =", arquivoEntrada)

    stats = [0, 0, 0, 0]
    cont = 0

    cache = Cache(nsets, bsize, assoc, subst)

    try:
        with open(arquivoEntrada, 'rb') as bin_file:
            while True:
                addresses = bin_file.read(4)
                if not addresses:
                    break
                end = int.from_bytes(addresses, byteorder='big')
                response = cache.load(end)

                if response == 2:
                    if not cache.is_full():
                        response = 3

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
