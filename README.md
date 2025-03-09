# Predição de Mortalidade de Peixes com Flask e Modelos de Machine Learning

Este é um projeto Flask que utiliza modelos de Machine Learning para prever a mortalidade de peixes com base em dados ambientais e intervenções.

## 🚀 Funcionalidades
- Interface web para entrada de dados.
- Predição utilizando quatro modelos de machine learning:
  - Regressão Logística (Logistic Regression)
  - Árvore de Decisão (Decision Tree)
  - Floresta Aleatória (Random Forest)
  - Support Vector Machine (SVM)
- Retorno da previsão com indicação de "Morreria" ou "Sobreviveria".

## 📂 Estrutura do Projeto
```
app/
│-- app.py
│-- templates/
│   │-- index.html
│   │-- result.html
│   │-- error.html
│-- static/
│   │-- style.css
│-- model/
│   │-- logistic_regression_modelo.joblib
│   │-- decision_tree_modelo.joblib
│   │-- random_florest_modelo.joblib
│   │-- support_vector_modelo.joblib
requirements.txt
.gitignore
LICENSE
README.md
```

## 🛠️ Instalação e Configuração
1. Clone o repositório:
   ```bash
   git clone https://github.com/IohanaViterbino/ml_tilapia.git
   cd ml_tilapia
   ```
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```bash
   python app.py
   ```
5. Acesse no navegador:
   ```
   http://127.0.0.1:5000/
   ```

## 📊 Como Usar
1. Preencha os campos do formulário na interface web.
2. Escolha um modelo de predição.
3. Clique em **Prever**.
4. O sistema exibirá se o peixe "Morreria" ou "Sobreviveria".

## 📌 Dependências Principais
- Flask
- Joblib
- NumPy

## Notebook de estudo para essa API
[Google Colab](https://colab.research.google.com/drive/1ZUGA9_ZRCF4U2s1W3ySUzO5YI8uesIpL?usp=sharing)

## 📝 Licença
Este projeto é distribuído sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
