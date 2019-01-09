
# @class_declaration clientes_inactivos #
from YBLEGACY.constantes import *


class clientes_inactivos(flfactppal):

    def clientes_inactivos_queryGrid_clientesInactivos(self, model, filters):
        fecha = ''
        if(filters):
            print(filters['[d_fecha]'])
            fecha = "'" + filters['[d_fecha]'] + "'"
        if not fecha or fecha == "''":
            fecha = 'CURRENT_DATE'
        query = {}
        query["tablesList"] = ("clientes,pedidoscli")
        query["select"] = ("c.codcliente, c.nombre, c.email, c.telefono1, MAX(antes.fecha) as fecha, d.direccion")
        query["from"] = ("clientes AS c INNER JOIN pedidoscli AS antes ON c.codcliente = antes.codcliente AND antes.fecha < " + fecha + " LEFT OUTER JOIN pedidoscli AS despues ON c.codcliente = despues.codcliente AND despues.fecha >= " + fecha + " INNER JOIN dirclientes d ON c.codcliente = d.codcliente and d.domfacturacion is true")
        query["where"] = "antes.codcliente IS NOT NULL and despues.codcliente IS NULL"
        query["groupby"] = " c.codcliente, c.nombre, c.email, c.telefono1, d.direccion"
        query["orderby"] = "c.nombre DESC"
        return query

    def clientes_inactivos_queryGrid_ventasClientes(self, model, filters):
        print("-----------------------------------cliente: " + model.codcliente)
        query = {}
        query["tablesList"] = ("pedidoscli,lineaspedidoscli")
        query["select"] = ("lineaspedidoscli.referencia, lineaspedidoscli.descripcion, lineaspedidoscli.cantidad, lineaspedidoscli.pvpunitario, lineaspedidoscli.dtopor, pedidoscli.fecha, lineaspedidoscli.pvptotal, pedidoscli.codigo")
        query["from"] = ("pedidoscli INNER JOIN lineaspedidoscli ON pedidoscli.idpedido = lineaspedidoscli.idpedido")
        query["where"] = ("pedidoscli.codcliente = '" + str(model.codcliente) + "'")
        query["orderby"] = "pedidoscli.fecha DESC"
        return query

    def clientes_inactivos_dameDetalleVentasPorCliente(self, model):
        print('codcliente ', str(model))
        url = '/principal/clientes/' + str(model.codcliente) + '/ventasclientes'
        return url

    def clientes_inactivos_dameEmails(self, model, oParam):
        print('Cogiendo emails')
        emails = ''
        aChecked = oParam['selecteds'].split(u",")
        response = {}
        response['status'] = 1
        if not aChecked[0]:
            response['msg'] = "Error: Selecciona un elemento"
            return response
        for i in range(len(aChecked)):
            print(aChecked)
            email = qsatype.FLUtil.sqlSelect(u"clientes", u"email", ustr(u"codcliente = '", aChecked[i], u"'"))
            print(email)
            if email and email != '':
                emails = emails + email + ';'
        response["status"] = 2
        response["confirm"] = emails
        response["close"] = True
        return response

    def clientes_inactivos_queryGrid_clientesNuevos(self, model, filters):
        fecha = ''
        if(filters):
            print(filters['[d_fecha]'])
            fecha = "'" + filters['[d_fecha]'] + "'"
        if not fecha or fecha == "''":
            fecha = 'CURRENT_DATE'
        query = {}
        query["tablesList"] = ("clientes,pedidoscli")
        query["select"] = ("c.codcliente, c.nombre, c.email, c.telefono1, MIN(antes.fecha) as fecha, d.direccion")
        query["from"] = ("clientes AS c INNER JOIN pedidoscli AS antes ON c.codcliente = antes.codcliente AND antes.fecha >= " + fecha + " LEFT OUTER JOIN pedidoscli AS despues ON c.codcliente = despues.codcliente AND despues.fecha < " + fecha + " INNER JOIN dirclientes d ON c.codcliente = d.codcliente and d.domfacturacion is true")
        query["where"] = " antes.codcliente IS NOT NULL and despues.codcliente IS NULL"
        query["groupby"] = " c.codcliente, c.nombre, c.email, c.telefono1, d.direccion"
        query["orderby"] = "c.nombre DESC"
        return query

    def __init__(self, context=None):
        super().__init__(context)

    def queryGrid_clientesInactivos(self, model, filters):
        return self.ctx.clientes_inactivos_queryGrid_clientesInactivos(model, filters)

    def queryGrid_ventasClientes(self, model, filters):
        return self.ctx.clientes_inactivos_queryGrid_ventasClientes(model, filters)

    def dameDetalleVentasPorCliente(self, model):
        return self.ctx.clientes_inactivos_dameDetalleVentasPorCliente(model)

    def dameEmails(self, model, oParam):
        return self.ctx.clientes_inactivos_dameEmails(model, oParam)

    def queryGrid_clientesNuevos(self, model, filters):
        return self.ctx.clientes_inactivos_queryGrid_clientesNuevos(model, filters)

