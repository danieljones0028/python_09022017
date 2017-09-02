#!/usr/bin/env python3
import docker
import argparse

# def criar_container(imagem, comando):
    # cliente = docker.from_env()
    # executando = cliente.containers.run(imagem, comando)
    # print(executando)
# 
# 
# com args
def criar_container(args):
    cliente = docker.from_env()
    executando = cliente.containers.run(args.imagem, args.comando)
    print(executando)
    return(executando)
# 
# 

def listar_containers():
    client = docker.from_env()
    get_all = client.containers.list(all)
    for cada_container in get_all:
        conectando = client.containers.get(cada_container.id)
        print("O container %s utiliza a imagem %s rodando o comando %s" % (conectando.short_id, conectando.attrs['Config']['Image'], conectando.attrs['Config']['Cmd']))

def procurar_container(imagem):
    client = docker.from_env()
    get_all = client.containers.list(all)
    for cada_container in get_all:
        conectando = client.containers.get(cada_container.id)
        imagem_container = conectando.attrs['Config']['Image']
        if str(imagem).lower() in str(imagem_container).lower():
            print("Achei o container %s q contem a palavrfa %s no nome da sua imagem: %s" % (cada_container.short_id, imagem, imagem_container))
# listas container
# verificar portar que estao blindando
# se for menor de 1024 deve remover o container


def remover_container():
    client = docker.from_env()
    get_all = client.containers.list(all)
    for cada_container in get_all:
        conectando = client.containers.get(cada_container.id)
        portas = conectando.attrs['HostConfig']['PortBindings']
        portas = str(portas)
        portas2 = ''.join(filter(str.isdigit, portas))
        # print(portas)
        # print(portas2)
        if portas2 <= str(801024):
            print ("porta e maior que 1024 o container não sera removido.")
        else:
            print("A porta e menor que 1024 o container sera removido")
            conectando.remove(force=True)


# Jeferson que fez
# def remover_container():
    # client = docker.from_env()
    # get_all = client.containers.list(all)
    # for cada_container in get_all:
        # conectando = client.containers.get(cada_container.id)
        # portas = conectando.attrs['HostConfig']['PortBindings']
        # if isinstance(portas,dict):
            # for porta, porta1, in portas.items():
                # porta1 = str(porta1)
                # porta2 = ''.join(filter(str.isdigit, porta1))
                # if int("Removendo o container %s que esta escutando na orta %s e bindando no host na porta %s" % (i.short_id, porta, porta2))
                # removendo = i.remove(force=True)

parser = argparse.ArgumentParser(description="docker-cli criado na aula de python")
subparser = parser.add_subparsers()
# 
criar_opt = subparser.add_parser('criar')
criar_opt.add_argument('--imagem', required=True)
criar_opt.add_argument('--comando', required=True)
criar_opt.set_defaults(func=criar_container)

cmd = parser.parse_args()
cmd.func(cmd)

# listar_containers()
# criar_container("alpine", "echo VAIIII")
# procurar_container("nginx")
# remover_container()