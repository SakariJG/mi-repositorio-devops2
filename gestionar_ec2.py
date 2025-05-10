#!/usr/bin/env python3
import boto3
import sys
def listar_instancias():
 ec2 = boto3.resource('ec2')
 for i in ec2.instances.all():
 nombre = "Sin nombre"
 if i.tags:
 for tag in i.tags:
 if tag['Key'] == 'Name':
 nombre = tag['Value']
 print(f"{i.id}\t{i.instance_type}\t{i.state['Name']}\t{nombre}")
def iniciar_instancia(id):
 ec2 = boto3.resource('ec2')
 ec2.Instance(id).start()
 print(f"Iniciando instancia {id}")
def detener_instancia(id):
 ec2 = boto3.resource('ec2')
 ec2.Instance(id).stop()
 print(f"Deteniendo instancia {id}")
if len(sys.argv) < 2:
 print("Uso: python gestionar_ec2.py [listar|iniciar|detener] [ID_INSTANCIA]")
 sys.exit(1)
accion = sys.argv[1]
if accion == "listar":
 listar_instancias()
elif accion == "iniciar" and len(sys.argv) == 3:
 iniciar_instancia(sys.argv[2])
elif accion == "detener" and len(sys.argv) == 3:
 detener_instancia(sys.argv[2])
else:
 print("Acción inválida")
