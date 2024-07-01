from django.urls import path, include
from rest_framework import routers
from api import views


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Your REST API Documentation",
        default_version="v1",
        description="Documentation for your REST API using Swagger",
        terms_of_service="https://github.com/Capijos/ticket-sales-backend/tree/main",
        contact=openapi.Contact(email="jose.tito.acrota@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"products", views.ProductViewSet)
router.register(r"product-types", views.ProductTypeViewSet)
router.register(r"carts", views.CartViewSet)
router.register(r"cart-items", views.CartItemViewSet)
router.register(r"sales", views.SaleViewSet)
router.register(r"orders", views.OrderViewSet)
router.register(r"order-items", views.OrderItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "api-docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
