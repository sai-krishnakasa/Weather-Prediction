from flask import Flask,render_template,request
import pickle
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method=="POST":
        with open('model.pkl', 'rb') as f:
            data = pickle.load(f) 
        max_temp=int(request.form.get('maxtempC',None))
        min_temp=int(request.form.get('mintempC',None))
        cloud_cover=int(request.form.get('cloudcover',None))
        humidity=int(request.form.get('humidity',None))
        sun_hour=float(request.form.get('sunHour',None))
        # max_temp=request.form.get('maxtempC',None)
        heat_index=int(request.form.get('HeatIndexC',None))
        pressure=int(request.form.get('pressure',None))
        precipitation=float(request.form.get('precipMM ',None))
        wind_speed=int(request.form.get('windspeedKmph',None))
        print([max_temp,min_temp,cloud_cover,humidity,sun_hour,heat_index,precipitation,pressure,wind_speed])
        out=data.predict([[max_temp,min_temp,cloud_cover,humidity,sun_hour,heat_index,precipitation,pressure,wind_speed]])
        out=round(out[0],2)
        return render_template('index.html',output=out)
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)

