import boto.ec2

class ec2():
    def __init__(self,regiao,aaki,asak):
        self.regiao=regiao
        self.aaki=aaki
        self.asak=asak
        self.interface = boto.ec2.connect_to_region(self.regiao, aws_access_key_id=self.aaki,
                                               aws_secret_access_key=self.asak)
    def listaInstancias(self):
        reserva = self.interface.get_all_instances()
        for i in reserva:
            print(i.instances[0].id + "," +
                  i.instances[0].ip_address + "," +
                  i.instances[0].public_dns_name + "," +
                  i.instances[0].private_ip_address + "," +
                  i.instances[0].private_dns_name + "," +
                  i.instances[0].tags['Name'] + "," +
                  i.instances[0].state + "," +
                  i.instances[0].instance_type)
        #print(dir(reserva[0].instances[0]))
    def listarInstanciasLigadas(self):
        reserva = self.interface.get_all_instances()
        for i in reserva:
            if i.instances[0].state == "running" :
                print(i.instances[0].id + "," +
                      i.instances[0].ip_address + "," +
                      i.instances[0].public_dns_name + "," +
                      i.instances[0].private_ip_address + "," +
                      i.instances[0].private_dns_name + "," +
                      i.instances[0].tags['Name'] + "," +
                      i.instances[0].state + "," +
                      i.instances[0].instance_type)
            # print(dir(reserva[0].instances[0]))