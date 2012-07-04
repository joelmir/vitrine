# -*- coding:utf-8 -*-
#Autor:guerra
#Data: 02/02/12
#Ultima alteracao:

from django.utils.translation import ugettext_lazy as _
from django.db import models


STATUS_CHOICES = {
    'A': "Ativo",
    'I': "Inaivo",
}


class ItemMenu(models.Model):

    codigo_sequencia = models.ImageField(_(u"Codigo da Sequência"), help_text=_(u"Código da Sequencia a ser inserido o Item de Menu"))
    nome = models.CharField(_(u"Nome"), max_length=100)
    # Descricao que vai no texto de ajuda do Item, tilte do menu
    descricao_nome = models.CharField(_(u"Descrição do Nome"), max_length=200,
        help_text=_(u"Descricao que vai no texto de ajuda do item."))
    descricao = models.CharField(_(u"Descrição do Item"), max_length=300)
    # Item de menu pai, se for null é um item de menu principal
    item_menu_pai = models.ForeignKey('self',verbose_name=_(u"Item Pai"), blank=True, null=True, help_text=_(u"Item de Menu Pai"))
    # Data e Hora da criação do registro
    dthr = models.DateTimeField(_(u"Criado em"), auto_now_add=True)
    ultima_alteracao = models.DateTimeField(_(u"Última Alteração"), auto_now=True)
    status = models.CharField(_(u"Status"), max_length=1, choices=STATUS_CHOICES)

    class Meta:
        app_label = "Item de Menu"
        db_table = 'item_menu'
        ordering = [] # fieldes de ordenação
        verbose_name = _(u"Item de Menu") # Nome para o usuário
        verbose_name_plural = _(u"Itens de Menu")

    def __unicode__(self):
        return u"%s - %s" % (self.codigo_sequencia, self.nome)



class LinkMenu(models.Model):
    """
    Lembrar de ver sobre get_absolute_url
    """

    codigo_sequencia = models.ImageField(_(u"Codigo da Sequência"), help_text=_(u"Código da Sequencia a ser inserido o Link de Menu"))
    nome = models.CharField(_(u"Nome"), max_length=100)

    # Descricao que vai no texto de ajuda do Item, tilte do menu
    descricao_nome = models.CharField(_(u"Descrição do Nome"), max_length=200,
        help_text=_(u"Descricao que vai no texto de ajuda do item."))
    descricao = models.CharField(_(u"Descrição do Link"), max_length=300)
    # Data e Hora da criação do registro
    dthr = models.DateTimeField(_(u"Criado em"), auto_now_add=True)
    ultima_alteracao = models.DateTimeField(_(u"Última Alteração"), auto_now=True)

    item_menu = models.ForeignKey(ItemMenu, verbose_name=_(u"Item de Menu Pai"), blank=True, null=True, help_text=_(u"Item de Menu Pai do Link"))

    status = models.CharField(_(u"Status"), max_length=1, choices=STATUS_CHOICES)

    #url_name = models.CharField(_(u"Nome URL"), max_length=200, help_text = _(u"url da aplicação aplicacao_app/link_aplicacao/"))
    #dev_name = models.CharField("Caminho da Função", max_length = 200, help_text='projeto.aplicacao_app.aplicacao_views.aplicacao_funcao')

    def __unicode__(self):
        return u"%s - %s" % (self.codigo_sequencia, self.nome)

    class Meta:
        app_label = "Link de Menu"
        db_name = "link_menu"
        ordering = [] # fieldes de ordenação
        verbose_name = _(u"Link de Menu") # Nome para o usuário
        verbose_name_plural = _(u"Links de Menu")


    # SOBRESCREVENDO METODO SAVE
#   def save(self, force_insert=False, force_update=False, using=None):
#       if not self.id:
#           self.data_criacao = datetime.now()
#       else:
#           self.data_alteracao = datetime.now()
#       super(self,NomeModel).save(*args,**kwargs)