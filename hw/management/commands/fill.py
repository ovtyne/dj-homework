from django.core.management import BaseCommand

from hw.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        category_list = [
            {'title': 'категория 1', 'description': 'описание категории 1'},
            {'title': 'категория 2', 'description': 'описание категории 2'},
            {'title': 'категория 3', 'description': 'описание категории 3'},
            {'title': 'категория 4', 'description': 'описание категории 4'},
            {'title': 'категория 5', 'description': 'описание категории 5'},
        ]

        categories_for_create = []
        for category_item in category_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_for_create)

        product_list = [
            {'title': 'продукт 1', 'description': 'описание продукта 1', 'category': categories_for_create [0], 'price': 100},
            {'title': 'продукт 2', 'description': 'описание продукта 2', 'category': categories_for_create [0], 'price': 50},
            {'title': 'продукт 3', 'description': 'описание продукта 3', 'category': categories_for_create [2], 'price': 70},
            {'title': 'продукт 4', 'description': 'описание продукта 4', 'category': categories_for_create [1], 'price': 23},
            {'title': 'продукт 5', 'description': 'описание продукта 5', 'category': categories_for_create [4], 'price': 67}
        ]


        products_for_create = []
        for product_item in product_list:
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_for_create)
