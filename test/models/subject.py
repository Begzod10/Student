from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class Subject(models.Model):
    name = models.CharField()


dtm_imtihon_fanlari = [
    "Ona tili",
    "Matematika",
    "Tarix",
    "Fizika",
    "Kimyo",
    "Biologiya",
    "Geografiya",
    "Ingliz tili",
    "Rus tili",
    "Qoraqalpoq tili",
    "Nemis tili",
    "Fransuz tili",
    "Koreys tili",
    "Xitoy tili",
    "Adabiyot"
]


@receiver(post_migrate)
def create_subjects(sender, **kwargs):
    for subject in dtm_imtihon_fanlari:
        Subject.objects.get_or_create(name=subject)
