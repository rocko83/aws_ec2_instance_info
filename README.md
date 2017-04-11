# aws_ec2_instance_info
Running aws_favil.py will output the following data in a CSV format:
INSTANCE	PUBLIC IP	PUBLIC DNS	PRIVATE IP	PRIVATE DNS	HOSTNAME	INSTANCE TYPE

usage: aws_facil.py [-h] --region REGION --access ACCESS --key KEY
                    [--listar_instancias] [--ligadas] [--instancia INSTANCIA]
                    [--bloquear BLOQUEAR] [--desbloquear DESBLOQUEAR]
                    [--verificar VERIFICAR]

optional arguments: 
  -h, --help            show this help message and exit
  --region REGION       Regiao de disponibilidade da AWS
  --access ACCESS       Chave aws_access_key_id para autencacao a AWS
  --key KEY             Segredo da chave aws_access_key_id da conta AWS
  --listar_instancias   Lista instnacias na AWS por região

Listar:
  Utilize somente com "--listar_instancias"

  --ligadas             Utilize para listar instancias ligadas
  --instancia INSTANCIA
                        Utilize para listar informações de uma instancia
                        específica. É preciso especificar o ID da instancia

disableApiTermination:  
  Verifique, bloqueie os desbloqueie o TERMINATION de instancias do EC2.

  --bloquear BLOQUEAR   Bloqueia uma instancia do EC2 para o APITermination.
  --desbloquear DESBLOQUEAR
                        Desbloqueia uma instancia do EC2 para o
                        APITermination.
  --verificar VERIFICAR 
                        Verifica se uma instancia do EC2 está bloqueada para o
                        APITermination.
