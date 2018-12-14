
# @class_declaration clientes_inactivos_clientes #
class clientes_inactivos_clientes(flfactppal_clientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    @helpers.decoradores.accion(aqparam=["oParam"])
    def queryGrid_clientesInactivos(model, filters):
        return form.iface.queryGrid_clientesInactivos(model, filters)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def queryGrid_ventasClientes(model):
        return form.iface.queryGrid_ventasClientes(model)

    @helpers.decoradores.accion()
    def dameDetalleVentasPorCliente(self):
        return form.iface.dameDetalleVentasPorCliente(self)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def dameEmails(self, oParam):
        return form.iface.dameEmails(self, oParam)

