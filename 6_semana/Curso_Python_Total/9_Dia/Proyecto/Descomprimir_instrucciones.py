import shutil
from pathlib import Path
ruta = Path('/Users/virginia/Documents/Practicas_Prof/6_semana/Curso_Python/9_Dia/Proyecto/zip') / 'proyecto9.zip'

shutil.unpack_archive(ruta, "Descomprimir", 'zip')