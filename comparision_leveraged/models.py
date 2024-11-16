from django.db import models
from django_jalali.db import models as jmodels


class fund(models.Model):
    name=models.CharField(max_length=15)

class Financial_data(models.Model):
    fund = models.ForeignKey(fund, on_delete=models.CASCADE)
    BaseUnitsTotalNetAssetValue=models.DecimalField(decimal_places=1,max_digits=15)
    SuperUnitsTotalNetAssetValue=models.DecimalField(decimal_places=1,max_digits=15)
    Leverage_percentage=models.DecimalField(decimal_places=1,max_digits=15)
    date=jmodels.jDateField()

#Financial data based on date




# Create your models here.
