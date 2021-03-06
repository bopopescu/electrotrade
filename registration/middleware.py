from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.utils.deprecation import MiddlewareMixin
from .forms import *
from electonicswebservice.admininfo import *
from django.http import HttpResponse, JsonResponse
from .TokenAuthentigetion import *
import traceback
from django.utils.functional import SimpleLazyObject
import os
import sys
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
import json
from django.forms.models import model_to_dict

View_class = ['user_delete', 'user_register', 'user_login', 'index', 'login', 'forget_password',
              'verify_forget_password', 'media', 'serve', 'login_with_otp_send', 'login_with_otp_verify']


class CommonMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            if request.user.is_authenticated:
                return None
            if view_func.__name__ not in View_class:
                token_authentication = user_token_authentication(request)
                if token_authentication is None:
                    return_json['valid'] = False
                    return_json['message'] = "Token Not Found"
                    return_json['count_result'] = 1
                    return_json['data'] = None
                    return JsonResponse(return_json, status=200)
                elif isinstance(token_authentication, dict):
                    if "Error" in token_authentication:
                        return_json['valid'] = False
                        return_json['message'] = token_authentication['Error']
                        return_json['count_result'] = 1
                        return_json['data'] = None
                        return JsonResponse(return_json, status=200)
                elif token_authentication:
                    request.COOKIES['id'] = token_authentication.account_id
                    if request.method == "POST":
                        return None
                    return None
                else:
                    return_json['valid'] = False
                    return_json['message'] = "Token Authentication Failed"
                    return_json['count_result'] = 1
                    return_json['data'] = None
                    return JsonResponse(return_json, status=200)
            else:
                token_authentication = user_token_authentication(request)
                if token_authentication is None:
                    return None
                if isinstance(token_authentication, dict):
                    if "Error" in token_authentication:
                        return_json['valid'] = False
                        return_json['message'] = "Token Not Found"
                        return_json['count_result'] = 1
                        return_json['data'] = None
                        return JsonResponse({'Error': token_authentication['Error']},
                                            status=200)
                elif token_authentication:
                    request.session['last_activity'] = str(datetime.now())
                    return_json['valid'] = False
                    return_json['message'] = "Token Not Found"
                    return_json['count_result'] = 1
                    return_json['data'] = None
                    return JsonResponse({"UserData": UserInfo(token_authentication)}, status=200)
                else:
                    return None
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(str((e, exc_type, f_name, exc_tb.tb_lineno)))
            return_json['valid'] = False
            return_json['message'] = f"{e}, {f_name}, {exc_tb.tb_lineno}"
            return_json['count_result'] = 1
            return_json['data'] = None
            return JsonResponse(return_json, status=200)


class StandardExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        logger.error(exception)
        if request.user.is_authenticated:
            return_json['valid'] = False
            return_json['message'] = str(exception)
            return_json['count_result'] = 1
            return_json['data'] = None
            return JsonResponse(return_json, status=200, safe=False)
        elif Register.objects.filter(account_id=request.COOKIES['id']).exists():
            return_json['valid'] = False
            return_json['message'] = str(exception)
            return_json['count_result'] = 1
            return_json['data'] = None
            return_json['data'] = UserInfo(Register.objects.get(account_id=request.COOKIES['id']))
            return JsonResponse(return_json, status=200, safe=False)
        return_json['valid'] = False
        return_json['message'] = str(exception)
        return_json['count_result'] = 1
        return_json['data'] = None
        return JsonResponse(return_json, status=200, safe=False)


class UserRegisterMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            if request.method == "POST":
                form = RegisterForm(request.POST)
                if not form.is_valid():
                    if form.errors:
                        error = eval(form.errors.as_json())
                        if '__all__' in error:
                            error = error['__all__'][0]['message']
                        return_json['valid'] = False
                        return_json['message'] = error
                        return_json['count_result'] = 1
                        return_json['data'] = None
                        logger.error(form.errors)
                        return JsonResponse(return_json, status=200)
                else:
                    return view_func(request, form)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(e)
            return_json['valid'] = False
            return_json['message'] = f'{e}, {f_name}, {exc_tb.tb_lineno}'
            return_json['count_result'] = 1
            return_json['data'] = None
            return JsonResponse(return_json, status=200)


class LoginMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            if request.method == "POST":
                form = LoginForm(request.POST)
                if not form.is_valid():
                    if form.errors:
                        error = eval(form.errors.as_json())
                        if '__all__' in error:
                            error = eval(error['__all__'][0]['message'])[0]
                        return_json['valid'] = False
                        return_json['message'] = error
                        return_json['count_result'] = 1
                        return_json['data'] = None
                        logger.error(form.errors)
                        return JsonResponse(return_json, status=200)
                else:
                    return view_func(request, form)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(e)
            return_json['valid'] = False
            return_json['message'] = f'{e}, {f_name}, {exc_tb.tb_lineno}'
            return_json['count_result'] = 1
            return_json['data'] = None
            return JsonResponse(return_json, status=200)

    def process_template_response(self, request, response):
        return response


class ProfileMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            userprofiledata = Register.objects.get(account_id=request.COOKIES['id'])
            if request.method == "POST":
                form = UserProfileEditForm(request.POST, request.FILES)
                if not form.is_valid():
                    if form.errors:
                        error = eval(form.errors.as_json())
                        if '__all__' in error:
                            error = eval(error['__all__'][0]['message'])[0]
                        return_json['valid'] = False
                        return_json['message'] = error
                        return_json['count_result'] = 1
                        return_json['data'] = UserInfo(userprofiledata)
                        logger.error(form.errors)
                        return JsonResponse(return_json, status=200)
                else:
                    return view_func(request, form)
            else:
                userprofiledata_json = UserInfo(userprofiledata)
                userprofiledata_json['city_list'] = city_json_data(City.objects.all())
                userprofiledata_json['state_list'] = state_json_data(State.objects.all())
                userprofiledata_json['business_type_list'] = business_type_json_data(BusinessType.objects.all())
                return_json['valid'] = True
                return_json['message'] = "Successfully Update"
                return_json['count_result'] = 1
                return_json['data'] = userprofiledata_json
                return JsonResponse(return_json, status=200)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(e)
            return_json['valid'] = False
            return_json['message'] = f'{e}, {f_name}, {exc_tb.tb_lineno}'
            return_json['count_result'] = 1
            return_json['data'] = None
            return JsonResponse(return_json, status=200)

    def process_template_response(self, request, response):
        return response


class LoginWithOtpSendMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == "POST":
            form = LoginWithOtpSendForm(request.POST)
            if not form.is_valid():
                if form.errors:
                    error = eval(form.errors.as_json())
                    if '__all__' in error:
                        error = error['__all__'][0]['message']
                    return_json['valid'] = False
                    return_json['message'] = error
                    return_json['count_result'] = 1
                    return_json['data'] = None
                    logger.error(form.errors)
                    return JsonResponse(return_json, status=200)
            else:
                return view_func(request, form)

    def process_template_response(self, request, response):
        return response


class LoginWithOtpVerifyMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == "POST":
            form = LoginWithOtpVerifyForm(request.POST)
            if not form.is_valid():
                if form.errors:
                    error = eval(form.errors.as_json())
                    if '__all__' in error:
                        error = eval(error['__all__'][0]['message'])[0]
                    return_json['valid'] = False
                    return_json['message'] = error
                    return_json['count_result'] = 1
                    return_json['data'] = None
                    logger.error(form.errors)
                    return JsonResponse(return_json, status=200)
            else:
                return view_func(request, form)

    def process_template_response(self, request, response):
        return response