from django.db import models
# from django.core.validators import MaxValueValidator, RegexValidator
#
#
# class Student(models.Model):
#     pro_name = models.CharField(max_length=100, null=True)
#     # age = models.IntegerField(max_length=100, null=True)
#     pro_price = models.CharField(primary_key=False, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
#
#     # address = models.CharField(max_length=200, blank=True)
#     # def __str__(self):
#     #     return self.age