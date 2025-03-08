from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Carrega o modelo treinado
model = joblib.load("regressao_modelo.joblib")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Obtém os dados do formulário
        data = [
            float(request.form["fish_weight"]),
            float(request.form["temperature"]),
            float(request.form["oxygen"]),
            float(request.form["ph"]),
            float(request.form["turbidity"]),
            int(request.form["oxygen_intervention"]),
            int(request.form["corrective_intervention"]),
            int(request.form["oxygen_automatic"]),
            int(request.form["corrective_measures"]),
            int(request.form["thermal_risk"]),
            int(request.form["health_status"])
        ]
        
        # Faz a previsão
        prediction = model.predict([data])[0]
        
        # Converte 0 e 1 para "Sim" ou "Não"
        resultado_texto = "Morreria" if prediction == 1 else "Sobreviveria"

        return render_template("result.html", resultado_texto=resultado_texto)
    except Exception as e:
        return render_template("error.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
