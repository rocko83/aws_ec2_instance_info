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
                        help='Select the avaiability zone')

    parser.add_argument('--access',
                        required=True,
                        action='store',
                        help="The access ID for a AWS account with EC2 credential")

    parser.add_argument('--key',
                        required=True,
                        action='store',
                        help='Secret id for the access ID')
    parser.add_argument('--listar_instancias',
                        required=False,
                        action='store_true',
                        help='List instances per region')
    listar = parser.add_argument_group('List', 'Use only with "--listar_instancias"')
    listar.add_argument('--ligadas',
                        required=False,
                        action='store_true',
                        help='List instances in "running" state')
    listar.add_argument('--instancia',
                        required=False,
                        action='store',
                        help='Show data for a specific instance')
    bloqueio = parser.add_argument_group('disableApiTermination', 'Checks wherever a EC2 instance has the termination API enabled')
    bloqueio.add_argument('--bloquear',
                          required=False,
                          action='store',
                          help='Disable the Termination protection')
    bloqueio.add_argument('--desbloquear',
                          required=False,
                          action='store',
                          help='Enable the termination protection')
    bloqueio.add_argument('--verificar',
                          required=False,
                          action='store',
                          help='Print the termination protection flag for a specific instance')
    args = parser.parse_args()

    return args
def erroExclusaoMutuaBloqueio():
    print("Erro, more than one argumente was passed for the APITermination protection.")
    exit(1)
args = get_args()
sys.path.insert(0,'./classes')
instancia = ec2.ec2(args.region, args.access, args.key)
if args.listar_instancias == True:
    if args.ligadas == True:
        instancia.listarInstanciasLigadas()
    else:
        if args.instancia == None:
            instancia.listaInstancias(None)
        else:
            instancia.listaInstancias(args.instancia)
if args.bloquear is not None:
    if args.desbloquear is not None:
        erroExclusaoMutuaBloqueio()
    if args.verificar is not None:
        erroExclusaoMutuaBloqueio()
    instancia.bloquearInstancia(args.bloquear)
if args.desbloquear is not None:
    if args.bloquear is not None:
        erroExclusaoMutuaBloqueio()
    if args.verificar is not None:
        erroExclusaoMutuaBloqueio()
    instancia.desbloquearInstancia(args.desbloquear)
if args.verificar is not None:
    if args.bloquear is not None:
        erroExclusaoMutuaBloqueio()
    if args.desbloquear is not None:
        erroExclusaoMutuaBloqueio()
    instancia.listarTerminate(args.verificar)