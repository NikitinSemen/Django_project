from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(*args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category = [
            {'name': 'Продовольственные товары', 'description': 'кисломолчка, бакалея, мясные полуфабрикаты'},
            {'name': 'электроника', 'description': 'телевизоры, приставки, комплектующие'},
            {'name': 'Холодильное оборудование', 'description': 'морозильные камеры, бытовые холодильники'}
        ]

        category_list_for_fill = []
        for item in category:
            category_list_for_fill.append(
                Category(**item)
            )
        Category.objects.bulk_create(category_list_for_fill)
        prod, electro, refreg = Category.objects.all()

        product = [
            {'name': 'Творог обезжиреный', 'description': 'Творог жирностью 0.5%', 'category': prod, 'price': 120},
            {'name': 'LG 219d285', 'description': 'Диагональ 81см, блютуз поддержка, подключение к wifi',
             'category': electro, 'price': 21000},
            {'name': 'Hersun', 'description': 'Морозильник вместительный, серого цвета, оснащен четырьмя полками',
             'category': refreg, 'price': 7000}
        ]
        product_list_for_fill = []
        for item in product:
            product_list_for_fill.append(
                Product(**item)
            )
        Product.objects.bulk_create(product_list_for_fill)
