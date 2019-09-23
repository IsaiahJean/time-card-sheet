from django.db import models

# Create your models here.


class Report(models.Model):
    name = models.CharField(max_length=30)
    file_number = models.DecimalField(max_digits=4, decimal_places=0)
    work_date = models.DateField()
    time_in = models.CharField(max_length=10)
    time_out = models.CharField(max_length=10)
    location = models.CharField(max_length=15)
    sector = models.CharField(max_length=5)
    hours_code = models.CharField(max_length=4)
    hours_worked = models.TimeField()
    report_date = models.DateTimeField(auto_now=True)
    fbp_billing = models.CharField(max_length=10)
    amco_billing = models.CharField(max_length=10)
    batch_id = models.CharField(max_length=10)
    company_code = models.CharField(max_length=10)
