from django.contrib import admin
from django.urls import path


from saboreaSoft.views import (BebidasListView, CredencialActualizar,
                               CredencialCrear, CredencialDetalle,
                               CredencialEliminar, CredencialListado,
                               DescuentoActualizar, DescuentoCrear,
                               DescuentoDetalle, DescuentoEliminar,
                               DescuentoListado, FacturaActualizar,
                               FacturaCrear, FacturaDetalle, FacturaEliminar,
                               FacturaListado, FritangaListView,
                               HamburguesasListView, Login, Menu,
                               PerrosListView, ProductoActualizar,
                               ProductoCrear, ProductoDetalle,
                               ProductoEliminar, ProductoListado,
                               RestauranteActualizar, RestauranteCrear,
                               RestauranteDetalle, RestauranteEliminar,
                               RestauranteListado, SalchipapasListView,
                               UsuarioActualizar, UsuarioCrear, UsuarioDetalle,
                               UsuarioEliminar, UsuarioListado, UsuarioPerfil,
                               UsuarioRegistrar, VentaActualizar, VentaCrear,
                               VentaDetalle, VentaEliminar, VentaListado,
                                categorias, contactanos, inicio, inicioAdmin,
                               procesar_factura)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', inicio, name = 'inicio'),
    path('administrador/', inicioAdmin, name = "inicioAdmin"),
    path('categorias/', categorias, name = "categorias"),
    path('contactanos/', contactanos, name = "contactanos"),

    path('login/', Login.as_view(template_name = "pages/login/login.html"), name = "login"),
    path('menu/', Menu.as_view(template_name = "pages/categorias/menu.html"), name = 'leer_menu'),
    path('pedidos/', procesar_factura, name = "pedidos"),
    
    
    path('categorias/salchipapas', SalchipapasListView.as_view(template_name = "pages/categorias/salchipapa.html"), name = 'leer_producto_salchipapas'),
    path('categorias/hamburguesas', HamburguesasListView.as_view(template_name = "pages/categorias/hamburguesa.html"), name = 'leer_producto_hamburguesas'),
    path('categorias/perros', PerrosListView.as_view(template_name = "pages/categorias/perro.html"), name = 'leer_producto_perros'),
    path('categorias/fritangas', FritangaListView.as_view(template_name = "pages/categorias/fritanga.html"), name = 'leer_producto_fritangas'),
    path('categorias/bebidas', BebidasListView.as_view(template_name = "pages/categorias/bebidas.html"), name = 'leer_producto_bebidas'),
    
    path('credencial/'                  , CredencialListado.as_view(template_name = "models/credencial/index.html"), name = 'leer_credencial'),
    path('credencial/detalle/<str:pk>'  , CredencialDetalle.as_view(template_name = "models/credencial/detalles.html"), name = 'detalles_credencial'),
    path('credencial/crear'             , CredencialCrear.as_view(template_name = "models/credencial/crear.html"), name = 'crear_credencial'),
    path('credencial/editar/<str:pk>'   , CredencialActualizar.as_view(template_name = "models/credencial/actualizar.html"), name = 'actualizar_credencial'),
    path('credencial/eliminar/<str:pk>' , CredencialEliminar.as_view(), name = 'eliminar_credencial'),
    path('login/registrar'              , UsuarioRegistrar.as_view(template_name = "models/credencial/registrarse.html"), name = 'registrar_usuario'),
    
    path('descuento/'                   , DescuentoListado.as_view(template_name = "models/descuento/index.html"), name = 'leer_descuento'),
    path('descuento/detalle/<int:pk>'   , DescuentoDetalle.as_view(template_name = "models/descuento/detalles.html"), name = 'detalles_descuento'),
    path('descuento/crear'              , DescuentoCrear.as_view(template_name = "models/descuento/crear.html"), name = 'crear_descuento'),
    path('descuento/editar/<int:pk>'    , DescuentoActualizar.as_view(template_name = "models/descuento/actualizar.html"), name = 'actualizar_descuento'), 
    path('descuento/eliminar/<int:pk>'  , DescuentoEliminar.as_view(), name = 'eliminar_descuento'), 
    
    path('factura/', FacturaListado.as_view(template_name = "models/factura/index.html"), name = 'leer_factura'),
    path('factura/detalle/<int:pk>', FacturaDetalle.as_view(template_name = "models/factura/detalles.html"), name = 'detalles_factura'),
    path('factura/crear', FacturaCrear.as_view(template_name = "models/factura/crear.html"), name = 'crear_factura'),
    path('factura/editar/<int:pk>', FacturaActualizar.as_view(template_name = "models/factura/actualizar.html"), name = 'actualizar_factura'), 
    path('factura/eliminar/<int:pk>', FacturaEliminar.as_view(), name = 'eliminar_factura'), 
    
    path('producto/', ProductoListado.as_view(template_name = "models/producto/index.html"), name = 'leer_producto'),
    path('producto/detalle/<int:pk>', ProductoDetalle.as_view(template_name = "models/producto/detalles.html"), name = 'detalles_producto'),
    path('producto/crear', ProductoCrear.as_view(template_name = "models/producto/crear.html"), name = 'crear_producto'),
    path('producto/editar/<int:pk>', ProductoActualizar.as_view(template_name = "models/producto/actualizar.html"), name = 'actualizar_producto'), 
    path('producto/eliminar/<int:pk>', ProductoEliminar.as_view(), name = 'eliminar_producto'), 
    
    path('restaurante/', RestauranteListado.as_view(template_name = "models/restaurante/index.html"), name = 'leer_restaurante'),
    path('restaurante/detalle/<int:pk>', RestauranteDetalle.as_view(template_name = "models/restaurante/detalles.html"), name = 'detalles_restaurante'),
    path('restaurante/crear', RestauranteCrear.as_view(template_name = "models/restaurante/crear.html"), name = 'crear_restaurante'),
    path('restaurante/editar/<int:pk>', RestauranteActualizar.as_view(template_name = "models/restaurante/actualizar.html"), name = 'actualizar_restaurante'), 
    path('restaurante/eliminar/<int:pk>', RestauranteEliminar.as_view(), name = 'eliminar_restaurante'), 
    
    path('usuario/', UsuarioListado.as_view(template_name = "models/usuario/index.html"), name = 'leer_usuario'),
    path('usuario/detalle/<int:pk>', UsuarioDetalle.as_view(template_name = "models/usuario/detalles.html"), name = 'detalles_usuario'),
    path('usuario/crear', UsuarioCrear.as_view(template_name = "models/usuario/crear.html"), name = 'crear_usuario'),
    path('usuario/editar/<int:pk>', UsuarioActualizar.as_view(template_name = "models/usuario/actualizar.html"), name = 'actualizar_usuario'), 

    path('usuario/eliminar/<int:pk>', UsuarioEliminar.as_view(), name = 'eliminar_usuario'), 
    path('perfil/', UsuarioPerfil.as_view(template_name = "models/usuario/perfil.html"), name = 'perfil_usuario'),
    
    path('venta/', VentaListado.as_view(template_name = "models/venta/index.html"), name = 'leer_venta'),
    path('venta/detalle/<int:pk>', VentaDetalle.as_view(template_name = "models/venta/detalles.html"), name = 'detalles_venta'),
    path('venta/crear', VentaCrear.as_view(template_name = "models/venta/crear.html"), name = 'crear_venta'),
    path('venta/editar/<int:pk>', VentaActualizar.as_view(template_name = "models/venta/actualizar.html"), name = 'actualizar_venta'),
    path('venta/eliminar/<str:pk>', VentaEliminar.as_view(), name = 'eliminar_venta')
]
