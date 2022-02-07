#!/bin/bash
echo "export requirements.txt"
poetry export -o requirements.txt --without-hashes
poetry export -o requirements-dev.txt --dev --without-hashes
echo "autoflake"
autoflake --recursive --in-place  \
        --remove-unused-variables \
        --remove-all-unused-imports  \
        --ignore-init-module-imports \
        tw_complex
echo "black"
black tw_complex
echo "isort"
isort tw_complex
echo "flake8"
flake8 tw_complex --count --statistics
echo "OK"