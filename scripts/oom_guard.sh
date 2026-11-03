#!/usr/bin/env bash
# Antigravity & Docker Permanent OOM Guard
# Forces Linux kernel OOM score to -1000 (immune) for Antigravity, Docker, and IDE components.

PATTERNS="antigravity|docker|containerd|qemu-system|language_server|pyrefly|virtiofsd"

while true; do
    for p in $(pgrep -f "$PATTERNS" 2>/dev/null); do
        if [ -d "/proc/$p" ]; then
            # Never protect test containers or pytest runners
            cmd=$(cat "/proc/$p/cmdline" 2>/dev/null | tr '\0' ' ' || true)
            if [[ "$cmd" =~ pynguin|pytest|coverage|run_experiment ]]; then
                continue
            fi
            curr=$(cat "/proc/$p/oom_score_adj" 2>/dev/null || true)
            if [ "$curr" != "-1000" ] && [ -n "$curr" ]; then
                sudo /usr/bin/choom -n -1000 -p "$p" 2>/dev/null || true
            fi
        fi
    done
    sleep 2
done
