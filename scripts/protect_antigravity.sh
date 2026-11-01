#!/usr/bin/env bash
set -euo pipefail

# 1. Update systemd user scope to OOMPolicy=continue
for scope in $(systemctl --user list-units --type=scope --no-legend 2>/dev/null | awk '{print $1}' | grep -E 'antigravity'); do
    dir="$HOME/.config/systemd/user/${scope}.d"
    mkdir -p "$dir"
    cat <<EOF > "$dir/override.conf"
[Scope]
OOMPolicy=continue
ManagedOOMPreference=avoid
EOF
done
systemctl --user daemon-reload 2>/dev/null || true

# 2. If running as root / sudo, immunize Antigravity from kernel OOM killer (-1000)
if [ "$(id -u)" -eq 0 ]; then
    for pid in $(pgrep -f "antigravity|pyrefly"); do
        echo -1000 > "/proc/$pid/oom_score_adj" 2>/dev/null || true
    done
    echo "Antigravity immunized against OOM killer (oom_score_adj = -1000)."
else
    echo "Systemd scope protected with OOMPolicy=continue."
    echo "To grant kernel-level immunity, run: sudo $0"
fi
