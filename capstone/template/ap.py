from flask import Flask, render_template, request
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pickle
app= Flask(__name__,template_folder='template')
@app.route("/",methods=['GET','POST'])
def getvalue():
    if request.method=='POST':    
        nit=request.form["N"]
        p=request.form["P"]
        k=request.form["K"]
        ph=request.form["pH"]
        rain=request.form["rainfall"]
        return render_template('new.html',nit=nit,p=p,k=k,ph=ph,rain=rain)
        print(p)
    else:
        return render_template('dashboard.html')
if __name__=='__main__':    
    app.run(debug=True, use_reloader=False)
