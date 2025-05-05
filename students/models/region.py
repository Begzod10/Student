from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

provinces_data = [
    {"id": "1", "name_uz": "Qoraqalpogʻiston Respublikasi", "name_oz": "Қорақалпоғистон Республикаси",
     "name_ru": "Республика Каракалпакстан", "name_en": "Republic of Karakalpakstan"},
    {"id": "2", "name_uz": "Andijon viloyati", "name_oz": "Андижон вилояти", "name_ru": "Андижанская область",
     "name_en": "Andijan Region"},
    {"id": "3", "name_uz": "Buxoro viloyati", "name_oz": "Бухоро вилояти", "name_ru": "Бухарская область",
     "name_en": "Bukhara Region"},
    {"id": "4", "name_uz": "Jizzax viloyati", "name_oz": "Жиззах вилояти", "name_ru": "Джизакская область",
     "name_en": "Jizzakh Region"},
    {"id": "5", "name_uz": "Qashqadaryo viloyati", "name_oz": "Қашқадарё вилояти", "name_ru": "Кашкадарьинская область",
     "name_en": "Qashqadaryo Region"},
    {"id": "6", "name_uz": "Navoiy viloyati", "name_oz": "Навоий вилояти", "name_ru": "Навоийская область",
     "name_en": "Navoi Region"},
    {"id": "7", "name_uz": "Namangan viloyati", "name_oz": "Наманган вилояти", "name_ru": "Наманганская область",
     "name_en": "Namangan Region"},
    {"id": "8", "name_uz": "Samarqand viloyati", "name_oz": "Самарқанд вилояти", "name_ru": "Самаркандская область",
     "name_en": "Samarkand Region"},
    {"id": "9", "name_uz": "Surxondaryo viloyati", "name_oz": "Сурхондарё вилояти",
     "name_ru": "Сурхандарьинская область", "name_en": "Surxondaryo Region"},
    {"id": "10", "name_uz": "Sirdaryo viloyati", "name_oz": "Сирдарё вилояти", "name_ru": "Сырдарьинская область",
     "name_en": "Sirdaryo Region"},
    {"id": "11", "name_uz": "Toshkent viloyati", "name_oz": "Тошкент вилояти", "name_ru": "Ташкентская область",
     "name_en": "Tashkent Region"},
    {"id": "12", "name_uz": "Fargʻona viloyati", "name_oz": "Фарғона вилояти", "name_ru": "Ферганская область",
     "name_en": "Fergana Region"},
    {"id": "13", "name_uz": "Xorazm viloyati", "name_oz": "Хоразм вилояти", "name_ru": "Хорезмская область",
     "name_en": "Khorezm Region"},
    {"id": "14", "name_uz": "Toshkent shahri", "name_oz": "Тошкент шаҳри", "name_ru": "Город Ташкент",
     "name_en": "City of Tashkent"}
]


class Region(models.Model):
    name = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, null=True)
    name_en = models.CharField(max_length=255, null=True)
    name_oz = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'students'


class District(models.Model):
    name = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@receiver(post_migrate)
def create_regions(sender, **kwargs):
    for province in provinces_data:
        Region.objects.get_or_create(
            name=province['name_uz'],

        )
