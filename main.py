# cache_val [n_sets * assoc];
# cache_tag [n_sets * assoc];
# //criar uma estrutura de dados para armazenar os tags e os bits de validade.
#
# n_bits_offset = log2 bsize;
# n_bits_indice = log2 nsets;
#
# n_bits_tag = 32 - n_bits_offset - n_bits_indice;
# //descobre o número de bits de cada parcela do endereço
#
# //para todos os endereços do arquivo
# while (not EOF)
# {
#     endereço = ler (arquivo_de_entrada.bin);
#     tag = endereço >> (n_bits_offset + n_bits_indice);
#     indice = (endereço >> n_bits_offset) & (2^n_bits_indice -1);
#     //isso é uma máscara que vai deixar apenas os bits do índice na variável “endereço”.
#
#     // para o mapeamento direto
#     if (cache_val[indice] == 0)
#     {
#         miss_conpulsório ++;
#         cache_val[indice] = 1;
#         cache_tag[indice] = tag;
#         // estas duas últimas instruções representam o tratamento da falta.
#     }
#     else
#         if (cache_tag[indice] == tag)
#         hit ++;
#         else
#         {
#             miss ++;
#             //conflito ou capacidade?
#             cache_val[indice] = 1;
#             cache_tag[indice] = tag;
#         }
