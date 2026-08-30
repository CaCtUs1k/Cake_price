from django.db import models

class Cake(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва торта")
    image = models.ImageField(upload_to='cakes/', verbose_name="Картинка для детального огляду товару")
    preview_image = models.ImageField(upload_to='cakes/previews/', blank=True, null=True, verbose_name="Картинка для каталогу")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Базова ціна")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Торт"
        verbose_name_plural = "Торти"

class RuleSettings(models.Model):
    min_order_weight = models.PositiveIntegerField(default=2, verbose_name="Мінімальна вага замовлення (кг)")
    two_tier_min_weight = models.PositiveIntegerField(default=4, verbose_name="Мін. вага двоповерхового (кг)")
    different_fillings_min_weight = models.PositiveIntegerField(default=5, verbose_name="Мін. вага для різних начинок (кг)")
    tier_construction_price = models.PositiveIntegerField(default=250, verbose_name="Ціна конструкції для ярусного (грн)")
    weight_tolerance = models.PositiveIntegerField(default=300, verbose_name="Похибка ваги (+/- г)")
    portion_weight = models.PositiveIntegerField(default=200, verbose_name="Розрахунок на людину (+/- г)")
    velour_price_per_kg = models.PositiveIntegerField(default=200, verbose_name="Ціна велюрового покриття (грн/кг)")
    trifle_price = models.PositiveIntegerField(default=150, verbose_name="Ціна трайфлу (грн/шт)")
    bento_price = models.PositiveIntegerField(default=750, verbose_name="Ціна бенто торта (грн)")
    bento_1kg_price = models.PositiveIntegerField(default=1100, verbose_name="Ціна бенто 1 кг (грн)")

    def __str__(self):
        return "Налаштування правил та умов"

    class Meta:
        verbose_name = "Налаштування правил"
        verbose_name_plural = "Налаштування правил"

class Filling(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва начинки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Начинка"
        verbose_name_plural = "Начинки"

class SiteSettings(models.Model):
    telegram = models.URLField(max_length=200, blank=True, verbose_name="Посилання на Telegram")
    instagram = models.URLField(max_length=200, blank=True, verbose_name="Посилання на Instagram")
    facebook = models.URLField(max_length=200, blank=True, verbose_name="Посилання на Facebook")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Номер телефону")

    def save(self, *class_self, **kwargs):
        # Гарантуємо, що в базі завжди буде лише один рядок налаштувань
        self.pk = 1
        super().save(*class_self, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Налаштування сайту та соцмереж"

    class Meta:
        verbose_name = "Налаштування сайту"
        verbose_name_plural = "Налаштування сайту"