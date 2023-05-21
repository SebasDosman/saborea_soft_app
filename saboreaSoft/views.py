from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.db.models import F

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.urls import reverse

from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from saboreaSoft.models import Descuento, Credencial, Factura, Producto, Restaurante, Usuario, Venta
import uuid


# Apartado inicio
def inicio(request):
    return render(request, 'pages/inicio/inicio.html')

# Apartado inicio del administrador
def inicioAdmin(request):
    return render(request, 'pages/inicio/inicioAdmin.html')

# Apartado categorias
def categorias(request):
    return render(request, 'pages/categorias/categorias.html')

# Apartado contactanos
def contactanos(request):
    return render(request, 'pages/contactanos/contacto.html')


# Apartado Pedidos    
def procesar_factura(request):
    if request.method == 'POST':
        id_factura = request.POST.get('id_factura')
        nit_restaurante = request.POST.get('nit_restaurante_id')
        fecha_compra = request.POST.get('fecha_compra')
        total_pago = request.POST.get('total_pago')
        restaurante = get_object_or_404(Restaurante, nit=nit_restaurante)

        factura = Factura.objects.create(id_factura=id_factura, nit_restaurante=restaurante, fecha_compra=fecha_compra, total_pago=total_pago)

        for key in request.POST:
            if key.startswith('id_venta_'):
                index = key.split('_')[-1]
              
                id_venta = str(uuid.uuid4()) 
                cantidad = request.POST.get(f'cantidad_{index}')
                id_factura_id = request.POST.get(f'id_factura_id_{index}')
                id_producto_id = request.POST.get(f'id_producto_id_{index}')

                venta = Venta.objects.create(id_venta=id_venta, cantidad=cantidad, id_factura_id=id_factura_id, id_producto_id=id_producto_id)
                Producto.objects.filter(id_producto=id_producto_id).update(cantidad=F('cantidad') - 1)
        
    return render(request, 'pages/pedidos/pedidos.html')
    
# Apartado login
class Login(ListView):
    template_name = 'login.html'
    context_object_name = 'credencial_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario_list'] = Usuario.objects.all()
        return context

    def get_queryset(self):
        return Credencial.objects.all()

# Apartado de Credencial
class CredencialListado(ListView):
    model = Credencial

class CredencialCrear(SuccessMessageMixin, CreateView):
    model = Credencial
    form = Credencial 
    fields = "__all__" 
    success_message = 'Credencial creada correctamente!' 
    def get_success_url(self):
        return reverse('leer_credencial')
    
    
class UsuarioRegistrar(SuccessMessageMixin, CreateView):
    model = Credencial 
    form = Credencial 
    fields = "__all__" 
    success_message = 'Credencial registrado correctamente!' 

    def get_success_url(self):        
        return reverse('leer_usuario')

class CredencialDetalle(DetailView):
    model = Credencial

class CredencialActualizar(SuccessMessageMixin, UpdateView):
    model = Credencial
    form = Credencial 
    fields = "__all__" 
    success_message = 'Credencial actualizada correctamente!' 

    def get_success_url(self):
        return reverse('leer_credencial')

class CredencialEliminar(SuccessMessageMixin, DeleteView):
    model = Credencial
    form = Credencial
    fields = "__all__"     

    def get_success_url(self):
        success_message = 'Credencial eliminada correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer_credencial')


#Apartado de Descuento
class DescuentoListado(ListView):
    model = Descuento

class DescuentoCrear(SuccessMessageMixin, CreateView):
    model = Descuento 
    form = Descuento 
    fields = "__all__" 
    success_message = 'Descuento creado correctamente!' 

    def get_success_url(self):        
        return reverse('leer_descuento')

class DescuentoDetalle(DetailView): 
    model = Descuento

class DescuentoActualizar(SuccessMessageMixin, UpdateView):
    model = Descuento 
    form = Descuento 
    fields = "__all__" 
    success_message = 'Descuento actualizado correctamente!' 

    def get_success_url(self):               
        return reverse('leer_descuento')

class DescuentoEliminar(SuccessMessageMixin, DeleteView):
    model = Descuento 
    form = Descuento
    fields = "__all__"     

    def get_success_url(self): 
        success_message = 'Descuento eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer_descuento')


# Apartado de Restaurante
class RestauranteListado(ListView):
    model = Restaurante

class RestauranteCrear(SuccessMessageMixin, CreateView): 
    model = Restaurante 
    form = Restaurante 
    fields = "__all__" 
    success_message = 'Restaurante creado correctamente!' 

    def get_success_url(self):
        return reverse('leer_restaurante')

class RestauranteDetalle(DetailView): 
    model = Restaurante 

class RestauranteActualizar(SuccessMessageMixin, UpdateView): 
    model = Restaurante 
    form = Restaurante 
    fields = "__all__" 
    success_message = 'Restaurante actualizado correctamente!' 

    def get_success_url(self):               
        return reverse('leer_restaurante') 

class RestauranteEliminar(SuccessMessageMixin, DeleteView): 
    model = Restaurante 
    form = Restaurante
    fields = "__all__"     

    def get_success_url(self): 
        success_message = 'Restaurante eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer_restaurante') 


#Apartado de Factura
class FacturaListado(ListView):
    model = Factura

class FacturaCrear(SuccessMessageMixin, CreateView):
    model = Factura 
    form = Factura 
    fields = "__all__" 
    success_message = 'Factura creada correctamente!' 

    def get_success_url(self):        
        return reverse('leer_factura')

class FacturaDetalle(DetailView): 
    model = Factura

class FacturaActualizar(SuccessMessageMixin, UpdateView):
    model = Factura 
    form = Factura 
    fields = "__all__" 
    success_message = 'Factura actualizada correctamente!' 

    def get_success_url(self):               
        return reverse('leer_factura')

class FacturaEliminar(SuccessMessageMixin, DeleteView):
    model = Factura 
    form = Factura
    fields = "__all__"     

    def get_success_url(self): 
        success_message = 'Factura eliminada correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer_factura')


#Apartado de Producto
class ProductoListado(ListView):
    model = Producto

class ProductoCrear(SuccessMessageMixin, CreateView):
    model = Producto 
    form = Producto 
    fields = "__all__" 
    success_message = 'Producto creado correctamente!' 

    def form_valid(self, form):
        producto = form.save(commit=False)
        descuento_id = self.request.POST.get('id_descuento')
        
        if descuento_id:
            descuento = Descuento.objects.get(pk=descuento_id)
            precio_con_descuento = producto.precio - descuento.descuento
            producto.precio = precio_con_descuento

        producto.save()
        return redirect('leer_producto')

class ProductoDetalle(DetailView): 
    model = Producto

class ProductoActualizar(SuccessMessageMixin, UpdateView):
    model = Producto 
    form = Producto 
    fields = "__all__" 
    success_message = 'Producto actualizado correctamente!' 

    def form_valid(self, form):
        producto = form.save(commit=False)
        descuento_id = self.request.POST.get('id_descuento')
        
        if descuento_id:
            descuento = Descuento.objects.get(pk=descuento_id)
            precio_con_descuento = producto.precio - descuento.descuento
            producto.precio = precio_con_descuento

        producto.save()
        return redirect('leer_producto')

class ProductoEliminar(SuccessMessageMixin, DeleteView): 
    model = Producto 
    form = Producto
    fields = "__all__"     

    def get_success_url(self): 
        success_message = 'Producto eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer_producto') 


# Apartado de Usuario
class UsuarioListado(ListView):
    model = Usuario

class UsuarioCrear(SuccessMessageMixin, CreateView):
    model = Usuario 
    form = Usuario 
    fields = "__all__" 
    success_message = 'Usuario creado correctamente!' 

    def get_success_url(self):        
        return reverse('leer_usuario')
    
# Apartado registro del perfil usuario
class UsuarioPerfil(SuccessMessageMixin, CreateView):
    model = Usuario
    form = Usuario
    fields = "__all__"
    success_message = 'Usuario creado correctamente!!'
    

    def get_success_url(self):
        return reverse('leer_usuario')

class UsuarioDetalle(DetailView): 

    model = Usuario

class UsuarioActualizar(SuccessMessageMixin, UpdateView):
    model = Usuario 
    form = Usuario 
    fields = "__all__" 
    success_message = 'Usuario actualizado correctamente!' 

    def get_success_url(self):               
        return reverse('leer_usuario')

class UsuarioEliminar(SuccessMessageMixin, DeleteView): 
    model = Usuario 
    form = Usuario
    fields = "__all__"     

    def get_success_url(self): 
        success_message = 'Usuario eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer_usuario') 


#Apartado de Venta
class VentaListado(ListView):
    model = Venta

class VentaCrear(SuccessMessageMixin, CreateView):
    model = Venta 
    form = Venta 
    fields = "__all__" 
    success_message = 'Venta creado correctamente!' 

    def get_success_url(self):        
        return reverse('leer_venta') 

class VentaDetalle(DetailView): 
    model = Venta

class VentaActualizar(SuccessMessageMixin, UpdateView):
    model = Venta 
    form = Venta 
    fields = "__all__" 
    success_message = 'Venta actualizado correctamente!' 

    def get_success_url(self):               
        return reverse('leer_venta')  

class VentaEliminar(SuccessMessageMixin, DeleteView):
    model = Venta 
    form = Venta
    fields = "__all__"     

    def get_success_url(self): 
        success_message = 'Venta eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer_venta') 


# Apartado del Menu
class Menu(ListView):
    model = Producto
    template_name = 'menu.html'
    context_object_name = 'productos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorias = ['Hamburguesas', 'Perros', 'Salchipapas', 'Bebidas', 'Fritanga']
        productos_por_categoria = [[] for _ in range(len(categorias))]

        # Agregar los productos correspondientes a cada categoría en la lista
        for producto in Producto.objects.all():
            categoria_index = categorias.index(producto.categoria) if producto.categoria in categorias else -1
            if categoria_index >= 0:
                productos_por_categoria[categoria_index].append(producto)

        # Agregar las listas al contexto
        context['hamburguesas'] = productos_por_categoria[0]
        context['perros'] = productos_por_categoria[1]
        context['salchipapas'] = productos_por_categoria[2]
        context['bebidas'] = productos_por_categoria[3]
        context['fritangas'] = productos_por_categoria[4]

        return context


# Apartado categoria salchipapa
class SalchipapasListView(ListView):
    model = Producto
    template_name = 'salchipapa.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.filter(categoria='Salchipapas')

# Apartado categoria hamburguesa
class HamburguesasListView(ListView):
    model = Producto
    template_name = 'hamburguesas.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.filter(categoria='Hamburguesas')

# Apartado categoria perros
class PerrosListView(ListView):
    model = Producto
    template_name = 'perro.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.filter(categoria='Perros')

# Apartado categoria fritanga
class FritangaListView(ListView):
    model = Producto
    template_name = 'fritanga.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.filter(categoria='Fritanga')

# Apartado categoria bebidas
class BebidasListView(ListView):
    model = Producto
    template_name = 'bebidas.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.filter(categoria='Bebidas')
    
