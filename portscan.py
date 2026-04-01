import socket
import os
import random
import dns.resolver

def limpar_tela():
    os.system("clear")

ports = [21,22,80,443,445,3306]

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"
BLUES = "\033[38;2;0;255;255m"

while True:

 limpar_tela()

 ASCII_art = [f"""{GREEN}
╔═════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                     ║
║ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗                                   ║
║ ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║                                   ║
║ ██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║                                   ║
║ ██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║                                   ║
║ ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║                                   ║
║ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝                                   ║
║                                                                                     ║
║ ██████╗  ██████╗ ██████╗ ████████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗               ║
║ ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝ ██╔════╝██╔════╝██╔══██╗████╗  ██║               ║
║ ██████╔╝██║   ██║██████╔╝   ██║    ███████╗██║     ███████║██╔██╗ ██║               ║
║ ██╔═══╝ ██║   ██║██╔══██╗   ██║    ╚════██║██║     ██╔══██║██║╚██╗██║               ║
║ ██║     ╚██████╔╝██║  ██║   ██║    ███████║╚██████╗██║  ██║██║ ╚████║               ║
║ ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ {RESET}{GREEN}           /
║                                                                                     ║
║       {RESET}  ╔══════════════════════════════════════╗{GREEN}                                    /.
║       {RESET}  ║ {GREEN}  DOMAIN  PORTSCAN {RESET}                   ║ {GREEN}                           "
║       {RESET}  ║   {BLUE}scanning ports...{RESET} [{RED}■■■■■■■■■■{RESET}]     ║{GREEN}                       .:
║       {RESET}  ║   status: {GREEN}ACTIVE{RESET}                     ║{GREEN}                                 -_
║       {RESET}  ╚══════════════════════════════ ═══════╝{GREEN}                                    ,:;
╚═════════════════════════════════════════════════════════════════════════════════════╝{RESET}
             {GREEN}>>> ACCESS GRANTED <<<{RESET}

""",

f"""{GREEN}
╔══════════════════════════════════════╗
║  ██████╗  ██████╗ ██████╗ ████████╗  ║
║  ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝  ║
║  ██████╔╝██║   ██║██████╔╝   ██║     ║
║  ██╔═══╝ ██║   ██║██╔══██╗   ██║     ║
║  ██║     ╚██████╔╝██║  ██║   ██║     ║
║  ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝     ║
║       {RESET} {BLUES}>>>  PORT SCANNER  <<<{RESET}{GREEN}       ║
╚══════════════════════════════════════╝{RESET}
                   """,

f"""{GREEN}
░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░ ░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░ ░▒▓█▓▒░      
░▒▓███████▓▒░░▒▓████████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░ ░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░ ░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░ ░▒▓███████▓▒░
{RESET}
       {RED} >> scanning ports... << {RESET}
                   """,

f"""{GREEN}
██████████████████████████████
█▄─▄▄▀█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█
██─▄─▄██─▄█▀██─██─██─▄█▀█▄▄▄▄─█
▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀ {RESET}
      {RED}PORT SCAN CORE{RESET}
                   """,
]
 escolha = random.choice(ASCII_art)
 print(escolha)
 opcao = int(input(f"Qual opção deseja?\n\n{RED}[1]{RESET}-{BLUES}Verificação de portas para um website ou loopback{RESET}\n{RED}[2]{RESET}-{BLUES}IPV4 de um website{RESET}\n{RED}[3]{RESET}-{BLUES}Help{RESET}\n{RED}[4]{RESET}-{BLUES}exit{RESET}\n{BLUES}:{RESET}"))
 if opcao == 1:
  limpar_tela()
  domain = str(input(f"{BLUES}Escreva o website ou lo...\n:{RESET}"))
  for port in ports:
      client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client.settimeout(0.1)
      code = client.connect_ex((domain, port))
      if code == 0:
         print(port,f"{BLUES}---> OPEN{RESET}")

      else:
         print(port,f"{RED}---> CLOSED{RESET}")
  exit = input("")

 elif opcao == 3:
   limpar_tela()
   print(f"""{BLUES}
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
{RESET}""")
   sair = input("")

 elif opcao == 2:
   limpar_tela()
   res = dns.resolver.Resolver()
   alvo = str(input(f"{BLUES}Diga o website\n:{RESET}"))
   registro_dns = str(input(f"{BLUES}registro_dns\n:{RESET}"))
   resultado = res.resolve(alvo, registro_dns)
   limpar_tela()
   for info in resultado:
      print(alvo, "tem endereço", info)
   exit = input("")

 elif opcao == 4:
   limpar_tela()
   break

 else:
   limpar_tela()
   print(f"{RED}Opção não encontrada...{RESET}")
