# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration clientes_inactivos #
from YBLEGACY.constantes import *


class clientes_inactivos(interna):

    def clientes_inactivos_initValidation(self, name, data=None):
        response = True
        return response

    def clientes_inactivos_iniciaValoresLabel(self, model=None, template=None, cursor=None):
        labels = {}
        return labels

    def clientes_inactivos_bChLabel(self, fN=None, cursor=None):
        labels = {}
        return labels

    def clientes_inactivos_getFilters(self, model, name, template=None):
        filters = []
        return filters

    def clientes_inactivos_getForeignFields(self, model, template=None):
        fields = []
        return fields

    def clientes_inactivos_getDesc(self):
        desc = None
        return desc

    def __init__(self, context=None):
        super(clientes_inactivos, self).__init__(context)

    def initValidation(self, name, data=None):
        return self.ctx.clientes_inactivos_initValidation(name, data)

    def iniciaValoresLabel(self, model=None, template=None, cursor=None):
        return self.ctx.clientes_inactivos_iniciaValoresLabel(model, template, cursor)

    def bChLabel(self, fN=None, cursor=None):
        return self.ctx.clientes_inactivos_bChLabel(fN, cursor)

    def getFilters(self, model, name, template=None):
        return self.ctx.clientes_inactivos_getFilters(model, name, template)

    def getForeignFields(self, model, template=None):
        return self.ctx.clientes_inactivos_getForeignFields(model, template)

    def getDesc(self):
        return self.ctx.clientes_inactivos_getDesc()


# @class_declaration head #
class head(clientes_inactivos):

    def __init__(self, context=None):
        super(head, self).__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super(ifaceCtx, self).__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
