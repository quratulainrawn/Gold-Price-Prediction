import tkinter as ttk
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
model=pd.read_pickle('GoldPricePredictor.pickle')

app=ttk.Tk()
app.geometry('300x380')
app.title('Gold Price Predictor')

SPX=ttk.Variable(app)
ttk.Label(app,text="SPX Value",padx=15,pady=15).grid(row=0,column=0)
ttk.Entry(app,textvariable=SPX,width=10).grid(row=0,column=1)

USO=ttk.Variable(app)
ttk.Label(app,text="US Oil Price",padx=15,pady=15).grid(row=1,column=0)
ttk.Entry(app,textvariable=USO,width=10).grid(row=1,column=1)

SLV=ttk.Variable(app)
ttk.Label(app,text="Silver Price",padx=15,pady=15).grid(row=2,column=0)
ttk.Entry(app,textvariable=SLV,width=10).grid(row=2,column=1)

EUR_to_USD_ratio=ttk.Variable(app)
ttk.Label(app,text="EUR to USD ratio",padx=15,pady=15).grid(row=3,column=0)
ttk.Entry(app,textvariable=EUR_to_USD_ratio,width=10).grid(row=3,column=1)

def prediction():
    global model
    query_data={
        'SPX':[eval(SPX.get())],
        'USO':[eval(USO.get())],
        'SLV':[eval(SLV.get())],
        'EUR/USD':[eval(EUR_to_USD_ratio.get())]
    }
    price=model.predict(pd.DataFrame(query_data))
    result.set(round(price[0],2))

ttk.Button(app,text='Predict',command=prediction,font=('Arial',20)).grid(row=4,column=0,columnspan=2)

result=ttk.Variable(app)
result.set('0')
ttk.Label(app,textvariable=result,pady=15,font=('Arial',20)).grid(row=5,column=0,columnspan=2)









app.mainloop()