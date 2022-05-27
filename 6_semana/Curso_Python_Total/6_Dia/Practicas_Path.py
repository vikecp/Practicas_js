from pathlib import Path

# ruta relativa
guia = Path("Barcelona", "Sagrada_familia.txt")

#otra ruta relativa
from pathlib import Path
ruta = Path("Curso Python","Día 6","practicas_path.py")

#ruta absluta
from pathlib import Path
base = Path.home()
ruta = Path(base,"Curso Python","Día 6","practicas_path.py")

# ruta absolutaa
base = Path.home()
ruta_absoluta = Path(base,"Barcelona", "Sagrada_familia.txt")
print(ruta_absoluta)


base = Path.home()
ruta_absoluta = Path(base,"Europa", "España", Path("Barcelona", "Sagrada_familia.txt"))
#cambiar el nombre del archivo
ruta2 = ruta_absoluta.with_name("La_pedrera.txt")
print(ruta_absoluta)
print(ruta2)

#enumerar archivos
guia = Path(Path.home(),"Europa")

for txt in Path(guia).glob("**/*.txt"):
    print(txt)



