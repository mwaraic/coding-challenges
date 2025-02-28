#!/bin/sh
pytest tests

python calc.py '( 42 * 34 ) - ( 93 / 86 ) * ( 75 - 22 )'