
# @class_declaration clientes_inactivos_clientes #
class clientes_inactivos_clientes(flfactppal_clientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    @helpers.decoradores.accion(aqparam=["oParam"])
    def queryGrid_clientesInactivos(model, filters):
        return form.iface.queryGrid_clientesInactivos(model, filters)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def queryGrid_ventasClientes(model, filters):
        return form.iface.queryGrid_ventasClientes(model, filters)

    @helpers.decoradores.accion()
    def dameDetalleVentasPorCliente(self):
        return form.iface.dameDetalleVentasPorCliente(self)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def dameEmails(self, oParam):
        return form.iface.dameEmails(self, oParam)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def queryGrid_clientesNuevos(model, filters):
        return form.iface.queryGrid_clientesNuevos(model, filters)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def queryGrid_comparativas(model, filters):
        return form.iface.queryGrid_comparativas(model, filters)

    def field_colorRow(self):
        return form.iface.field_colorRow(self)

    @helpers.decoradores.accion()
    def dameDetalleComparativasArticulo(self):
        return form.iface.dameDetalleComparativasArticulo(self)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def queryGrid_comparativasArticulo(model, filters):
        return form.iface.queryGrid_comparativasArticulo(model, filters)

