from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contactos', methods=['GET', 'POST'])
def contactos():
    if request.method == 'POST':
        nombre = request.form.get('name') 
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')

        print(f"Nombre: {nombre}, Email: {email}, Mensaje: {mensaje}")

        return render_template('salida.html', nombre=nombre, email=email, mensaje=mensaje)
    
    return render_template('contactos.html')

if __name__ == '__main__':
    app.run(debug=True)
