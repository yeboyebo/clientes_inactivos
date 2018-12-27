# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration clientes_inactivos #
from YBLEGACY.constantes import *


class clientes_inactivos(interna):

    def clientes_inactivos_getDesc(self):
        return None

    def __init__(self, context=None):
        super().__init__(context)

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
