#!/bin/bash

PYTHON_EXE=$(which python)

$PYTHON_EXE create_tables.py

RC=$(echo $?)

[ "${RC}" = "0" ] && $PYTHON_EXE etl.py
