from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse
import re
import logging

logger = logging.getLogger("tickets")


class ValidPermission(MiddlewareMixin):

    def process_request(self, request):
        # 当前用户访问的URL
        current_path = request.path_info
        logger.debug("当前用户请求的URL：{}".format(current_path))
        # 白名单
        if current_path == "/":
            return None
        valid_url_list = ["/login/", "/users/login/", "/logout/", "/users/logout/", "/admin/.*", "/500/", "/404/", "/403/", "/media/*", "/reretpwd/", "/custompwd/"]
        for url in valid_url_list:
            if re.match(url, current_path):
                return None

        # 校验是否登录
        user_id = request.session.get("user_id")
        logger.debug("user_id: {}".format(user_id))
        if not user_id:
            return redirect("/login/")

        for item in request.session.get("permission_list"):
            # tiem  /users/delete/(\d+)
            reg = "^%s$" % item     # ^/users/delete/(\d+)$
            res = re.match(reg, current_path)
            if res:
                return None

        return render(request, "base/403.html")
