import boto.ec2
import json

class ec2():
    def __init__(self,regiao,aaki,asak):
        self.regiao=regiao
        self.aaki=aaki
        self.asak=asak
        self.interface = boto.ec2.connect_to_region(self.regiao, aws_access_key_id=self.aaki,
                                               aws_secret_access_key=self.asak)
    def listaInstancias(self,state,instancia):
        self.instancia=instancia
        self.state=state
        if self.instancia == None:
            if self.state == None:
                reserva = self.interface.get_all_instances()
            else:
                reserva = self.interface.get_all_instances(filters={'instance-state-name': self.state})
        else:
            if self.state == None:
                reserva = self.interface.get_all_instances(filters={'instance-id': self.instancia})
            else:
                reserva = self.interface.get_all_instances(filters={'instance-id': self.instancia,
                                                                    'instance-state-name': self.state})
        for i in reserva:
            if 'Name' not in i.instances[0].tags:
                tag_name = "None"
            else:
                tag_name = i.instances[0].tags['Name']
            print(i.instances[0].id,
                  i.instances[0].ip_address,
                  i.instances[0].public_dns_name,
                  i.instances[0].private_ip_address,
                  i.instances[0].private_dns_name,
                  tag_name,
                  i.instances[0].state,
                  i.instances[0].instance_type)
    def listWithoutTag(self):
        reserva = self.interface.get_all_instances()
        for i in reserva:
            if 'Name' not in i.instances[0].tags:
                print(i.instances[0].id)
    def listarTerminate(self,instancia):
        print(instancia,self.interface.get_instance_attribute(instancia, 'disableApiTermination'))
    def bloquearInstancia(self,instancia):
        self.interface.modify_instance_attribute(instancia, 'disableApiTermination', True)
        self.listarTerminate(instancia)
    def desbloquearInstancia(self,instancia):
        self.interface.modify_instance_attribute(instancia, 'disableApiTermination', False)
        self.listarTerminate(instancia)
    def stop(self,instancia):
        self.interface.stop_instances(instancia)
    def start(self,instancia):
        self.interface.start_instances(instancia)
    def terminate(self,instancia):
        self.interface.terminate_instances(instancia)