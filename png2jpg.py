# Importamos Image de la librería PIL
from PIL import Image

# formato Image.open(fp,mode = 'r',formato)
imagen = Image.open(r'imagen2.png') # Creamos el objeto que almacena la imagen en "imagen"
# formato Image.save(fp,formato,parametros)
imagen.save('imagen3.jpg') # Con save() asignamos el nombre y formato de la nueva imagen