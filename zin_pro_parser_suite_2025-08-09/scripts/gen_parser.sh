#!/usr/bin/env bash
set -euo pipefail

VER="4.13.1"
DIST="antlr-${VER}-complete.jar"
TOOL_DIR="tools/antlr"
OUT_DIR="compiler/gen/python"

mkdir -p "${TOOL_DIR}" "${OUT_DIR}"

if [ ! -f "${TOOL_DIR}/${DIST}" ]; then
  echo "[+] Downloading ANTLR ${VER}..."
  curl -L -o "${TOOL_DIR}/${DIST}" "https://www.antlr.org/download/${DIST}"
fi

echo "[+] Generating Python3 parser..."
java -jar "${TOOL_DIR}/${DIST}" -Dlanguage=Python3 -visitor -o "${OUT_DIR}" docs/spec/grammar/Zin.g4

echo "[+] Done. Generated in ${OUT_DIR}"
