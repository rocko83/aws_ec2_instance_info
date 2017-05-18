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
    listar.add_argument('--instancia',
                        required=False,
                        action='store',
                        help='Show data for a specific instance')
    listar.add_argument('--state',
                        required=False,
                        action='store',
                        help='Especify the state of the instaces for filtering. Ex.: pending | running | shutting-down | terminated | stopping | stopped')
    listar.add_argument('--without_tag',
                        required=False,
                        action='store_true',
                        help='Show instances which do not have tag Name')
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
    manage=bloqueio = parser.add_argument_group('Manage Instance status', 'Stop/Start/Terminate an EC2 instance')
    manage.add_argument('--start',
                        required=False,
                        action='store',
                        help='Start an AWS EC2 instance')
    manage.add_argument('--stop',
                        required=False,
                        action='store',
                        help='Stop an AWS EC2 instance')
    manage.add_argument('--terminate',
                        required=False,
                        action='store',
                        help='Terminate an AWS EC2 instance')
    args = parser.parse_args()

    return args
def erroExclusaoMutua():
    print("Erro, two or more arguments was passed to a mutual exclusive operation")
    exit(1)
args = get_args()
sys.path.insert(0,'./classes')
instancia = ec2.ec2(args.region, args.access, args.key)
if args.listar_instancias == True:
    if args.state is not None:
        instancia.listaInstancias(args.state,None)
    else:
        if args.without_tag == True:
            instancia.listWithoutTag()
        else:
            if args.instancia is not None:
                instancia.listaInstancias(None,None)
            else:
                instancia.listaInstancias(None,args.instancia)

if args.bloquear is not None:
    if args.desbloquear is not None:
        erroExclusaoMutua()
    if args.verificar is not None:
        erroExclusaoMutua()
    instancia.bloquearInstancia(args.bloquear)
    exit(0)
if args.desbloquear is not None:
    if args.bloquear is not None:
        erroExclusaoMutua()
    if args.verificar is not None:
        erroExclusaoMutua()
    instancia.desbloquearInstancia(args.desbloquear)
    exit(0)
if args.verificar is not None:
    if args.bloquear is not None:
        erroExclusaoMutua()
    if args.desbloquear is not None:
        erroExclusaoMutua()
    instancia.listarTerminate(args.verificar)
    exit(0)
if args.stop is not None:
    if args.start is not None:
        erroExclusaoMutua()
    if args.terminate is not None:
        erroExclusaoMutua()
    instancia.stop(args.stop)
    exit(0)
if args.start is not None:
    if args.stop is not None:
        erroExclusaoMutua()
    if args.terminate is not None:
        erroExclusaoMutua()
    instancia.start(args.start)
    exit(0)
if args.terminate is not None:
    if args.start is not None:
        erroExclusaoMutua()
    if args.stop is not None:
        erroExclusaoMutua()
    instancia.terminate(args.terminate)
    exit(0)