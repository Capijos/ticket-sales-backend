from django.test import TestCase
from django.utils import timezone
from .models import ProductType, Cart, CartItem, Sale, Order, OrderItem, User, Product

class ProductTypeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='user@example.com',
            first_name='John',
            last_name='Doe',
            document_id='123456789',
            age=30
        )
        self.product = Product.objects.create(
            name='Test Product',
            description='This is a test product',
            images=['image1.jpg', 'image2.jpg'],
            expiration_date=timezone.now() + timezone.timedelta(days=30)
        )
        self.product_type = ProductType.objects.create(
            product=self.product,
            type_name='Type A',
            price=10.99,
            stock=100
        )

    def test_product_type_creation(self):
        self.assertEqual(self.product_type.product, self.product)
        self.assertEqual(self.product_type.type_name, 'Type A')
        self.assertEqual(self.product_type.price, 10.99)
        self.assertEqual(self.product_type.stock, 100)
        self.assertTrue(self.product_type.type_id)

class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='user@example.com',
            first_name='John',
            last_name='Doe',
            document_id='123456789',
            age=30
        )
        self.cart = Cart.objects.create(
            user=self.user
        )

    def test_cart_creation(self):
        self.assertEqual(self.cart.user, self.user)
        self.assertTrue(self.cart.created_at)

class CartItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='user@example.com',
            first_name='John',
            last_name='Doe',
            document_id='123456789',
            age=30
        )
        self.product = Product.objects.create(
            name='Test Product',
            description='This is a test product',
            images=['image1.jpg', 'image2.jpg'],
            expiration_date=timezone.now() + timezone.timedelta(days=30)
        )
        self.cart = Cart.objects.create(
            user=self.user
        )
        self.product_type = ProductType.objects.create(
            product=self.product,
            type_name='Type A',
            price=10.99,
            stock=100
        )
        self.cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            type=self.product_type,
            quantity=2
        )

    def test_cart_item_creation(self):
        self.assertEqual(self.cart_item.cart, self.cart)
        self.assertEqual(self.cart_item.product, self.product)
        self.assertEqual(self.cart_item.type, self.product_type)
        self.assertEqual(self.cart_item.quantity, 2)

class SaleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='user@example.com',
            first_name='John',
            last_name='Doe',
            document_id='123456789',
            age=30
        )
        self.product = Product.objects.create(
            name='Test Product',
            description='This is a test product',
            images=['image1.jpg', 'image2.jpg'],
            expiration_date=timezone.now() + timezone.timedelta(days=30)
        )
        self.product_type = ProductType.objects.create(
            product=self.product,
            type_name='Type A',
            price=10.99,
            stock=100
        )
        self.sale = Sale.objects.create(
            user=self.user,
            product=self.product,
            type=self.product_type,
            quantity=1,
            total_price=10.99
        )

    def test_sale_creation(self):
        self.assertEqual(self.sale.user, self.user)
        self.assertEqual(self.sale.product, self.product)
        self.assertEqual(self.sale.type, self.product_type)
        self.assertEqual(self.sale.quantity, 1)
        self.assertEqual(self.sale.total_price, 10.99)
        self.assertTrue(self.sale.sale_date)

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='user@example.com',
            first_name='John',
            last_name='Doe',
            document_id='123456789',
            age=30
        )
        self.order = Order.objects.create(
            user=self.user,
            total_price=50.00
        )

    def test_order_creation(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.total_price, 50.00)
        self.assertTrue(self.order.order_date)

class OrderItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='user@example.com',
            first_name='John',
            last_name='Doe',
            document_id='123456789',
            age=30
        )
        self.product = Product.objects.create(
            name='Test Product',
            description='This is a test product',
            images=['image1.jpg', 'image2.jpg'],
            expiration_date=timezone.now() + timezone.timedelta(days=30)
        )
        self.product_type = ProductType.objects.create(
            product=self.product,
            type_name='Type A',
            price=10.99,
            stock=100
        )
        self.order = Order.objects.create(
            user=self.user,
            total_price=50.00
        )
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            type=self.product_type,
            quantity=3,
            price=10.99
        )

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.product, self.product)
        self.assertEqual(self.order_item.type, self.product_type)
        self.assertEqual(self.order_item.quantity, 3)
        self.assertEqual(self.order_item.price, 10.99)
