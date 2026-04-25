# DCTF PDF Sheet Generator

Ferramenta que lê PDFs de DCTFs (Declaração de Débitos e Créditos Tributários Federais) e extrai os dados relevantes para uma planilha Excel (`.xlsx`).

## Dados extraídos

Para cada declaração encontrada nos PDFs, os seguintes dados são extraídos e organizados como colunas na planilha:

| Coluna | Descrição |
|---|---|
| `CÓDIGO RECEITA` | Código da receita federal |
| `PERÍODO DE APURAÇÃO` | Mês/ano ou trimestre/ano de apuração |
| `DÉBITO APURADO` | Valor do débito apurado |
| `ARQUIVO DE ORIGEM` | Nome do arquivo PDF de origem |

As linhas da planilha são ordenadas pelo período de apuração.

## Estrutura de pastas

```
dctf-pdf-sheet-generator/
├── main.py                         # Ponto de entrada da aplicação
├── requirements.txt                # Dependências Python
├── pdfs/                           # Pasta padrão para os PDFs de entrada
└── src/
    ├── argparsers/
    │   ├── argparser.py            # Interface base para parsers de argumentos
    │   └── declaration_argparser.py# Parser dos argumentos de linha de comando
    ├── builders/
    │   └── declaration_builder.py  # Orquestra a leitura dos PDFs e a construção da planilha
    ├── fields/
    │   ├── field.py                # Interface base para campos extraídos
    │   ├── code_field.py           # Campo: código de receita
    │   ├── debit_field.py          # Campo: débito apurado
    │   ├── filename_field.py       # Campo: nome do arquivo de origem
    │   └── period_field.py         # Campo: período de apuração
    └── pdf_readers/
        ├── pdf_reader.py           # Interface base para leitores de PDF
        └── py_mu_pdf_reader.py     # Implementação com PyMuPDF
```

## Como rodar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Coloque os PDFs na pasta de entrada

Por padrão, o programa lê todos os arquivos `.pdf` da pasta `pdfs/`. Você pode usar outra pasta via argumento.

### 3. Execute

```bash
python main.py
```

Isso irá gerar o arquivo `declarations.xlsx` no diretório atual.

### Argumentos opcionais

| Argumento | Padrão | Descrição |
|---|---|---|
| `-f`, `--folder` | `pdfs` | Caminho para a pasta com os PDFs |
| `-o`, `--output` | `declarations.xlsx` | Caminho para o arquivo de saída |

**Exemplo com argumentos personalizados:**

```bash
python main.py -f /caminho/para/pdfs -o resultado.xlsx
```
