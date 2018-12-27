# @class_declaration interna_clientesinactivos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_clientesinactivos(modelos.mtd_clientesinactivos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration clientes_inactivos_clientesinactivos #
class clientes_inactivos_clientesinactivos(interna_clientesinactivos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration clientesinactivos #
class clientesinactivos(clientes_inactivos_clientesinactivos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.clientesinactivos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
