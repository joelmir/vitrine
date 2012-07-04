# -*- coding:utf-8 -*-
#Autor:guerra
#Data: 02/02/12
#Ultima alteracao:

from django.utils.safestring import mark_safe
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
from django.conf import settings


def homepage(request):
    '''
    Metodo que carrega a Homepage do site
    '''

    return render_to_response("core/base.html", RequestContext(request,{} ))




#    from django.http import HttpResponse
#    from django.template import loader, Context
#    def homepage(request):
#        t = loader.get_template('index.html')
#        c = Context()
#        content = t.render(c)
#        return HttpResponse(content)


def gera_menu_principal(request):
    '''
    Metodo que monta o menu principal
    '''

    lista_menu_principal = (
            ("Home","/"),
            ("Empresa","/empresa"),
            ("Fale Conosco","/fale_conosco"),
        )

    render_template = loader.get_template('core/menu_principal.html')
    contexto = Context({
        "lista_menu_principal": lista_menu_principal
    })
    content = render_template.render(contexto)

    return content

def gera_menu_categorias(request):
    '''
    Mótodo que gera as categorias
    '''
    
    #
    # TODO Carregar as categorias do banco 
    #
    
    lista_categorias = (
        (""


#    teste = mark_safe(render_to_response("core/menu_principal.html", {
#
#            "lista_menu_principal": lista_menu_principal,
#        }))


#    return render_to_response("core/menu_principal.html", {
#        "lista_menu_principal": lista_menu_principal,
#    })

