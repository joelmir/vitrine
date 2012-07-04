# -*- coding:utf-8 -*-
#Desenvolvedor: Rober Guerra
#Data: 30/09/11
#Hora: 10:44
#Ultima alteracao: 


import re
from django.conf import settings

class BrowserDetectionMiddleware(object):

    def __init__(self):

        self.data_browser = [
            {
                'subString': "CHROME",
                'identity': "CHROME",
                'versionSearch': "CHROME/"
            },
            {
                'subString': "APPLE",
                'identity': "SAFARI",
                'versionSearch': "VERSION/"
            },
            {
                'subString': "OPERA MINI",
                'identity': "OPERA MINI",
                'versionSearch': "OPERA MINI/"
            },
            {
                'subString': "OPERA",
                'identity': "OPERA",
                'versionSearch': "VERSION/"
            },
            {
                'subString': "FIREFOX",
                'identity': "FIREFOX",
                'versionSearch': "FIREFOX/"
            },
            {
                'subString': "MSIE",
                'identity': "EXPLORER",
                'versionSearch': "MSIE "
            },

            {
                'subString': "SEAMONKEY",
                'identity': "SEAMONKEY",
                'versionSearch': "SEAMONKEY/"
            },
            {
                'subString': "GECKO",
                'identity': "MOZILLA",
                'versionSearch': "RV:"
            },
            {
                'subString': "WEBKIT",
                'identity': "WEBKIT",
                'verionSearch': "CHROME/"
            },
            {
                'subString': "WEBKIT",
                'identity': "WEBKIT",
                'verionSearch': "SAFARI/"
            },
            #NÃO SUPORTADOS
            '''
            {   # For Netscape >= 9.0
                'subString': "NAVIGATOR",
                'identity': "NETSCAPE",
                'versionSearch': "NAVIGATOR/"
            },
            {   # For Netscape 7.0-9.0
                'subString': "NETSCAPE",
                'identity': "NETSCAPE",
                'versionSearch': "NETSCAPE/"
            },
            {   # For Netscape 6.x
                'subString': "NETSCAPE",
                'identity': "NETSCAPE",
                'versionSearch': "NETSCAPE6/"
            },
            {
                'subString': "KONQUEROR",
                'identity': "KONQUEROR",
                'versionSearch': "KONQUEROR/"
            },
            '''
        ]

        self.data_os = (
            'WINDOWS',
            'LINUX',
            'MAC',
            'ANDROID',
            'IPHONE',
            'UNKNOW',
        )
    def process_request(self, request):
        request.browser_name = ''
        request.browser_version = 0.0
        request.os_name = ''

        try:
            agent = request.META['HTTP_USER_AGENT'].upper()
            for os in self.data_os:
                if os in agent:
                    request.os_name = os
                    break

            for b in self.data_browser:
                if b['subString'] in agent:
                    browser_name = b['identity']
                    browser_version = ''
                    if b.has_key('versionSearch'):
                        #f = re.compile(b['versionSearch']+'([0-9\.]+)',re.M) #expressao regular antiga
                        f = re.compile(b['versionSearch']+'([0-9]+\.[0-9]+)',re.M)
                        m = f.search(agent)
                        if m:
                            browser_version = m.group(1)

                    #atribui para a requisição as variaveis da requisição
                    request.browser_name = browser_name
                    request.browser_version = float(browser_version)
                    break;

            #CASO NÃO TENHA ENCONTRADO O NAVEGADOR OU SISTEMA OPERACIONAL
            if not request.os_name or not request.browser_name:
                user_agent = ''
                host_name = ''
                if 'HTTP_USER_AGENT' in request.META:
                    user_agent = str(request.META['HTTP_USER_AGENT'])
                if 'HOST_NAME' in request.META:
                    host_name = str(reques.META['HOST_NAME'])
                menssagem = """\
                Erro: Navegador ou Sistema Operacional desconhecido
                NOME_CLIENTE: %s
                PREFIXO_URL: %s
                HOST_NAME: %s
                HTTP_USER_AGENT: %s
                """ % (settings.NOME_CLIENTE, settings.PREFIXO_URL,host_name, user_agent)
                enviaEmailErro(assunto="Erro: Navegador ou OS desconhecido",menssagem=menssagem)
        #EM CASO DE ERRO ENVIA EMAIL ATRAVÉS DE UMA THREAD
        except:

            user_agent = ''
            host_name = ''
            if 'HTTP_USER_AGENT' in request.META:
                user_agent = str(request.META['HTTP_USER_AGENT'])
            if 'HOST_NAME' in request.META:
                host_name = str(reques.META['HOST_NAME'])
            menssagem = """\
            Erro: Erro ao verificar navegador ou OS
            NOME_CLIENTE: %s
            PREFIXO_URL: %s
            HOST_NAME: %s
            HTTP_USER_AGENT: %s
            """ % (NOME_CLIENTE, PREFIXO_URL, host_name, user_agent)
            enviaEmailErro(assunto="Erro: Erro ao verificar navegador ou OS",menssagem=menssagem)
        
    def process_view(self, request, view_func, view_args, view_kwargs):
        pass

    def process_response(self, request, response):
        return response

    def process_exception(self, request, exception):
        pass
