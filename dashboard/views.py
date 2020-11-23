from django.shortcuts import render, redirect
from django.http import HttpResponse
from staff.models import ManagerInfo, EmpInfo, Payment_details
from django.contrib.auth.models import User
from dashboard.forms import ManagerForm, EmpForm, CreateUserForm
from django.contrib.auth import authenticate , login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
import datetime
from dashboard.decorators import paymentCheck

import logging, traceback


import razorpay
client = razorpay.Client(auth=("rzp_test_yU3FAUN0xK1zJV", "dRz9xMgqAVEefkgtP1Q25lKE"))


#-----------

@csrf_exempt 
def Register(request):
    form = ManagerForm()
    userform = CreateUserForm()
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        userform = CreateUserForm(request.POST)
        if form.is_valid() and userform.is_valid():
            user = userform.save()
            form = form.save(commit = False)
            form.user = user
            form.email = user.email
            # form.payment_status = False
            Payment_details(user= user).save()
            form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('payment')
        else:
            print("Not Working")

    return render (request, "addform.html", {'form': form , 'userform': userform })

@login_required(login_url = 'login')
# @paymentCheck
def payment(request):
    user = ManagerInfo.objects.get(user= request.user)
    Payment = Payment_details.objects.get(user = request.user)

    # CREAING ORDER
    order_amount = "12000"
    order_currency = "INR"
    # order_receipt = "order_rcptid_11"
    # notes = user.name + user.email
    
    response = client.order.create(dict(amount=order_amount, currency=order_currency,  payment_capture='1'))    
    
    order_id = response['id']
    order_status = response['status']
    if order_status == "created":
        Payment.amount = order_amount
        Payment.order_id = order_id
        Payment.save()
        context = {"amount": order_amount,
                   "user": user,
                   "order_id": order_id }

        return render(request, "payment-page.html",context )
    return HttpResponse('<h1>Error in  create order function</h1>')
    

@csrf_exempt
@login_required(login_url = 'login')
# @paymentCheck
def payment_status(request):
    user = ManagerInfo.objects.get(user= request.user)
    payment = Payment_details.objects.get(user = request.user)
    
    date =  payment.payment_date + datetime.timedelta(days =365)
    print(date)
    response = request.POST

    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }

    # VERIFYING SIGNATURE
    try:
        # user.save(payment_status = "0")
        status = client.utility.verify_payment_signature(params_dict)
        # save payment details
        
        payment.razorpay_payment_id = response['razorpay_payment_id']
        payment.razorpay_order_id = response['razorpay_order_id']
        payment.razorpay_signature = response['razorpay_signature']
        # payment.save()
        # date = datetime.now() + datetime.timedelta(days =365) 
        payment.payment_end_date = date
        payment.save()

        #-------Status --------#
    
        user.payment_status = "true"
        user.save()
        #
        # client.payment.capture(dict("payment.razorpay_payment_id", "12000", {"currency":"INR"}))
        print("done")
        
        return render(request, 'order_summary.html', {'status': 'Payment Successful'})
    except:
        
        print("Fail")

        return render(request, 'order_summary.html', {'status': 'Payment Faliure!!!'})


#------------- Login View  -----------#
def Login(request):
    if request.user.is_authenticated:
        return redirect('emplist')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                username = User.objects.get(email=username).username
            except User.DoesNotExist:
                username = request.POST.get('username')
            user = authenticate(request, username= username, password=password )
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('emplist')
            else:
                messages.info(request, 'Username OR Password Wrong')
    return render (request, 'dashboard_templates/login.html')


# Logout view 
@login_required(login_url = 'login')
# @paymentCheck
def Logout(request):
    logout(request)
    logging.info("Logged Out") #logging INFO 
    return redirect('login')


# ---------------------- Dashboard Home  -------------------------
  
@login_required(login_url = 'login')
# @paymentCheck
def index(request):
       return render (request, 'dashboard_templates/dashboard.html')


# ------------------- Empl List -----------------------------
@login_required(login_url = 'login')
# @paymentCheck
def emp_list(request):
    # Query For Database (Employee)
    # manager = ManagerInfo.objects.get(user=request.user)
    # emplist = EmpInfo.objects.filter(manager = manager.id)
    manager_user = User.objects.get(username = request.user)
    emplist = EmpInfo.objects.filter(manager_user = manager_user).order_by('id')

    form = EmpForm()
    page = request.GET.get('page', 1)

    paginator = Paginator(emplist, 10)
    try:
        emplist = paginator.page(page)
    except PageNotAnInteger:
        emplist = paginator.page(1)
    except EmptyPage:
        emplist = paginator.page(paginator.num_pages)

    context = { 'emplist': emplist, 'form': form }
    return render (request, 'dashboard_templates/employee-list.html', context )


# ------------------- Add Employee -----------------------------

@login_required(login_url = 'login')
# @paymentCheck
def add_emp(request):
    form = EmpForm()
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username = request.user)
            form = form.save(commit = False)
            form.manager_user = user
            form.save()
            logging.info("Added Entry") #logging INFO 
    context = {'form': form }
    return redirect ('emplist')


# ------------------- Update Employee  -----------------------------

@login_required(login_url = 'login')
# @paymentCheck
def update_emp(request, id):
    employee = EmpInfo.objects.get(id=id)
    form = EmpForm(instance = employee)
    if request.method == 'POST':
        form = EmpForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()
            return redirect ('emplist')
    context = {'form': form, 'employee': employee }
    return render (request, 'dashboard_templates/employee-list.html', context )


# ------------------- Delete Employee  ---------------------
@login_required(login_url = 'login')
# @paymentCheck
def delete_emp(request, id):
    employee = EmpInfo.objects.get(id = id)
    if request.method == 'POST':
        employee.delete()
        return redirect('emplist')
    context = {'employee': employee }
    return render(request, 'dashboard_templates/employee-list.html', context )
