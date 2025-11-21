# Scanner de Porta TCP SYN (Stealth Scan) em Python

---

Este é um projeto desenvolvido para fins de estudo em **cibersegurança**, focado em reconhecimento de rede e manipulação de pacotes em baixo nível.

O objetivo é simular a técnica de "Stealth Scan" (varredura furtiva), permitindo identificar portas abertas enviando pacotes SYN customizados sem completar a conexão TCP (handshake), o que o torna mais discreto que scanners convencionais.

O sistema é executado via **linha de comando (CLI)** e utiliza privilégios de administrador para criar e injetar pacotes brutos na rede.

# Tech Stack

---

[![My Skills](https://skillicons.dev/icons?i=python,linux)](https://skillicons.dev)

## Funcionalidades

---

O sistema permite ao usuário executar as seguintes ações via terminal:

- **Envio de pacotes SYN**
    
    Constrói manualmente um pacote IP/TCP com a flag `SYN` ativada, simulando o início de uma conexão real.
- **Análise de Resposta (Flags TCP)**

    Captura a resposta do servidor alvo e verifica as flags (`SYN/ACK` ou `RST`) para determinar se a porta está aberta ou fechada.
- **Execução Privilegiada**

    O script opera em baixo nível, interagindo diretamente com a interface de rede, exigindo permissões de superusuário (sudo).
- **Tratamento de Erros**

    Mensagens claras para falhas de permissão, endereços inválidos ou timeouts.

## Estrutura de Dados e Tecnologia

---

* `Scapy`: biblioteca poderosa para manipulação interativa de pacotes de rede.
* `TCP/IP Handshake`: aplicação prática dos conceitos de conexão (SYN -> SYN/ACK -> ACK).
* `Raw Sockets`: uso de sockets brutos para controle total do cabeçalho do pacote.

A escolha dessas ferramentas visa aprofundar o entendimento sobre como os protocolos de rede funcionam "por baixo do capô".

## Como Executar

---

Este projeto depende da biblioteca externa `scapy` e requer privilégios de administrador (root/sudo).

**1. Clone o repositório:**
```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

### Configuração e Execução por Sistema

#### Linux / MacOS

**2. Prepare o ambiente:**

Recomenda-se o uso de um ambiente virtual, mas lembre-se que o ```sudo``` precisa ter acesso às bibliotecas.
```bash
   # Crie e ative a venv
   python3 -m venv venv
   source venv/bin/activate
   
   # Instale as dependências
   pip install -r requirements.txt
```

**3. Execute a ferramenta:**

⚠️ Nota: Como o Scapy envia pacotes brutos, é necessário usar sudo. Aponte para o python dentro da venv:
```bash
   sudo venv/bin/python3 syn_canner.py
```

#### Windows
**Pré-requisito Extra:** Para o Scapy funcionar corretamente no Windows manipulando pacotes, você deve instalar o Npcap (selecione a opção "Install Npcap in WinPcap API-compatible Mode" durante a instalação).

**2. Prepare o ambiente (PowerShell)**
```powershell
    # Crie e ative a venv
    python -m venv venv
    
    # Instale as dependências
    pip install -r requirements.txt
```

**3. Execute a ferramenta: ⚠️ Nota:** Abra seu terminal (CMD ou PowerShell) como Administrador (Botão direito -> Executar como Administrador).
```powershell
   python syn_scanner.py
```

---

**4. Interação: O programa solicitará os dados no terminal:**
```bash
    Enter Target IP: 192.168.1.10
    Enter Target Port: 80
```

**5. O resultado será exibido informando se a porta está ABERTA (Open), FECHADA (Closed) ou FILTRADA.**

## Estrutura de Arquivos

---

O projeto segue uma estrutura simples e objetiva:
```bash
   📂 python-port-scanning/
   ├── syn_scanner.py           # Arquivo principal com a lógica do Scapy
   ├── requirements.txt         # Lista de dependências (scapy)
   └── README.md                # Documentação
```