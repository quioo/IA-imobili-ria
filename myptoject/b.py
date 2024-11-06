import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_excel('database_imoveis.xlsx')

print(df.head())

X = df[['Tamanho (m²)', 'Nº de Quartos', 'Nº de Banheiros', 'Idade da Casa (anos)', 'Distância ao centro (km)']]
y = df['Preço (R$)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de regressão linear
model = LinearRegression()

# Treinar o modelo com os dados de treino
model.fit(X_train, y_train)

# Fazer previsões nos dados de teste
y_pred = model.predict(X_test)

# Avaliar o desempenho do modelo com o erro quadrático médio
mse = mean_squared_error(y_test, y_pred)
print(f'Erro Quadrático Médio (MSE): {mse}')

# Exibir os coeficientes das variáveis independentes
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coeficiente'])
print(coefficients)


