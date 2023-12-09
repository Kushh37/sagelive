from django.test import TestCase
from .models import Category, Vendor,Product,CartOrder,CartOrderProducts,Address, User
from datetime import datetime

class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(title="Dairy", image="thumbnail-3.jpg")

    def test_cid_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('cid').verbose_name
        self.assertEqual(field_label, 'cid')

    def test_title_content(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.title, "Dairy")

    def test_image_content(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.image, "thumbnail-3.jpg")

    def test_category_image(self):
        category = Category.objects.get(id=1)
        self.assertIn('thumbnail-3.jpg', category.category_image())

class VendorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='adminheet@gmail.com', password='Heet$6537')
        Vendor.objects.create(title="Metro Inc", user=user, image="thumbnail-3.jpg")

    def test_vid_label(self):
        vendor = Vendor.objects.get(title="Metro Inc")
        field_label = vendor._meta.get_field('vid').verbose_name
        self.assertEqual(field_label, 'vid')

    def test_title_content(self):
        vendor = Vendor.objects.get(title="Metro Inc")
        self.assertEqual(vendor.title, "Metro Inc")

    def test_vendor_image(self):
        vendor = Vendor.objects.get(title="Metro Inc")
        self.assertIn('thumbnail-3.jpg', vendor.vendor_image())

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(title="Dairy")
        user = User.objects.create(username='adminheet@gmail.com', password='Heet$6537')
        vendor = Vendor.objects.create(title="Metro Inc", user=user)
        Product.objects.create(title="Milk", category=category, vendor=vendor, user=user)

    def test_pid_label(self):
        product = Product.objects.get(title="Milk")
        field_label = product._meta.get_field('pid').verbose_name
        self.assertEqual(field_label, 'pid')


class CartOrderModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='adminheet@gmail.com', password='Heet$6537')
        CartOrder.objects.create(
            user=user, 
            price="10.99", 
            paid_status=True, 
            product_status="processing"
        )

    def test_user_relation(self):
        cart_order = CartOrder.objects.get(id=1)
        self.assertEqual(cart_order.user.username, 'adminheet@gmail.com')

    def test_paid_status_field(self):
        cart_order = CartOrder.objects.get(id=1)
        self.assertTrue(cart_order.paid_status)

    def test_order_date_field(self):
        cart_order = CartOrder.objects.get(id=1)
        self.assertTrue(isinstance(cart_order.order_date, datetime))

    def test_product_status_field(self):
        cart_order = CartOrder.objects.get(id=1)
        self.assertEqual(cart_order.product_status, "processing")

    def test_sku_field(self):
        cart_order = CartOrder.objects.get(id=1)
        self.assertIsNotNone(cart_order.sku)

class CartOrderProductsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='adminheet@gmail.com', password='Heet$6537')

        test_order = CartOrder.objects.create(
            user=user, 
            price="15.99", 
            paid_status=False,
            product_status="processing"
        )

        CartOrderProducts.objects.create(
            order=test_order,
            invoice_no="INV12345",
            product_status="shipped",
            item="Milk",
            image="milk.jpg",
            qty=2,
            price="200.00",
            total="400.00"
        )

    def test_order_relation(self):
        order_product = CartOrderProducts.objects.get(invoice_no ="INV12345")
        self.assertEqual(order_product.order.user.username, 'adminheet@gmail.com')

    def test_invoice_no_field(self):
        order_product = CartOrderProducts.objects.get(invoice_no ="INV12345")
        self.assertEqual(order_product.invoice_no, "INV12345")

    def test_product_status_field(self):
        order_product = CartOrderProducts.objects.get(invoice_no ="INV12345")
        self.assertEqual(order_product.product_status, "shipped")

    def test_item_field(self):
        order_product = CartOrderProducts.objects.get(invoice_no ="INV12345")
        self.assertEqual(order_product.item, "Milk")

    def test_image_field(self):
        order_product = CartOrderProducts.objects.get(invoice_no ="INV12345")
        self.assertEqual(order_product.image, "milk.jpg")

    def test_qty_field(self):
        order_product = CartOrderProducts.objects.get(invoice_no ="INV12345")
        self.assertEqual(order_product.qty, 2)

    def test_price_field(self):
        order_product = CartOrderProducts.objects.get(invoice_no ="INV12345")
        self.assertEqual(order_product.price, 200.00)

    def test_total_field(self):
        order_product = CartOrderProducts.objects.get(invoice_no ="INV12345")
        self.assertEqual(order_product.total, 400.00)

class AddressModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='adminheet@gmail.com', password='Heet$6537')

        Address.objects.create(
            user=user, 
            mobile="6479200137",
            address="150, Mohawk Rd E",
            status=True
        )

    def test_user_relation(self):
        address = Address.objects.get(id=1)
        self.assertEqual(address.user.username, 'adminheet@gmail.com')

    def test_mobile_field(self):
        address = Address.objects.get(id=1)
        self.assertEqual(address.mobile, "6479200137")

    def test_address_field(self):
        address = Address.objects.get(id=1)
        self.assertEqual(address.address, "150, Mohawk Rd E")

    def test_status_field(self):
        user = User.objects.get(username='adminheet@gmail.com')
        Address.objects.create(user=user, mobile="0987654321", address="456, Python Avenue")
        address = Address.objects.get(mobile="0987654321")