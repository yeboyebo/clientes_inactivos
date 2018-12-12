# @class_declaration interna_co_cuentas #
import importlib

from YBUTILS.viewREST import helpers

from models.flcontppal import models as modelos


class interna_co_cuentas(modelos.mtd_co_cuentas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration clientes_inactivos_co_cuentas #
class clientes_inactivos_co_cuentas(interna_co_cuentas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def initValidation(name, data=None):
        return form.iface.initValidation(name, data)

    def iniciaValoresLabel(self, template=None, cursor=None, data=None):
        return form.iface.iniciaValoresLabel(self, template, cursor)

    def bChLabel(fN=None, cursor=None):
        return form.iface.bChLabel(fN, cursor)

    def getFilters(self, name, template=None):
        return form.iface.getFilters(self, name, template)

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def getDesc():
        return form.iface.getDesc()


# @class_declaration co_cuentas #
class co_cuentas(clientes_inactivos_co_cuentas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


definitions = importlib.import_module("models.flcontppal.co_cuentas_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
