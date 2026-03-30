import socket
import os
import random

def limpar_tela():
    os.system("clear")

ports = [21,22,80,443,445,3306]

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

while True:

 limpar_tela()

 print(f"{RED}-{RESET}"*49)
 ASCII_art = [f"""{GREEN}

██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝

██████╗  ██████╗ ██████╗ ████████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝ ██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝██║   ██║██████╔╝   ██║    ███████╗██║     ███████║██╔██╗ ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║    ╚════██║██║     ██╔══██║██║╚██╗██║
██║     ╚██████╔╝██║  ██║   ██║    ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ {RESET}

        ╔═══ ══════════════════════════════════╗
       ║ {GREEN}  DOMAIN  PORTSCAN {RESET}                   ║
        ║   {BLUE}scanning ports...{RESET} [{RED}■■■■■■■■■■{RESET}]     ║
        ║   status: {GREEN}ACTIVE{RESET}                     ║
        ╚══════════════════════════════ ═══════╝

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
║        >>>  PORT SCANNER  <<<       ║
╚══════════════════════════════════════╝
                   {RESET}""",

f"""{GREEN}
░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░ ░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░ ░▒▓█▓▒░      
░▒▓███████▓▒░░▒▓████████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░ ░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░ ░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░ ░▒▓███████▓▒░

        >> scanning ports... <<
                   {RESET}""",

f"""{GREEN}
██████████████████████████████
█▄─▄▄▀█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█
██─▄─▄██─▄█▀██─██─██─▄█▀█▄▄▄▄─█
▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀
      PORT SCAN CORE
                   {RESET}""",
]
 escolha = random.choice(ASCII_art)
 print(escolha)
 print(f"{RED}-{RESET}"*49)in
main


 opcao = int(input(f"[{RED}1{RESET}]-{BLUE}Port verification for a website or loopback{RESET}\n[{RED}2{RESET]-{BLUE}Help{RESET}\n[{RED}3{RESET}]-{BLUET}exit{RESET}\n{BLUE}:{RESET}"))
 if opcao == 1:
  limpar_tela()
  domain = str(input("Escreva o website ou lo...\n:"))
  for port in ports:
      client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client.settimeout(0.1)
      code = client.connect_ex((domain, port))
      if code == 0:
         print(port,"---> OPEN")

      else:
         print(port,"---> CLOSED")
  exit = input("")

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
