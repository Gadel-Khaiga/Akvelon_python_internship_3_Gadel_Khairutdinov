from django.db import models
import  random
# from django.contrib.auth import  get_user_model
# User = get_user_model()
# Create your models here.


class Wolf(models.Model):
    Trans_TYPE = (
        ('income', 'Income'),
        ('withdrawal of funds', 'Withdrawal of funds')
    )
    # user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='First Name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='Second Name', max_length=30, blank=True)
    email = models.CharField(verbose_name='email', unique=True, max_length=100, blank=True)
    transaction = models.IntegerField(verbose_name='Transaction', choices=Trans_TYPE)
    amount = models.CharField(verbose_name='amount', max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    Trans_from = models.CharField(verbose_name='From / To whom', max_length=100, blank=True)