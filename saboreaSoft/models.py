from django.db import models


class Credencial(models.Model):
    correo = models.EmailField(max_length = 50, unique = True, primary_key = True)
    usuario_credencial = models.CharField(max_length = 30, unique = True, null = False)
    contrasenia_credencial = models.CharField(max_length = 30, null = False)
    
    def __str__(self):
        return self.correo
    
    class Meta:
        db_table = "credencial"


class Descuento(models.Model):
    id_descuento    = models.CharField(max_length = 10, unique = True, primary_key = True)
    descuento       = models.DecimalField(max_digits = 8, decimal_places = 2, null = False, blank = False, default = 0)
    fecha_inicio    = models.DateField(null = False)
    fecha_final     = models.DateField(null = False)
    
    def __str__(self):
        return self.id_descuento
    
    class Meta:
        db_table = "descuento"


class Restaurante(models.Model):
    nit = models.CharField(max_length = 10, unique = True, primary_key = True)
    direccion = models.CharField(max_length = 15, null = False)
    telefono = models.CharField(max_length = 10, null = False)
    
    def __str__(self):
        return self.nit
    
    class Meta:
        db_table = "restaurante"

class Factura(models.Model):
    id_factura = models.CharField(max_length = 50, unique = True, primary_key = True)
    nit_restaurante = models.ForeignKey(Restaurante, on_delete = models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    total_pago = models.DecimalField(max_digits = 8, decimal_places=2, null = False, blank = False)
    
    def __str__(self):
        return f"{ self.id_factura } - { self.nit_restaurante.nit }"

    class Meta:
        db_table = "factura"  


class Producto(models.Model):
    id_producto = models.CharField(max_length = 10, unique = True, primary_key = True)
    nombre_prod = models.CharField(max_length = 30, null = False)
    descripcion = models.CharField(max_length = 100, null = False)
    imagen = models.ImageField(upload_to = 'static/uploads')
    categoria = models.CharField(max_length = 30, null = False)
    cantidad = models.IntegerField(null = False)
    precio = models.DecimalField(max_digits = 8, decimal_places = 2, null = False, blank = False)
    id_descuento = models.ForeignKey( Descuento, on_delete = models.CASCADE )
    
    def __str__(self):
        return f"{ self.id_producto } - { self.id_descuento.id_descuento }"
    
    class Meta:
        db_table = "producto"  


class Usuario(models.Model):

    num_identificacion = models.CharField   (max_length = 10, unique = True, primary_key = True)
    tipo_documento = models.CharField       (max_length = 15, null = False)
    nombre = models.CharField               (max_length = 30, null = False)
    apellido = models.CharField             (max_length = 30, null = False)
    rol = models.CharField                  (max_length = 30 , null = True)
    direccion = models.CharField             (max_length = 30, null = False)
    telefono = models.CharField             (max_length = 10, unique = True, null = False)
    fecha_nacimiento = models.DateField     (null = False)
    correo = models.ForeignKey              (Credencial, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{ self.num_identificacion } - { self.correo.correo }"
    
    class Meta:
        db_table = "usuario"


class Venta(models.Model):
    id_venta    = models.CharField(max_length = 50, unique = True, primary_key = True)
    cantidad    = models.IntegerField(null = False)
    id_factura  = models.ForeignKey(Factura, on_delete = models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
        
    def __str__(self):
        return f"{ self.id_venta } - { self.id_factura.id_factura } - { self.id_producto.id_producto }"
    
    class Meta: 
        db_table = "venta"