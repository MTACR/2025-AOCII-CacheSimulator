#!/bin/bash

tests=(
    "256 4 1 R 1 bin_100.bin" #100 0.9200 0.0800 1.00 0.00 0.00
    "128 2 4 R 1 bin_1000.bin" #1000 0.8640 0.1360 1.00 0.00 0.00
    "16 2 8 R 1 bin_10000.bin" #10000 0.9298 0.0702 0.18 0.79 0.03
    "512 8 2 R 1 vortex.in.sem.persons.bin" #186676 0.8782 0.1218 0.05 0.93 0.02
    "1 4 32 R 1 vortex.in.sem.persons.bin" #186676 0.5440 0.4560 0.00 1.00 0.00
    "2 1 8 R 1 bin_100.bin" #100 0.43 0.57 0.28 0.68 0.04
    "2 1 8 L 1 bin_100.bin" #100 0.46 0.54 0.30 0.67 0.04
    "2 1 8 F 1 bin_100.bin" #100 0.43 0.57 0.28 0.68 0.04
    "1 4 32 R 1 vortex.in.sem.persons.bin" #186676 0.5440 0.4560 0.00 1.00 0.00
    "1 4 32 L 1 vortex.in.sem.persons.bin" #186676 0.5756 0.4244 0.00 1.00 0.00
    "1 4 32 F 1 vortex.in.sem.persons.bin" #186676 0.5530 0.4470 0.00 1.00 0.00
)

for params in "${tests[@]}"; do
    echo "Executando teste: $params"
    python3 cache_simulator.py $params
    echo "----------------------------------------"
done
