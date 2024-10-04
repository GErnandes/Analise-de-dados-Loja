import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Inicializar o estado da sessão se não estiver presente
if 'data' not in st.session_state:
    # Carregar o DataFrame
    df_data = pd.read_csv("dataset/Base_de_Dados_Prova_1(Detalhe de Vendas).csv", sep=";", decimal=",", index_col=0, encoding='ISO-8859-1')
    st.session_state['data'] = df_data

st.title('Dashboard de Vendas')

# Calcular o valor total de vendas
valor_total_vendas = st.session_state['data']['Valor de venda'].sum()

# Calcular o valor total de vendas
valor_total_salario = st.session_state['data']['Salario total'].sum()

col1, col2 = st.columns(2)
col1.metric(label="Valor Total de Vendas", value=f"R$ {valor_total_vendas:,.2f}")
col2.metric(label="Valor Total dos Salários", value=f"R$ {valor_total_salario:,.2f}")


# Calcular os 10 produtos mais vendidos em quantidade
produtos_mais_vendidos_qtd = (st.session_state['data']
                           .groupby('Nome Produto', as_index=False)['Quantidade']
                           .sum()
                           .sort_values(by='Quantidade', ascending=False)
                           .head(10))

produtos_mais_vendidos_valor = (st.session_state['data']
                                  .groupby('Nome Produto', as_index=False)['Valor de venda']
                                  .sum()
                                  .sort_values(by='Valor de venda', ascending=False)
                                  .head(10)
                                  .round(2))

top10_clientes = (st.session_state['data']
                                  .groupby('Cliente', as_index=False)['Valor de venda']
                                  .sum()
                                  .sort_values(by='Valor de venda', ascending=False)
                                  .head(10)
                                  .round(2))

top10_vendedores = (st.session_state['data']
                                  .groupby('Vendedor', as_index=False)['Valor de venda']
                                  .sum()
                                  .sort_values(by='Valor de venda', ascending=False)
                                  .head(10)
                                  .round(2))

top10_categorias_qtd= (st.session_state['data']
                                  .groupby('Categoria', as_index=False)['Quantidade']
                                  .sum()
                                  .sort_values(by='Quantidade', ascending=False)
                                  .head(10))
                                  
top10_categorias_vlr= (st.session_state['data']
                                  .groupby('Categoria', as_index=False)['Valor de venda']
                                  .sum()
                                  .sort_values(by='Valor de venda', ascending=False)
                                  .head(10)
                                  .round(2))



# Exibir os 10 produtos mais vendidos em grafico
fig_qtd = px.bar(produtos_mais_vendidos_qtd,
                   x='Quantidade',
                   y='Nome Produto',
                   orientation='h',
                   title='Top 10 Produtos Mais Vendidos em Quantidade',
                   labels={'Quantidade': 'Quantidade Vendida', 'Nome Produto': 'Nome do Produto'},
                   color='Quantidade',
                   text='Quantidade',  # Mostrar os números exatos
                   color_continuous_scale=px.colors.sequential.Viridis,
                   category_orders={'Nome Produto': produtos_mais_vendidos_qtd['Nome Produto'].tolist()})  # Ordenar do maior para o menor


# Criar gráfico de barras para produtos mais vendidos em valor
fig_valor = px.bar(produtos_mais_vendidos_valor,
                   x='Valor de venda',
                   y='Nome Produto',
                   orientation='h',
                   title='Top 10 Produtos Mais Vendidos em Valor de Venda',
                   labels={'Valor de venda': 'Valor de Venda (R$)', 'Nome Produto': 'Nome do Produto'},
                   color='Valor de venda',
                   text='Valor de venda',  # Mostrar os números exatos
                   color_continuous_scale=px.colors.sequential.Viridis,
                   category_orders={'Nome Produto': produtos_mais_vendidos_valor['Nome Produto'].tolist()})


# Exibir os 10 produtos mais vendidos em grafico
fig_cliente = px.bar(top10_clientes,
                   x='Valor de venda',
                   y='Cliente',
                   orientation='h',
                   title='Top 10 Clientes que mais Compram',
                   labels={'Valor de venda': 'Valor de Venda (R$)', 'Cliente': 'Nome do Cliente'},
                   color='Valor de venda',
                   text='Valor de venda',  # Mostrar os números exatos
                   color_continuous_scale=px.colors.sequential.Viridis,
                   category_orders={'Cliente': top10_clientes['Cliente'].tolist()})  # Ordenar do maior para o menor



                   
# Exibir os 10 produtos mais vendidos em grafico
fig_vendedor = px.bar(top10_vendedores,
                   x='Valor de venda',
                   y='Vendedor',
                   orientation='h',
                   title='Top 10 Vendedores que mais Vendem',
                   labels={'Valor de venda': 'Valor de Venda (R$)', 'Vendedor': 'Nome do Vendedor'},
                   color='Valor de venda',
                   text='Valor de venda',  # Mostrar os números exatos
                   color_continuous_scale=px.colors.sequential.Viridis,
                   category_orders={'Vendedor': top10_vendedores['Vendedor'].tolist()})  # Ordenar do maior para o menor

# Exibir os 10 categorias mais vendidas em quantidade  em grafico
fig_categoria = px.bar(top10_categorias_qtd,
                   x='Quantidade',
                   y='Categoria',
                   orientation='h',
                   title='Top 10 Categorias que mais vendem em Quantidade',
                   labels={'Quantidade': 'Quantidade Vendida (R$)', 'Categoria': 'Categorias'},
                   color='Quantidade',
                   text='Quantidade',  # Mostrar os números exatos
                   color_continuous_scale=px.colors.sequential.Viridis,
                   category_orders={'Categoria': top10_categorias_qtd['Categoria'].tolist()})  # Ordenar do maior para o menor

# Exibir os 10 produtos mais vendidos em grafico
fig_categoria2 = px.bar(top10_categorias_vlr,
                   x='Valor de venda',
                   y='Categoria',
                   orientation='h',
                   title='Top 10 Categorias que mais vendem em Valor de Venda',
                   labels={'Valor de venda': 'Valor de Venda (R$)', 'Categoria': 'Categorias'},
                   color='Valor de venda',
                   text='Valor de venda',  # Mostrar os números exatos
                   color_continuous_scale=px.colors.sequential.Viridis,
                   category_orders={'Categoria': top10_categorias_vlr['Categoria'].tolist()})  # Ordenar do maior para o menor


st.plotly_chart(fig_qtd)
st.plotly_chart(fig_valor)
st.plotly_chart(fig_categoria)
st.plotly_chart(fig_categoria2)
st.plotly_chart(fig_cliente)
st.plotly_chart(fig_vendedor)
