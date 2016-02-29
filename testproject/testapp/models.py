from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class TestModel(models.Model):
    """Basic Field Test"""
    name = models.CharField(max_length=255, blank=True, default='')
    phone = PhoneNumberField()


class TestModelPhoneB(models.Model):
    """Field Test for when Blank"""
    name = models.CharField(max_length=255, blank=True, default='')
    phone = PhoneNumberField(blank=True)


class TestModelPhoneNU(models.Model):
    """Field Test for when Null & Unique"""
    name = models.CharField(max_length=255, blank=True, default='')
    phone = PhoneNumberField(null=True, unique=True)


class TestModelPhoneBNU(models.Model):
    """Field Test for when Blank, Null & Unique"""
    name = models.CharField(max_length=255, blank=True, default='')
    phone = PhoneNumberField(blank=True, null=True, unique=True)


class TestModelPhoneNDNU(models.Model):
    """Field Test for when No Default, Null & Unique"""
    name = models.CharField(max_length=255, blank=True, default='')
    phone = PhoneNumberField(default=models.NOT_PROVIDED, null=True, unique=True)


class TestModelPhoneBNDNU(models.Model):
    """Field Test for when Blank, No Default, Null & Unique"""
    name = models.CharField(max_length=255, blank=True, default='')
    phone = PhoneNumberField(blank=True, default=models.NOT_PROVIDED, null=True, unique=True)


class TestModelPhoneDNU(models.Model):
    """Field Test for when Default, Null & Unique"""
    name = models.CharField(max_length=255, blank=True, default='')
    phone = PhoneNumberField(
        default='+41524242424', null=True, unique=True)


class TestModelPhoneBDNU(models.Model):
    """Field Test for when Blank, Default, Null & Unique"""
    name = models.CharField(max_length=255, blank=True, default='')
    phone = PhoneNumberField(
        blank=True, default='+41524242424', null=True, unique=True)


class TestModelPhoneEDNU(models.Model):
    """Field Test for when Empty Default, Null & Unique"""
    name = models.CharField(max_length=255, blank=True, default='')
    phone = PhoneNumberField(
        default='', null=True, unique=True)


class TestModelPhoneBEDNU(models.Model):
    """Field Test for when Blank, Empty Default, Null & Unique"""
    name = models.CharField(max_length=255, blank=True, default='')
    phone = PhoneNumberField(
        blank=True, default='', null=True, unique=True)
