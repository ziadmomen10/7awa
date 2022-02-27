from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.fields import IntegerField

# Create your models here.

class RiskCalculator(models.Model):

    risk_id = models.IntegerField(primary_key = True)
    risk_question = models.CharField(max_length=200)


class OprateRisk(models.Model):

    ope_risk_id = models.IntegerField(primary_key = True)
    ope_risk_date = models.DateField()
    ope_risk_answer = models.DecimalField(max_digits=20, decimal_places=10)
    ope_risk_result = models.DecimalField(max_digits=20, decimal_places=10)

class Prediction(models.Model):

    pred_id = models.IntegerField(primary_key = True)
    pred_feature1 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature2 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature3 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature4 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature5 = models.DecimalField(max_digits=20, decimal_places=10)

class Diagnos(models.Model):

    diag_id = models.IntegerField(primary_key = True)
    diag_date = models.DateField()
    diag_diagnosis = models.CharField(max_length=50)

class Examination(models.Model):

    ex_id = models.IntegerField(primary_key = True)
    ex_question = models.CharField(max_length=200) 
    ex_result = models.CharField(max_length=200)

class OprateExamination(models.Model):

    ope_ex_id = models.IntegerField(primary_key = True)
    ope_ex_date = models.DateField()
    ope_ex_answer = models.DateField()

class Phone(models.Model):

    pho_id = models.IntegerField(primary_key = True)
    pho_number = models.IntegerField()
    

class PeriodDate(models.Model):

    per_date_id = models.IntegerField(primary_key = True)
    per_date = models.DateField()



class user(models.Model):

    us_id = models.IntegerField(primary_key = True)
    us_firstname = models.CharField(max_length=50)
    us_lastname = models.CharField(max_length=50)
    us_email = models.CharField(max_length=50)
    us_birthdate = models.DateField(max_length=50)
    us_rathe = models.CharField(max_length=50)
    phone = models.ForeignKey(Phone, unique=True, null=True, on_delete=models.CASCADE)