from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _


class Partner(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('nome'))
    reg_id = models.CharField(max_length=50, verbose_name=_('registro de matrícula'), null=True, blank=True, default='')
    document_id = models.CharField(unique=True, max_length=150, verbose_name=_('numero do documento'))
    slug = models.SlugField(max_length=150, verbose_name=_('slug'), default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, db_column="user")

    class Meta:
        ordering = ['name']
        verbose_name = _('proprietário')
        verbose_name_plural = _('proprietários')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Cria a matrícula utilizando o id
        if not self.pk:
            person = super(Partner, self).save(*args, **kwargs)
            code = 'PR{id}05d'.format(id=self.id)
            self.reg_id = code
            self.save()
        else:
            person = super(Partner, self).save(*args, **kwargs)
        return person


class VehicleModel(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('modelo'))
    slug = models.SlugField(max_length=150, verbose_name=_('slug'), default='')

    class Meta:
        ordering = ['name']
        verbose_name = _('modelo')
        verbose_name_plural = _('modelos')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('fabricante'))
    slug = models.SlugField(max_length=150, verbose_name=_('slug'), default='')

    class Meta:
        ordering = ['name']
        verbose_name = _('fabricante')
        verbose_name_plural = _('fabricantes')

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    plate_num = models.CharField(unique=True, max_length=7, verbose_name=_('numero da placa'))
    chassis_num = models.CharField(unique=True, max_length=17, verbose_name=_('número de chassis'))
    model = models.ForeignKey(VehicleModel, verbose_name=_('modelo'), on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, verbose_name=_('fabricante'), on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Partner, verbose_name=_('proprietário'), on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, db_column="user")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('data da criação do registro'))
    slug = models.SlugField(max_length=150, verbose_name=_('slug'), default='')

    class Meta:
        ordering = ['user']
        verbose_name = _('veículo')
        verbose_name_plural = _('veículos')

    def __str__(self):
        return '{owner} - {model} - {plate}'.format(owner=self.owner.name, model=self.model, plate=self.plate_num)
