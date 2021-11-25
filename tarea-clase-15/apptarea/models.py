from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        db_table="marca"
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    class Meta:
        db_table="categoria"
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    precio = models.FloatField(default=0)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img')
    class Meta:
        db_table="productos"
    def __str__(self):
        return self.nombre

class Pago(models.Model):
    TARJETAS = ( #Choices
        ('marcado pago','mercado pago'),
        ('aula','aula'),
        ('efectivo','efectivo')
    )
    tarjetas = models.CharField(max_length=12, choices=TARJETAS)
    class Meta:
        db_table="pago"
    def __str__(self):
        return self.tarjetas

class TipoEnvio(models.Model):
    TIPOENVIO = ( #Choices
        ('envio domicilio','envio domicilio'),
        ('retiro al local','retiro al local')
    )
    tipoenvio = models.CharField(max_length=15, choices=TIPOENVIO)
    class Meta:
        db_table="tipo_envio"
    def __str__(self):
        return self.tipoenvio

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    contaseña = models.CharField(max_length=100)
    email = models.EmailField(default=0)
    celular = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    class Meta:
        db_table="usuarios"
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    total = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipoenvio = models.ForeignKey(TipoEnvio, on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=0)
    class Meta:
        db_table="pedidos"
    def __str__(self):
        return self.total

class UsuarioPedido(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    padido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    class Meta:
        db_table="usuario_pedido"
    
class ProductoPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    class Meta:
        db_table="producto_pedido"
