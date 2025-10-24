# GitHub Action do PCWA
Este repositório contém uma GitHub Action que lê os dados de um arquivo CSV `dados.csv` e atualiza automaticamente o arquivo YAML `projetos.yaml` com base nessas informações.
Este fluxo ajuda a organizar as informações que estão no premio.jornalismodedados.org.br.

## O que esta Action faz

A cada push na branch main, o GitHub Action executa os seguintes passos:

1. Faz o checkout do repositório.

2. Configura o ambiente Python.

3. Instala as dependências necessárias (pyyaml).

4. Executa o script `atualizar_yaml.py`, que:

- Lê os dados do arquivo `dados.csv`;

- Cria ou atualiza o arquivo `projetos.yaml`;

- Formata os dados no formato correto, com indentação adequada e título entre aspas.

- Comita e envia automaticamente as mudanças para o repositório.

## Estrutura dos arquivos

├── atualizar_yaml.py     # Script Python que processa o CSV e gera o YAML
├── dados.csv             # Fonte de dados (entrada)
├── projetos.yaml          # Arquivo YAML gerado automaticamente
└── .github/
    └── workflows/
        └── atualizar_yaml.yml   # Arquivo do GitHub Actions

## Como utilizar

1. Faça o push de uma atualização no CSV

Sempre que você fizer uma modificação no arquivo `dados.csv` e realizar um commit/push na branch main, o GitHub Action será executado automaticamente.

2. Verifique o resultado

Após a execução, o arquivo `projetos.yaml` será atualizado e comitado automaticamente no repositório.
