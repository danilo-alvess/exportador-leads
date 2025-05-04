import requests
import pandas as pd
import streamlit as st

API_KEY = 'Sua Chave de API'

API_URL = 'https://api.casadosdados.com.br/empresas/busca-avancada'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'pt-BR,pt;q=0.9',
    'Referer': 'https://casadosdados.com.br/',
    'Origin': 'https://casadosdados.com.br'
}

payload = {
    "query": {
        "uf": ["CE"],
        "municipio": [
            "FORTALEZA", "MARACANAU", "EUSEBIO", "AQUIRAZ",
            "SAO GONCALO DO AMARANTE", "CAUCAIA", "PACAJUS",
            "MARANGUAPE", "CASCAVEL", "HORIZONTE"
        ],
        "situacao_cadastral": ["ATIVA"]
    },
    "range_query": {
        "data_abertura": {
            "gte": "2024-01-01",
            "lte": "2024-03-01"
        },
        "capital_social": {
            "gte": 20000,
            "lte": 100000
        }
    },
    "mais_filtros": {
        "com_email": True,
        "somente_celular": True,
        "excluir_empresas_visualizadas": True,
        "excluir_email_contab": True
    },
    "limite": 10,
    "pagina": 1
}

response = requests.post(API_URL, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    empresas = data.get('empresas', [])
    
    if empresas:
        df = pd.DataFrame(empresas)
        st.dataframe(df)
    else:
        st.warning("Nenhuma empresa encontrada com os filtros aplicados.")
else:
    st.error(f"Erro {response.status_code}: {response.text}")
