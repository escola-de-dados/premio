import csv
import yaml

# Mapeamento dos campos do CSV para os campos do YAML
mapa_campos = {
    'title': 'Título do trabalho',
    'project_url': 'link',
    'veiculo': 'Veículo ou organização',
    'autoria': 'Autores(as) do trabalho',
    'data': 'Data de publicação',
    'resumo': 'Resumo do trabalho',
    'relevância': 'Relevância',
    'originalidade': 'Originalidade',
    'metodologia': 'Metodologia',
    'uf': 'UF',
    'tipo_inscricao': 'Categoria_inscrita',
    'formato': 'Formato',
    'category': 'Categoria_inscrita',
    'image': 'Imagem de destaque'  # Agora pega da coluna "Imagem de destaque"
}

# Tenta carregar dados YAML existentes (ou inicializa vazio)
try:
    with open('template.yaml', 'r', encoding='utf-8') as f:
        yaml_data = yaml.safe_load(f) or []
except FileNotFoundError:
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

# Exporta com indentação correta
with open('template.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(
        yaml_data,
        f,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        indent=2  # Garante indentação de 2 espaços
    )
