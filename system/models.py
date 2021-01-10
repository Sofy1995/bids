from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

# Create your models here.
class Bid(models.Model):

    print('models test print1')
    text = models.TextField(max_length=1000, help_text="Enter a brief description of the bid")

    TYPE_OF_BID = (
        ('h', 'hard'),
        ('c', 'cartridge'),
        ('pr', 'printer'),
        ('w', 'web or net'),
        ('t', 'telephone'),
        ('v', 'viruses'),
        ('s', 'soft'),
        ('pa', 'Parus'),
    )

    type_bid = models.CharField(max_length=2, choices=TYPE_OF_BID, blank=True, default='h')
    location = models.CharField(max_length=200, default='Location')
    print('hyation - (not need)', location)
    # location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    telephone_num = models.CharField(max_length=200, default='Number')
    # telephone_num = models.ForeignKey('Telephone', on_delete=models.SET_NULL, null=True)
    bider = models.CharField(max_length=200, default='Bider')
    # bider = models.ForeignKey('Bider', on_delete=models.SET_NULL, null=True)
    maker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    helper = models.CharField(max_length=200, default='Helper')
    # helper = models.ManyToManyField('Helper')
    time_creation = models.DateTimeField(auto_now=True)
    time_start = models.DateTimeField(null=True)
    time_done = models.DateTimeField(null=True)

    STATUS = (
        ('a', 'принята'),
        ('w', 'в работе'),
        ('f', 'выполнена'),
    )

    status = models.CharField(max_length=1, choices=STATUS, default='a')
    comment = models.CharField(max_length=200, default='')
    result = models.CharField(max_length=300, default='')

    class Meta:
        ordering = ["time_creation"]

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('bid-detail', args=[str(self.id)])

    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == 'f' and self.result == '':
            raise ValidationError({'status': 'Нельзя завершить заявку без результата.'})

# class Location(models.Model):
#     room = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.room

    # def get_adsolute_url(self):
    #     return reverse('locarion-detail', args=[str(self.id)])

# class Telephone(models.Model):
#     number = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.number
#
# class Bider(models.Model):
#     surname = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     father_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.surname + self.name[0] + self.father_name[0]


# class Maker(models.Model):
#     surname = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     father_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.surname + ' ' + self.name[0] + '. ' + self.father_name[0] + '.'
#
# class Helper(models.Model):
#     surname = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     father_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.surname + ' ' + self.name[0] + '. ' + self.father_name[0] + '.'
