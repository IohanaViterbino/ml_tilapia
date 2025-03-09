from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

def load_models():
    """Carrega os modelos treinados dinamicamente."""
    model_dir = os.path.join(os.path.dirname(__file__), "model")
    models = {
        "lr": "logistic_regression_modelo.joblib",
        "dt": "decision_tree_modelo.joblib",
        "rf": "random_florest_modelo.joblib",
        "sv": "support_vector_modelo.joblib"
    }
    
    return {key: joblib.load(os.path.join(model_dir, filename)) for key, filename in models.items()}

# Carregar todos os modelos na inicialização
models = load_models()

@app.route("/")
def index():
    """Renderiza a página inicial."""
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Mapeia os campos do formulário para conversões adequadas
        campos_float = ["average_fish_weight", "temperature", "dissolved_oxygen", "ph", "turbidity"]
        campos_int = ["oxygenation_interventions", "corrective_interventions", "oxygenation_automatic",
              "corrective_measures", "thermal_risk_index", "health_status"]

        # Obtém os dados do formulário
        data = [float(request.form[campo]) for campo in campos_float] + \
               [int(request.form[campo]) for campo in campos_int]
        
        # Obtém o modelo escolhido (padrão: Decision Tree)
        model_key = request.form.get("model_predict", "dt")
        prediction = get_model_prediction(model_key, data)

        # Converte 0 e 1 para "Morreria" ou "Sobreviveria"
        resultado_texto = "Morreria" if prediction == 1 else "Sobreviveria"

        return render_template("result.html", resultado_texto=resultado_texto)

    except Exception as e:
        return render_template("error.html", error=str(e))

def get_model_prediction(model_key, data):
    """Obtém a predição do modelo escolhido, usando Decision Tree como fallback."""
    model = models.get(model_key, models["dt"])
    return model.predict([data])[0]

if __name__ == "__main__":
    app.run(debug=True)
