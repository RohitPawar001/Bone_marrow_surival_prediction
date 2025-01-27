from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from Bone_marrow_survival_prediction.pipeline.prediction import PredictionPipeline


app = Flask(__name__)
@app.route("/",methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/train",methods=["GET"])
def training():
    os.system("python main.py")
    return "training successfull"

@app.route("/prediction", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            survival_time = int(request.form["survival_time"])
            PLTrecovery = int(request.form["PLTrecovery"])
            Donorage = float(request.form["Donorage"])
            Relapse = int(request.form["Relapse"])
            HLAmismatch = int(request.form["HLAmismatch"])
            

            data = [survival_time,PLTrecovery,Donorage,Relapse,HLAmismatch]
            data = np.array(data).reshape(1, 5)

            obj = PredictionPipeline()
            predict = obj.predict(data)
            if predict == 0:
                predict = "Sorry your chid could not be able survived form surgery."
            elif predict == 1:
                predict = "Their are high chances that your child could survive from this surgery"

            return render_template("results.html", predictions=str(predict))

        except Exception as e:
            print(f"Error: {e}")
            return "An error occurred during prediction."

                    
    


if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=8080)
