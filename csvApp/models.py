from django.db import models


# Create your models here.
class Csv_File_model(models.Model):
    year=models.IntegerField()
    Industry_aggregation_NZSIOC=models.CharField(max_length=30)
    Industry_code_NZSIOC=models.CharField(max_length=30)
    Industry_name_NZSIOC=models.CharField(max_length=80)

    def __str__(self):
        return self.year
