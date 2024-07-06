## Pessoal,  antes de rodar o código, é necessário instalar as bibliotecas abaixo
## O arquivo plotting.py tem que estar no mesmo diretório desse arquivo.

## pip install streamlit
## pip install pandas
## Para executar o código, rode o arquivo Executa_Analise.bat 

import streamlit as st
import pandas as pd
import plotting

# Carregar os dados
df = pd.read_csv('dados_cartao_convertido.csv')

# Adicionar coluna com os nomes dos titulares dos cartões
df['Titular'] = df['NumeroCartao'].map({
    7840517590708225: 'João',
    7142474765870246: 'Ana'
})

# Converter a coluna NumeroCartao para string
df['NumeroCartao'] = df['NumeroCartao'].astype(str)

# Convertendo a coluna data_compra para datetime
df['data_compra'] = pd.to_datetime(df['data_compra'])

# Calcular o valor total do cartão
valor_total_cartao = df['ValorCompra'].sum()

# Calcular o valor gasto por titular
valor_gasto_por_titular = df.groupby('Titular')['ValorCompra'].sum().reset_index()

# Calcular o valor gasto por categoria
valor_gasto_por_categoria = df.groupby('categoria')['ValorCompra'].sum().reset_index()

# Gráfico de barras dos gastos por categoria
fig_barra_categoria = plotting.grafico_gastos_por_categoria(valor_gasto_por_categoria)

# Gráfico de pizza dos gastos por categoria
#fig_barra_categoria_pizza = plotting.grafico_gastos_por_categoria_pie(valor_gasto_por_categoria)

# Gráfico de barras dos gastos por titular com cores diferentes
fig_barra_titular = plotting.grafico_gastos_por_titular(valor_gasto_por_titular)

# Gráfico de linha do valor total gasto ao longo do tempo
gastos_ao_longo_do_tempo = df.groupby('data_compra')['ValorCompra'].sum().reset_index()
fig_linha = plotting.grafico_gastos_ao_longo_do_tempo(gastos_ao_longo_do_tempo)

# Interface do Streamlit
st.set_page_config(layout="centered")
st.title('Compras de Cartão de Crédito')

st.header('Informações Gerais')
st.write(f'Valor total gasto: R$ {valor_total_cartao:.2f}')

st.header('Valor Gasto por Titular')
st.dataframe(valor_gasto_por_titular)

st.header('Valor Gasto por Categoria')
st.dataframe(valor_gasto_por_categoria)

st.header('Gráficos')
st.subheader('Gastos por Categoria')
st.plotly_chart(fig_barra_categoria)

st.subheader('Gastos por Titular')
st.plotly_chart(fig_barra_titular)

st.subheader('Valor Total Gasto ao Longo do Tempo')
st.plotly_chart(fig_linha)

# Interface do Streamlit
st.title('Todas as Compras no Cartão de Crédito')
st.header('Informações Gerais')
st.dataframe(df)