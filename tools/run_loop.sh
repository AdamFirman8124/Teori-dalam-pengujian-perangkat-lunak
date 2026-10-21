#!/bin/bash
# Jalankan notebook berulang sampai selesai (kode 0), dengan jeda antar-percobaan.
cd /home/masoyi/Teori-dalam-pengujian-perangkat-lunak-main || exit 1
LOG=experiment_results_linux/runner_stdout.log
for i in $(seq 1 200); do
  printf '=== attempt %s %s ===\n' "$i" "$(date -u +%FT%TZ)" >> "$LOG"
  .venv/bin/python tools/run_notebook.py experiments_linux.ipynb \
      experiment_results_linux/executed.ipynb >> "$LOG" 2>&1
  code=$?
  printf 'EXIT_CODE=%s\n' "$code" >> "$LOG"
  if [ "$code" -eq 0 ]; then
    break
  fi
  docker ps -aq --filter label=teori.experiment=codamosa | xargs -r docker rm -f >/dev/null 2>&1
  sleep 20
done
