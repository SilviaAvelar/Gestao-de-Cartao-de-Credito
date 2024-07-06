import plotly.express as px

def grafico_gastos_por_categoria_pie(valor_gasto_por_categoria):
    fig_pizza = px.pie(valor_gasto_por_categoria, values='ValorCompra', names='categoria', title='Gastos por Categoria')
    return fig_pizza

def grafico_gastos_por_categoria(valor_gasto_por_categoria):
    fig_barra = px.bar(valor_gasto_por_categoria, x='categoria', y='ValorCompra', 
                        title='Gastos por Categoria',
                        labels={'categoria': 'Categoria', 'ValorCompra': 'Valor Gasto'},
                        color='categoria', 
                        color_discrete_sequence=px.colors.qualitative.Pastel)
    return fig_barra


def grafico_gastos_por_titular(valor_gasto_por_titular):
    fig_barra = px.bar(valor_gasto_por_titular, x='Titular', y='ValorCompra', title='Gastos por Titular', labels={'Titular': 'Titular do Cartão', 'ValorCompra': 'Valor Gasto'}, color='Titular')
    return fig_barra

def grafico_gastos_ao_longo_do_tempo(gastos_ao_longo_do_tempo):
    fig_linha = px.line(gastos_ao_longo_do_tempo, x='data_compra', y='ValorCompra', title='Valor Total Gasto ao Longo do Tempo', labels={'data_compra': 'Data da Compra', 'ValorCompra': 'Valor Gasto'})
    return fig_linha
