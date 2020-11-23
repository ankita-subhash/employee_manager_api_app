from django.shortcuts import redirect
from staff.models import ManagerInfo, Payment_details
# import datetime

def unauthenticated_user(view_func):
    def wrapper_func(request, *awrgs, **kawrgs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request, *awrgs, **kawrgs)
    return wrapper_func
    

def paymentCheck(view_func):
    def wrapper_func(request, *awrgs, **kawrgs):
        user = ManagerInfo.objects.get(user= request.user)
        if user.payment_status == "false":
            return redirect('payment')
        else:
            return view_func(request, *awrgs, **kawrgs)
    return wrapper_func

# def paymentChange(view_func):
#     def wrapper_func(request, *awrgs, **kawrgs):
#         user = UserInfo.objects.get(user= request.user)
#         payment_details = Payment_details.objects.get(user = user) 
#         if user.payment_status == "false":
#             return redirect('payment')
#         else:
#             return view_func(request, *awrgs, **kawrgs)
#     return wrapper_func