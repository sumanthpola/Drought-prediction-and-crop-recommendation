from flask import Flask, render_template, request
import warnings
import pandas as pd
warnings.filterwarnings("ignore")
import numpy as np
import pickle
app= Flask(__name__,template_folder='button/template')
app.config["CLIENT_CSV"]="C:/Users/SUMANTH POLA/Desktop/project/FYP-2020-master"
@app.route("/")
def index():
    return render_template('home.html')
@app.route("/crop")
def crop():
    return render_template('dashboard.html')
@app.route("/submit",methods=['POST'])
def getvalue():
    if request.method=='POST':    
        nit=request.form["N"]
        p=request.form["P"]
        k=request.form["K"]
        ph=request.form["pH"]
        rain=request.form["rainfall"]
        nit=int(nit)
        p=int(p)
        k=int(k)
        ph=int(ph)
        rain=int(rain)
        data = [[nit,p,k,20,82,ph,rain]]
        df = pd.DataFrame(data, columns = ['N', 'P','K','temperature','humidity','ph','rainfall'])
        model=pickle.load(open('C:/Users/SUMANTH POLA/Desktop/project/FYP-2020-master/Machine Learning/APIs/NBClassifier.pkl','rb'))
        h=model.predict(data)
        return render_template('new.html',h=h)
if __name__=='__main__':    
    app.run(host='localhost',port=9874,debug=True, use_reloader=False)
