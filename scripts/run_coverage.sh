#!/usr/bin/env bash
# Run three program/test runs under coverage (parallel mode) and combine reports.
# Usage:
#   python3 -m pip install --user coverage
#   ./scripts/run_coverage.sh

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

echo "Running unit tests under coverage..."
python3 -m coverage run --parallel-mode -m unittest -v test_main.py

echo "Running object_main with test_commands.txt under coverage..."
python3 -m coverage run --parallel-mode object_main.py test_commands.txt

echo "Running object_main with input3.txt under coverage..."
python3 -m coverage run --parallel-mode object_main.py input3.txt

#This will crash the script, so commented out for now but run one time and the again with the others and then combine
# echo "Running object_main with no input under coverage..."
# python3 -m coverage run --parallel-mode object_main.py

echo "Combining coverage data files..."
python3 -m coverage combine

echo "Generating coverage report..."
python3 -m coverage report -m
python3 -m coverage html

echo "HTML report written to htmlcov/index.html"
