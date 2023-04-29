# SaboreaSoft-App

La aplicación "Saboreasoft - App" es un sistema de gestión para restaurantes que busca automatizar y mejorar los procesos de administración de un negocio gastronómico. Con esta herramienta, los administradores podrán gestionar de manera centralizada la información de los clientes, productos, ventas y descuentos, además de generar facturas precisas y detalladas.

# Características y funcionalidades
* Registro y gestión de información de los clientes.
* Gestión centralizada de información de productos y descuentos.
* Registro y gestión de ventas por parte de los clientes.
* Generación de facturas precisas y detalladas.
* Interfaces gráficas amigables, vistosas y de fácil manejo para el usuario.

# Requerimientos y tecnologías utilizadas
La aplicación fue desarrollada en el framework Django, utilizando lenguaje de programación Python y base de datos PostgreSQL. Para ejecutar la aplicación es necesario contar con una versión de Python 3.6 o superior, y tener instalado el administrador de paquetes pip.

# Instalación y configuración
Para instalar la aplicación, siga los siguientes pasos:

1. Descargue o clone el repositorio desde GitHub.
2. Cree y active un entorno virtual para la aplicación.
3. Instale las dependencias del proyecto con el comando pip install -r requirements.txt.
4. Configure la base de datos PostgreSQL en el archivo settings.py.
5. Ejecute las migraciones con el comando python manage.py migrate.
6. Cargue los datos iniciales en la base de datos con el comando python manage.py loaddata data.json.
7. Inicie el servidor de desarrollo con el comando python manage.py runserver.
Una vez que el servidor esté en ejecución, acceda a la aplicación desde su navegador web en la dirección http://localhost:8000/.

# Contribuir
Si deseas contribuir con el desarrollo de la aplicación, puedes realizar un fork del repositorio y enviar tus contribuciones mediante un pull request. También puedes reportar errores o sugerir mejoras mediante la creación de un issue en GitHub.

# Licencia
La aplicación "Saboreasoft - App" está licenciada bajo la licencia MIT. Consulte el archivo LICENSE para obtener más detalles.