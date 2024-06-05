from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")
    description = models.TextField(verbose_name="Опиcание категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование", help_text="Введите название"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание"
    )
    preview = models.ImageField(
        upload_to="product/", **NULLABLE, verbose_name="Фото", help_text="Вставьте фото"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, **NULLABLE, related_name="products"
    )
    price = models.IntegerField(null=False, verbose_name="Цена продукта")
    created_at = models.DateField(**NULLABLE, auto_now_add=True)
    updated_at = models.DateField(**NULLABLE, auto_now_add=True)
    views_counter = models.PositiveIntegerField(
        default=0,
        verbose_name='Счетчик просмотров'
    )
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='version_product')
    number_version = models.SmallIntegerField(verbose_name='номер версии')
    name_version = models.CharField(max_length=150, verbose_name='название версии')
    is_active_version = models.BooleanField(verbose_name='Активна')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
