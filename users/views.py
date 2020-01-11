from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from users.utils.permission import initial_session
from django.db import transaction
from django.db.models import Q, Count
from django.utils.http import urlquote
from django.http import FileResponse
from django.views import View
from users import models
import logging
import traceback
import json
from users.utils.celery_tasks import emilpattern, phonepattern, get_random_code, send_msg_mail

# Create your views here.

logger = logging.getLogger(__name__)


class UserListView(View):

    @method_decorator(login_required)
    def get(self, request):
        UserQuerySet = models.UserProfile.objects.all()
        return render(request, "users/users.html", {"UserQuerySet": UserQuerySet})

    @method_decorator(login_required)
    def post(self, request):

        return


class UserDetailView(View):

    @method_decorator(login_required)
    def get(self, request):
        UserQuerySet = models.UserProfile.objects.all()
        return render(request, "users/users.html", {"UserQuerySet": UserQuerySet})

    @method_decorator(login_required)
    def post(self, request):

        return


class RoleListView(View):

    @method_decorator(login_required)
    def get(self, request):
        RoleQuerySet = models.Role.objects.all()
        return render(request, "users/role.html", {"RoleQuerySet": RoleQuerySet})

    @method_decorator(login_required)
    def post(self, request):
        return


class RoleDetailView(View):

    @method_decorator(login_required)
    def get(self, request):
        RoleQuerySet = models.Role.objects.all()
        return render(request, "users/role.html", {"RoleQuerySet": RoleQuerySet})

    @method_decorator(login_required)
    def post(self, request):
        return


class PermissionListView(View):

    @method_decorator(login_required)
    def get(self, request):
        PermQuerySet = models.Permission.objects.all()
        return render(request, "users/permission.html", {"PermQuerySet": PermQuerySet})

    @method_decorator(login_required)
    def post(self, request):
        return


class PermissionDetailView(View):

    @method_decorator(login_required)
    def get(self, request):
        PermQuerySet = models.Permission.objects.all()
        return render(request, "users/permission.html", {"PermQuerySet": PermQuerySet})

    @method_decorator(login_required)
    def post(self, request):
        return


class MenuListView(View):

    @method_decorator(login_required)
    def get(self, request):
        MenuQuerySet = models.Menu.objects.all()
        return render(request, "users/menu.html", {"MenuQuerySet": MenuQuerySet})

    @method_decorator(login_required)
    def post(self, request):
        return


class MenuDetailView(View):

    @method_decorator(login_required)
    def get(self, request):
        MenuQuerySet = models.Menu.objects.all()
        return render(request, "users/menu.html", {"MenuQuerySet": MenuQuerySet})

    @method_decorator(login_required)
    def post(self, request):
        return


class UsersGroupListView(View):
    @method_decorator(login_required)
    def get(self, request):
        UserGroupQuerySet = models.UserGroup.objects.all()
        return render(request, "users/menu.html", {"UserGroupQuerySet": UserGroupQuerySet})

    @method_decorator(login_required)
    def post(self, request):
        return


class UsersGroupDetailView(View):
    @method_decorator(login_required)
    def get(self, request):
        UserGroupQuerySet = models.UserGroup.objects.all()
        return render(request, "users/menu.html", {"UserGroupQuerySet": UserGroupQuerySet})

    @method_decorator(login_required)
    def post(self, request):
        return


# class FileDownloadView(View):
#     @method_decorator(login_required)
#     def get(self, request, *args, **kwargs):
#         """
#         文件下载
#         :param request:
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         wk_enclosure_id = args[0]
#         WkReplies = models.WorkOrderReplies.objects.filter(id=wk_enclosure_id).first()
#         file = open(WkReplies.wk_enclosure_path, 'rb')
#         response = FileResponse(file)
#         response['Content-Type'] = 'application/octet-stream'
#         response['Content-Disposition'] = 'attachment;filename="{}"'.format(urlquote(WkReplies.wk_enclosure_name))
#         return response


def Service500View(request):
    return render(request, "base/500.html")


def Service403View(request):
    return render(request, "base/403.html")


def Service404View(request):
    return render(request, "base/404.html")


def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        userobj = authenticate(username=username, password=password)
        if userobj:
            login(request, userobj)
            request.session["user_id"] = userobj.pk
            initial_session(user=userobj, request=request)
            # return redirect(request.GET.get('next') or '/')
            return redirect("/")
        else:
            message = '用户名或密码错误'
    return render(request, "base/login.html", locals())


class CustompwdView(View):

    @method_decorator(login_required)
    def get(self, request):
        return render(request, "users/custompwd.html")

    @method_decorator(login_required)
    def post(self, request):
        oldpassword = request.POST.get("oldpassword")
        userobj = authenticate(username=request.user.username, password=oldpassword)
        if userobj:
            new_pwd1 = request.POST.get("password1")
            new_pwd2 = request.POST.get("password2")
            if new_pwd1 == new_pwd2:
                userobj.set_password(new_pwd2)
                userobj.save()
                logout(request)
                return JsonResponse({"code": 200, "message": "密码修改成功"})
            else:
                return JsonResponse({"code": 100, "message": "两次密码输入不一致"})
        else:
            return JsonResponse({"code": 100, "message": "用户名或邮箱不正确"})


class LogoutView(View):
    """
    退出登录
    """

    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return redirect("/login/")


class ResetPaswordView(View):

    def get(self, request):

        return render(request, "base/restpd.html")

    def post(self, request):
        # result = {"code": 0, "msg": "SUCCESS"}

        validation_username = request.POST.get("validation_username")
        validation_email = request.POST.get("validation_email")
        if not emilpattern.match(validation_email):
            # return JsonResponse({"code": 1, "msg": "邮箱格式不正确"})
            return JsonResponse({"code": 100, "message": "邮箱格式不正确"})
        pwd = get_random_code(10)
        userobj = models.UserProfile.objects.filter(
            Q(email=validation_email) and Q(username=validation_username)).first()
        if not userobj:
            # result["code"] = 1
            # result["msg"] = "用户名或邮箱不正确"
            # return JsonResponse({"result": result})
            return JsonResponse({"code": 100, "message": "用户名或邮箱不正确"})
        userobj.set_password(pwd)
        userobj.save()

        try:
            send_msg_mail.delay(userobj.email, email_body="密码：{}".format(pwd), email_title="工单系统密码重置成功")

        except Exception as er:
            logger.error(er)
        # result["msg"] = "密码重置成功，请查收手机短信或邮件"
        # return JsonResponse({"result": result})
        return JsonResponse({"code": 200, "message": "密码重置成功，请查收手机短信或邮件"})
