#!/bin/bash
# Starts various run_codamosa.py in parallel

for i in 0 1 2 3 4 5 6 7 8 9; do
    python3 run_codamosa.py >>log/run_codamosa-${i}.log 2>&1 &
done
