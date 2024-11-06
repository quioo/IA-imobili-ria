import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib

# Carregar a base de dados
data = pd.read_excel('C:/Users/junio/OneDrive/Área de Trabalho/myptoject/database_imoveis_expandido.xlsx')

# Converter a coluna 'Garagem' para valores numéricos
data = data.rename(columns={'Garagem ': 'Garagem'})
data['Garagem'] = data['Garagem'].apply(lambda x: 1 if x == 'Sim' else 0)


# Separar as variáveis independentes (X) e a variável dependente (y)
X = data[['m²', 'qnt Quartos', 'qnt Banheiros', 'Idade', 'Garagem', 'Distância centro']]
y = data['Preço']

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar os dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Criar e compilar o modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError(), metrics=[tf.keras.metrics.MeanAbsoluteError()])

# Treinar o modelo
history = model.fit(X_train_scaled, y_train, epochs=100, validation_data=(X_test_scaled, y_test), verbose=0)

# Avaliar o modelo
test_loss, test_mae = model.evaluate(X_test_scaled, y_test)
print("Mean Squared Error on test set:", test_loss)
print("Mean Absolute Error on test set:", test_mae)

# Salvar o modelo treinado em um arquivo .h5
model.save('modelo_regressao_imoveis.h5')

# Salvar o escalador
joblib.dump(scaler, 'scaler.joblib')

