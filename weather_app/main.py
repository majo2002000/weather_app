from flask import Flask, render_template, request
import requests
app= Flask(__name__)
def get_weather_data(city):
   APY_KEY ='f0726faa5b2e77a10e23a061f2ec3b8e'
   url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=es&appid={APY_KEY}'
   r = requests.get(url).json()
   return r

@app.route("/", methods=['POST', 'GET'])
def hello():
  if request.method == 'POST':
      ciudad=str(request.form.get('txtciudad'))
      data=get_weather_data(ciudad)
      return render_template('index.html', context = data)
  else: 
     return render_template('index.html')

@app.route("/cv")
def curriculum():
    return render_template('hv.html')
 


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method== 'POST':
      USUARIO='ADMIN@GMAIL.COM'
      PASSWORD='ADMIN'
      user= request.form.get("txtEmail")
      password=request.form.get("txtPassword")
      if USUARIO == user and PASSWORD == password:
        return render_template('index.html')
      else:
        return render_template('login.html', error1 = True)
    return render_template('login.html')

@app.route("/registro", methods=['POST', 'GET'])
def registro():
   return render_template('registro.html')


@app.errorhandler(404)
def not_found(error):
   return render_template('error.html'), 404

if __name__=='__main__':
    app.run(debug = True)

