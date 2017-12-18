from django.db import models
import json


# Create your models here.
class Mineral(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    image_filename = models.CharField(max_length=255, blank=True)
    image_caption = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    formula = models.CharField(max_length=255, blank=True)
    strunz_classification = models.CharField(max_length=255, blank=True)
    crystal_system = models.CharField(max_length=255, blank=True)
    unit_cell = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=255, blank=True)
    crystal_symmetry = models.CharField(max_length=255, blank=True)
    cleavage = models.CharField(max_length=255, blank=True)
    mohs_scale_hardness = models.CharField(max_length=255, blank=True)
    luster = models.CharField(max_length=255, blank=True)
    streak = models.CharField(max_length=255, blank=True)
    diaphaneity = models.CharField(max_length=255, blank=True)
    optical_properties = models.CharField(max_length=255, blank=True)
    group = models.CharField(max_length=255, blank=True)
    refractive_index = models.CharField(max_length=255, blank=True)
    crystal_habit = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


# minerals = json.load(open('minerals.json'))


# for mineral in minerals:
#     Mineral.objects.create(
#         name=mineral.get('name', ''),
#         image_filename=mineral.get('image filename', ''),
#         image_caption=mineral.get('image caption', ''),
#         category=mineral.get('category', ''),
#         formula=mineral.get('formula', ''),
#         strunz_classification=mineral.get('strunz classification', ''),
#         crystal_system=mineral.get('crystal system', ''),
#         unit_cell=mineral.get('unit cell', ''),
#         color=mineral.get('color', ''),
#         crystal_symmetry=mineral.get('crystal symmetry', ''),
#         cleavage=mineral.get('cleavage', ''),
#         mohs_scale_hardness=mineral.get('mohs scale hardness', ''),
#         luster=mineral.get('luster', ''),
#         streak=mineral.get('streak', ''),
#         diaphaneity=mineral.get('diaphaneity', ''),
#         optical_properties=mineral.get('optical properties', ''),
#         group=mineral.get('group', ''),
#         refractive_index=mineral.get('refractive index', ''),
#         crystal_habit=mineral.get('crystal habit', ''),
#     )

