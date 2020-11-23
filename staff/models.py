from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone

class ManagerInfo(models.Model):
    STATUS = [("true", "true"),
                ("false", "false"),]
    

    #---------------- User Manager --------------------#
    user = models.OneToOneField(User, null = True, on_delete= models.CASCADE )
    
    #-------------- Manager Details  --------------#
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    company_name  = models.CharField(max_length= 120, blank= True, null= True)
    birth_date = models.DateField(null= True, blank= True )
    home_address  = models.CharField(max_length= 250, blank= True, null= True)
    payment_status = models.CharField(choices= STATUS, max_length= 20, default= "false")

        
    def __str__(self):
        return self.first_name


class Payment_details(models.Model):

    user = models.OneToOneField(User, null = True, on_delete= models.CASCADE )
    amount = models.CharField(max_length= 1200, blank= True, null= True)
    order_id = models.CharField(max_length= 1200, blank= True, null= True)
    razorpay_order_id = models.CharField( max_length= 1200, blank= True, null= True)
    razorpay_payment_id = models.CharField( max_length= 1200, blank= True, null= True)
    razorpay_signature = models.CharField( max_length= 1200, blank= True, null= True)
    payment_date = models.DateField(default= timezone.now() , blank =True , null= True)
    payment_end_date = models.DateField(null= True, blank= True )

    def __str__(self):
        return str(self.user)
      

class EmpInfo(models.Model):
    
    #-------------- Employee Details  --------------#
    
    first_name = models.CharField(max_length=30, blank= False)
    last_name = models.CharField(max_length=30, blank = False)
    email = models.EmailField(blank= True, null= True)
    company_name  = models.CharField(max_length= 120, blank= True, null= True)
    mobile_number = models.CharField(max_length= 10, blank= True, null= True)
    birth_date = models.DateField(null= True, blank= True )
    home_address  = models.CharField(max_length= 250, blank= True, null= True)
    city = models.CharField(max_length= 25, blank= True, null= True)
    # emp_pwd = models.CharField(max_length= 25, blank= True, null= True)
    # manager= models.ForeignKey(ManagerInfo, on_delete=models.CASCADE, default= '1')
    manager_user= models.ForeignKey(User, on_delete=models.CASCADE, default = 1)


def __str__(self):
    return self.first_name
    