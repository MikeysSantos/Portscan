import socket
import os

def limpar_tela():
    os.system("clear")

while True:

 limpar_tela()

 print("-"*60)
 print("""

██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝

██████╗  ██████╗ ██████╗ ████████╗███████╗ ██████╗  █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝ ██╔══██╗████╗  ██║
██████╔╝██║   ██║██████╔╝   ██║   ███████╗██║  ███╗███████║██╔██╗ ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║██║   ██║██╔══██║██║╚██╗██║
██║     ╚██████╔╝██║  ██║   ██║   ███████║╚██████╔╝██║  ██║██║ ╚████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝



Ass:unixmasonry
 """)
 print("-"*60)
 opcao = int(input("Qual opção deseja?\n[1]-Verificação de portas para um website\n[2]-Help\n[3]-Exit\n:"))
 if opcao == 1:
   limpar_tela()
   domain = str(input("Escreva o website...\n:"))
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.settimeout(5)
   code = client.connect_ex((domain, 80))
   if code == 0:
    print("80  ---> OPEN")
    print("Conexão sucedida")
    sair = input("")
   else:
    print("80  ---> CLOSED")
    print("Tempo de espera maxima atingida, conexão recusada.")
    sair = input("")
 elif opcao == 2:
   limpar_tela()
   print("""
==================== HELP ====================

DOMAIN_PORTSCAN - Scanner básico de portas

Este script permite verificar se a porta 80 (HTTP)
de um website está aberta ou fechada.

---------------- COMO USAR ----------------

[1] Verificação de portas
- Escolha a opção 1
- Digite o domínio do site (ex: google.com)
- O script tentará se conectar na porta 80

---------------- RESULTADOS ----------------

OPEN   -> Porta aberta (conexão bem sucedida)
CLOSED -> Porta fechada ou bloqueada

---------------- OBSERVAÇÕES ----------------

- O script usa conexão TCP (socket)
- Tempo máximo de espera: 5 segundos
- Atualmente verifica apenas a porta 80

---------------- EXEMPLO ----------------

Entrada:
1
google.com

Saída:
80 ---> OPEN

===========================================

""")
   sair = input("")
 elif opcao == 3:
   limpar_tela()
   break

 else:
   limpar_tela()
   print("Opção não encontrada...")
   sair = input("")
