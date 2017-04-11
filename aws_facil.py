#!/usr/bin/env python
import sys
import os
import time
import atexit
import argparse
import getpass
import classes.ec2 as ec2
def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--region',
                        required=True,
                        action='store',
                        help='Regiao de disponibilidade da AWS')

    parser.add_argument('--access',
                        required=True,
                        action='store',
                        help="Chave aws_access_key_id para autencacao a AWS")

    parser.add_argument('--key',
                        required=True,
                        action='store',
                        help='Segredo da chave aws_access_key_id da conta AWS')
    parser.add_argument('--listar_instancias',
                        required=False,
                        action='store_true',
                        help='Lista instnacias na AWS por região')
    listar = parser.add_argument_group('Listar', 'Utilize somente com "--listar_instancias"')
    listar.add_argument('--ligadas',
                        required=False,
                        action='store_true',
                        help='Utilize para listar instancias ligadas')
    args = parser.parse_args()
    return args
args = get_args()
sys.path.insert(0,'./classes')
instancia = ec2.ec2(args.region, args.access, args.key)
if args.listar_instancias == True:
    if args.ligadas == True:
        instancia.listarInstanciasLigadas()
    else:
        instancia.listaInstancias()

