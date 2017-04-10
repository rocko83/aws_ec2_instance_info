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

    parser.add_argument('-r', '--region',
                        required=True,
                        action='store',
                        help='Regiao de disponibilidade da AWS')

    parser.add_argument('-a', '--access',
                        required=True,
                        action='store',
                        help="Chave aws_access_key_id para autencacao a AWS")

    parser.add_argument('-k', '--key',
                        required=True,
                        action='store',
                        help='Segredo da chave aws_access_key_id da conta AWS')

    args = parser.parse_args()
    return args
args = get_args()
sys.path.insert(0,'./classes')
instancia = ec2.ec2(args.region, args.access, args.key)
instancia.listaInstancias()

