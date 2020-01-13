import logging

logger = logging.getLogger("easyops")


def initial_session(user, request):

    PermissionsQuerySet = user.roles.values("permissions__permname", "permissions__url", "permissions__menu__id", "permissions__menu__menuname", "permissions__menu__icon", "permissions__menu__levelmenu").distinct()
    permission_list = []
    # 菜单字典
    permission_menu_dict = {}
    logger.debug("PermissionsQuerySet: {}".format(PermissionsQuerySet))
    # 二级菜单
    ClassMenu = list()

    for item in PermissionsQuerySet:
        if item.get("permissions__menu__menuname", ""):
            # 生成一级菜单
            if not item.get("permissions__menu__levelmenu"):
                # 是否有Dashboard，如果有Dashboard在菜单列表中显示在第一
                if item.get("permissions__menu__menuname") == "Dashboard":
                    permission_menu_dict[item.get("permissions__menu__id")] = {
                        "menuname": item.get("permissions__menu__menuname"),
                        "icon": item.get("permissions__menu__icon"),
                        "children": [
                        ]
                    }

    for item in PermissionsQuerySet:
        # 权限列表
        if item.get("permissions__url"):
            permission_list.append(item.get("permissions__url"))
        if item.get("permissions__menu__menuname", ""):
            # 生成一级菜单
            if not item.get("permissions__menu__levelmenu"):
                if not item.get("permissions__menu__menuname") == "Dashboard":
                    permission_menu_dict[item.get("permissions__menu__id")] = {
                        "menuname": item.get("permissions__menu__menuname"),
                        "icon": item.get("permissions__menu__icon"),
                        "children": [
                        ]
                    }
            else:
                ClassMenu.append(item)
    logger.debug("permission_menu_dict: {}".format(permission_menu_dict))
    logger.debug("ClassMenu: {}".format(ClassMenu))

    for item in ClassMenu:
        if item.get("permissions__menu__levelmenu") in permission_menu_dict:
            permission_menu_dict.get(item.get("permissions__menu__levelmenu")).get("children").append(
                {
                    "menuname": item.get("permissions__menu__menuname"),
                    "icon": item.get("permissions__menu__icon"),
                    "menuid": item.get("permissions__menu__id"),
                    "url": item.get("permissions__url")
                }
            )

    request.session["permission_list"] = permission_list
    request.session["permission_menu_dict"] = permission_menu_dict
    logger.debug("用户：{}, permission_list： {}, permission_menu_dict: {}".format(request.user.username, permission_list, permission_menu_dict))

