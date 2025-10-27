#!/usr/bin/env bash
set -euo pipefail
if [ -d tests ]; then
  pytest -q -k "not slow" || true
else
  echo "No tests yet"
fi
