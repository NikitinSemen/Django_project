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
    created_at = models.DateField(**NULLABLE)
    updated_at = models.DateField(**NULLABLE)
    views_counter = models.PositiveIntegerField(
        default=0,
        verbose_name='Счетчик просмотров'
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(
        max_length=200, verbose_name='Заголовок', help_text="Введите заголовок"
    )
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='Текст поста', help_text='Введите содержимое поста')
    photo = models.ImageField(upload_to='blog/', verbose_name='фото', help_text='Вставьте фото')
    created_at = models.DateField(**NULLABLE)
    is_published = models.BooleanField(default=True)
    views_counter = models.PositiveIntegerField(
        default=0,
        verbose_name='Счетчик просмотров'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
