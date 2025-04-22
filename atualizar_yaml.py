import csv
import yaml

# Mapeamento dos campos do CSV para os campos do YAML
mapa_campos = {
    'title': 'title',
    'project_url': 'Link',
    'veiculo': 'veiculo',
    'autoria': 'autoria',
    'data': 'data',
    'resumo': 'resumo',
    'relevância': 'relevância',
    'originalidade': 'originalidade',
    'metodologia': 'metodologia',
    'uf': 'uf',
    'tipo_inscricao': 'tipo_inscricao',
    'formato': 'formato',
    'category': 'tipo_inscricao',
    'image': 'image'  # Agora pega da coluna "Imagem de destaque"
}

# Lista para armazenar os dados que irão para o arquivo YAML
yaml_data = []

# Lê e converte dados do CSV
with open('dados.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        entrada = {}
        for campo_yaml, campo_csv in mapa_campos.items():
            valor = row.get(campo_csv, "").strip()
            if campo_yaml == 'image':  # Adiciona o caminho correto para o campo image
                valor = f"images/edicoes/2024/{valor}"
            entrada[campo_yaml] = valor
        entrada['ano'] = '2024'  # Ano fixo
        yaml_data.append(entrada)

# Exporta os dados para o arquivo 'projetos.yaml'
with open('projetos.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(
        yaml_data,
        f,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        indent=2
    )

print("Arquivo 'projetos.yaml' criado com sucesso!")
