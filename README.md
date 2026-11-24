# Sistema académico — guía 4 POO
Proyecto local de Django con SQLite. Python 3.11 o superior.

## Windows (CMD)
1. `py -3.11 -m venv venv`
2. `venv\Scripts\activate`
3. `pip install -r requirements.txt`
4. `python manage.py makemigrations academico`
5. `python manage.py migrate`
6. `python manage.py check`
7. `python manage.py test`
8. `python manage.py runserver`
9. Abrir http://127.0.0.1:8000/

La base db.sqlite3 se genera al migrar. Registrar primero docentes y estudiantes, después asignaturas, matrículas y calificaciones. Bootstrap se carga por CDN (requiere internet). Escala de notas propuesta: 0–100; una nota final por matrícula. El proyecto es para uso local, sin autenticación en las vistas públicas; no desplegar así en producción.

## IA y validación
Se utilizó ChatGPT para generar y revisar el código. Se incluyen pruebas automatizadas de rutas, nota fuera de rango, matrícula duplicada, registro de nota y eliminación protegida. Ejecutarlas y documentar resultados reales; no se ejecutaron en el entorno de generación porque Django no estaba instalado y no hubo conexión para instalarlo.
