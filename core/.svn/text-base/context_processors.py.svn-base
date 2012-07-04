# -*- coding:utf-8 -*-
#Autor:guerra
#Data: 02/02/12
#Ultima alteracao:

from django.utils.safestring import mark_safe

from core.core_views import gera_menu_principal

def context_core(request):

    menu_principal = gera_menu_principal(request)

    return {
        "MENU_PRINCIPAL" : mark_safe(menu_principal)
    }