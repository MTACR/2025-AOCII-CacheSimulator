import struct
import sys
from cache import Cache

def main():
    if len(sys.argv) != 7:
        print("Número de argumentos incorreto. Utilize: ")
        print("python3 main.py <nsets> <bsize> <assoc> <substituição> <flag_saida> arquivo_de_entrada")
        exit(1)

    # todo: verificar e corrigir pq o código não consegue buscar o bin dentro da pasta
    # ou se é erro ao executar no terminal

    nsets = int(sys.argv[1])
    bsize = int(sys.argv[2])
    assoc = int(sys.argv[3])
    subst = sys.argv[4]
    flagOut = int(sys.argv[5])
    arquivoEntrada = sys.argv[6]

    if nsets <= 0 or bsize <= 0 or assoc <= 0:
        print("Erro: nsets, bsize e assoc devem ser maiores que zero.")
        exit(1)

    if subst not in ['R', 'F', 'L']:
        print("Erro: A política de substituição deve ser 'R' (Random), 'F' (FIFO) ou 'L' (LRU).")
        exit(1)

    if flagOut not in [0, 1]:
        print("Erro: flagOut deve ser 0 ou 1.")
        exit(1)

    print("nsets =", nsets)
    print("bsize =", bsize)
    print("assoc =", assoc)
    print("subst =", subst)
    print("flagOut =", flagOut)
    print("arquivo =", arquivoEntrada)

    stats = [0] * 4
    cont = 0

    cache = Cache(nsets, bsize, assoc, subst)

    try:
        with open(arquivoEntrada, "rb") as bin_file:
            while True:
                data = bin_file.read(4)
                if not data:
                    break

                end = struct.unpack('i', data)[0]
                response = cache.load(end)

                if response == 2:
                    if not cache.is_full():
                        response = 3

                stats[response] += 1
                cont += 1

        total_miss = stats[1] + stats[2] + stats[3]

        if cont == 0:
            print("Aviso: Nenhum acesso à cache foi realizado.")
            exit(0)

        hit_rate = stats[0] / cont
        miss_rate = total_miss / cont

        if total_miss > 0:
            comp_miss_rate = stats[1] / total_miss
            cap_miss_rate = stats[2] / total_miss
            conf_miss_rate = stats[3] / total_miss
        else:
            comp_miss_rate = cap_miss_rate = conf_miss_rate = 0.0

        if flagOut == 1:
            print(f"{cont} "
                  f"{hit_rate:.2f} "
                  f"{miss_rate:.2f} "
                  f"{comp_miss_rate:.2f} "
                  f"{cap_miss_rate:.2f} "
                  f"{conf_miss_rate:.2f}")
        else:
            print(f"Nome do Arquivo:\t\t{arquivoEntrada}\n"
                  f"Total de Acessos:\t\t{cont}\n"
                  f"Total de Hit:\t\t\t{stats[0]}\n"
                  f"Taxa de Hit:\t\t\t{hit_rate * 100:.2f}%\n"
                  f"Total de Miss:\t\t\t{total_miss}\n"
                  f"Taxa de Miss:\t\t\t{miss_rate * 100:.2f}%\n"
                  f"Total de Miss Compulsório:\t{stats[1]}\n"
                  f"Taxa de Miss Compulsório:\t{comp_miss_rate * 100:.2f}%\n"
                  f"Total de Miss de Capacidade:\t{stats[2]}\n"
                  f"Taxa de Miss de Capacidade:\t{cap_miss_rate * 100:.2f}%\n"
                  f"Total de Miss de Conflito:\t{stats[3]}\n"
                  f"Taxa de Miss de Conflito:\t{conf_miss_rate * 100:.2f}%")

    except FileNotFoundError as ex:
        print(f"Erro: {ex}", file=sys.stderr)
    except IOError as ex:
        print(f"Erro: {ex}", file=sys.stderr)

if __name__ == '__main__':
    main()