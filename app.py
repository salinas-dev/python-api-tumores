from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Lista de nombres de imágenes en la carpeta 'img'
    image_names = ["imagen_1.jpg", "imagen_2.jpg", "imagen_3.jpg", "imagen_4.jpg", "imagen_5.jpg"]

    # Ruta a la carpeta de imágenes (img)
    image_folder = "img"

    # Renderizar la plantilla HTML con los datos
    return render_template('index.html', title="API de Tumores", image_names=image_names, image_folder=image_folder)

if __name__ == '__main__':
    app.run(debug=True)
