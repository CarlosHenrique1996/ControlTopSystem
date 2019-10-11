
from accounts.models import Salesman
from sales.models import Sales, SalesItem

class Checkout():

    def create_sale(self, salesman_pk, payment):
        salesman = Salesman.objects.filter(pk=salesman_pk)
        if salesman:
            sale = Sales()
            sale.salesman = salesman.first()
            sale.payment = payment
            sale.save()
            return {'status': 202, 'message': 'Venda criada', 'sale_pk': sale.pk }
        else:
            return {'status': 502, 'message': 'Erro ao criar a venda.'}

    def create_sale_item(self, sale_pk, product, quantity):
        sale = Sales.objects.filter(pk=sale_pk)
        if sale:
            saleitem = SalesItem()
            saleitem.sales = sale.first()
            saleitem.product = product
            saleitem.quantity = quantity
            saleitem.price = product.price
            saleitem.save()
            return {'status': 202, 'message': 'Item da venda criada' }
        else:
            return {'status': 502, 'message': 'Erro ao criar a venda.'}