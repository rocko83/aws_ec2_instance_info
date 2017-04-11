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
    listar.add_argument('--instancia',
                        required=False,
                        action='store',
                        help='Utilize para listar informações de uma instancia específica. '
                             'É preciso especificar o ID da instancia')
    bloqueio = parser.add_argument_group('disableApiTermination', 'Verifique, bloqueie os desbloqueie o TERMINATION de instancias do EC2.')
    bloqueio.add_argument('--bloquear',
                          required=False,
                          action='store',
                          help='Bloqueia uma instancia do EC2 para o APITermination.')
    bloqueio.add_argument('--desbloquear',
                          required=False,
                          action='store',
                          help='Desbloqueia uma instancia do EC2 para o APITermination.')
    bloqueio.add_argument('--verificar',
                          required=False,
                          action='store',
                          help='Verifica se uma instancia do EC2 está bloqueada para o APITermination.')
    args = parser.parse_args()

    return args
def erroExclusaoMutuaBloqueio():
    print("Erro, mais de um arqgumento do bloqueio de API foi passado")
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