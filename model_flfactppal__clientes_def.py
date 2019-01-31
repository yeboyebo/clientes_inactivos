
# @class_declaration clientes_inactivos #
from YBLEGACY.constantes import *
from YBUTILS.viewREST import cacheController

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

    def clientes_inactivos_queryGrid_comparativas(self, model, filters):
        trimestre = ''
        anio1 = ''
        anio2 = ''
        anio1f = ''
        anio2f = ''
        where = "1 = 1"
        if(filters):
            if filters['[trimestre]'] and filters['[trimestre]'] != "":
                # trimestre = filters['[trimestre]']
                print(filters['[trimestre]'])
                cacheController.setSessionVariable(ustr(u"trimestre_", qsatype.FLUtil.nameUser()), filters['[trimestre]'])
                trimestre = "'" + cacheController.getSessionVariable(ustr(u"trimestre_", qsatype.FLUtil.nameUser())) + "'"
                print(trimestre)
            if filters['[anio_1]'] and filters['[anio_1]'] != "":
                print("anio1-1: " + filters['[anio_1]'])
                if trimestre == "''":
                    print("anio1: " + filters['[anio_1]'])
                    anio1 = "'" + filters['[anio_1]'] + "-01-01'"
                    anio1f = "'" + filters['[anio_1]'] + "-12-31'"
                elif trimestre == "'T1'":
                    anio1 = "'" + filters['[anio_1]'] + "-01-01'"
                    anio1f = "'" + filters['[anio_1]'] + "-03-31'"
                elif trimestre == "'T2'":
                    anio1 = "'" + filters['[anio_1]'] + "-04-01'"
                    anio1f = "'" + filters['[anio_1]'] + "-06-30'"
                elif trimestre == "'T3'":
                    anio1 = "'" + filters['[anio_1]'] + "-07-01'"
                    anio1f = "'" + filters['[anio_1]'] + "-09-30'"
                elif trimestre == "'T4'":
                    anio1 = "'" + filters['[anio_1]'] + "-10-01'"
                    anio1f = "'" + filters['[anio_1]'] + "-12-31'"
                cacheController.setSessionVariable(ustr(u"anio1_", qsatype.FLUtil.nameUser()), anio1)
                cacheController.setSessionVariable(ustr(u"anio1f_", qsatype.FLUtil.nameUser()), anio1f)
            if filters['[anio_2]'] and filters['[anio_2]'] != "":
                print("anio2-2: " + filters['[anio_2]'])
                if trimestre == "''":
                    print("anio2: " + filters['[anio_2]'])
                    anio2 = "'" + filters['[anio_2]'] + "-01-01'"
                    anio2f = "'" + filters['[anio_2]'] + "-12-31'"
                elif trimestre == "'T1'":
                    anio2 = "'" + filters['[anio_2]'] + "-01-01'"
                    anio2f = "'" + filters['[anio_2]'] + "-03-31'"
                elif trimestre == "'T2'":
                    anio2 = "'" + filters['[anio_2]'] + "-04-01'"
                    anio2f = "'" + filters['[anio_2]'] + "-06-30'"
                elif trimestre == "'T3'":
                    anio2 = "'" + filters['[anio_2]'] + "-07-01'"
                    anio2f = "'" + filters['[anio_2]'] + "-09-30'"
                elif trimestre == "'T4'":
                    anio2 = "'" + filters['[anio_2]'] + "-10-01'"
                    anio2f = "'" + filters['[anio_2]'] + "-12-31'"
                cacheController.setSessionVariable(ustr(u"anio2_", qsatype.FLUtil.nameUser()), anio2)
                cacheController.setSessionVariable(ustr(u"anio2f_", qsatype.FLUtil.nameUser()), anio2f)
            print(anio1f)
            print(anio2f)
        if not anio1 or anio1 == "''":
            anio1 = "'2100-01-01'"
            anio1f = "'2100-01-01'"
            where = "1 = 2"
        if not anio2 or anio2 == "''":
            anio2 = "'2100-01-01'"
            anio2f = "'2100-01-01'"
            where = "1 = 2"
        print('Seguimos con la query')
        query = {}
        # Ya est�, a AQNext no le hab�a gustado que pusieses dos "as" en el mismo campo, porque no pod�a sacar bien el alias y eso. He hecho el cast con "::numeric" y he cambiado el nombre del campo en los json (estaba con c.codcliente) y ya va. Comprueba que no me haya cargado nada.
        # query["tablesList"] = ("clientes,pedidoscli")
        # query["select"] = ("clientes.codcliente, clientes.nombre, clientes.email, clientes.telefono1, COALESCE(SUM(f.total),0) as total1, dirclientes.direccion, COALESCE(SUM(f2.total),0) as total2, CASE WHEN COALESCE(SUM(f.total),0) = 0 THEN (CASE WHEN COALESCE(SUM(f2.total),0) = 0 THEN 0 ELSE 100 END) ELSE round(((((COALESCE(SUM(f2.total),0) - COALESCE(SUM(f.total),0)) * 100)) / COALESCE(SUM(f.total),0))::numeric,2) END as variacion")
        # query["from"] = ("clientes LEFT OUTER JOIN pedidoscli f ON clientes.codcliente = f.codcliente AND f.fecha BETWEEN " + anio1 + " AND " + anio1f + " LEFT OUTER JOIN pedidoscli f2 ON clientes.codcliente = f2.codcliente AND f2.fecha BETWEEN " + anio2 + " AND " + anio2f + " INNER JOIN dirclientes ON clientes.codcliente = dirclientes.codcliente and dirclientes.domfacturacion is true")
        # query["where"] = where
        # query["groupby"] = " clientes.codcliente, clientes.nombre, clientes.email, clientes.telefono1, dirclientes.direccion"
        # query["orderby"] = "clientes.nombre DESC"

        query["tablesList"] = ("clientes,dirclientes")
        query["select"] = ("clientes.codcliente, clientes.nombre, clientes.email, clientes.telefono1, dirclientes.direccion, (SELECT COALESCE(SUM(pedidoscli.total),0) from pedidoscli  where pedidoscli.codcliente = clientes.codcliente and pedidoscli.fecha BETWEEN " + anio1 + " AND " + anio1f + ") AS total1, (SELECT COALESCE(SUM(pedidoscli.total),0) from pedidoscli  where pedidoscli.codcliente = clientes.codcliente and pedidoscli.fecha BETWEEN " + anio2 + " AND " + anio2f + ") AS total2, CASE WHEN (SELECT COALESCE(SUM(pedidoscli.total),0) from pedidoscli  where pedidoscli.codcliente = clientes.codcliente and pedidoscli.fecha BETWEEN " + anio1 + " AND " + anio1f + ") = 0 THEN (CASE WHEN (SELECT COALESCE(SUM(pedidoscli.total),0) from pedidoscli  where pedidoscli.codcliente = clientes.codcliente and pedidoscli.fecha BETWEEN " + anio2 + " AND " + anio2f + ") = 0 THEN 0 ELSE 100 END) ELSE round((((((SELECT COALESCE(SUM(pedidoscli.total),0) from pedidoscli  where pedidoscli.codcliente = clientes.codcliente and pedidoscli.fecha BETWEEN " + anio2 + " AND " + anio2f + ") - (SELECT COALESCE(SUM(pedidoscli.total),0) from pedidoscli  where pedidoscli.codcliente = clientes.codcliente and pedidoscli.fecha BETWEEN " + anio1 + " AND " + anio1f + ")) * 100)) / (SELECT COALESCE(SUM(pedidoscli.total),0) from pedidoscli  where pedidoscli.codcliente = clientes.codcliente and pedidoscli.fecha BETWEEN " + anio1 + " AND " + anio1f + "))::numeric,2) END AS variacion")
        query["from"] = ("clientes INNER JOIN dirclientes ON clientes.codcliente = dirclientes.codcliente and dirclientes.domfacturacion is true")
        query["where"] = where
        query["groupby"] = " clientes.codcliente, clientes.nombre, clientes.email, clientes.telefono1, dirclientes.direccion"
        query["orderby"] = "clientes.nombre DESC"
        return query

    def clientes_inactivos_getForeignFields(self, model, template=None):
        fields = []
        if template == "comparativas":
            fields = [{'verbose_name': 'rowColor', 'func': 'field_colorRow'}]
        return fields

    def clientes_inactivos_field_colorRow(self, model):
        if model["total2"] > model["total1"]:
            return "cSuccess"
        else:
            return "cDanger"

    def clientes_inactivos_dameDetalleComparativasArticulo(self, model):
        url = '/principal/clientes/' + str(model.codcliente) + '/comparativasarticulo'
        return url

    def clientes_inactivos_queryGrid_comparativasArticulo(self, model, filters):
        print("-----------------------------------cliente: " + model.codcliente)
        anio1 = cacheController.getSessionVariable(ustr(u"anio1_", qsatype.FLUtil.nameUser()))
        anio1f = cacheController.getSessionVariable(ustr(u"anio1f_", qsatype.FLUtil.nameUser()))
        anio2 = cacheController.getSessionVariable(ustr(u"anio2_", qsatype.FLUtil.nameUser()))
        anio2f = cacheController.getSessionVariable(ustr(u"anio2f_", qsatype.FLUtil.nameUser()))
        query = {}
        query["tablesList"] = ("articulos,pedidoscli,lineaspedidoscli")
        query["select"] = ("articulos.referencia, articulos.descripcion, (SELECT COALESCE(SUM(lineaspedidoscli.cantidad),0) from lineaspedidoscli INNER JOIN pedidoscli ON lineaspedidoscli.idpedido = pedidoscli.idpedido WHERE pedidoscli.fecha BETWEEN " + anio1 + " AND " + anio1f + " AND pedidoscli.codcliente = '" + str(model.codcliente) + "' AND lineaspedidoscli.referencia = articulos.referencia) AS cant1, (SELECT COALESCE(SUM(lineaspedidoscli.cantidad),0) from lineaspedidoscli INNER JOIN pedidoscli ON lineaspedidoscli.idpedido = pedidoscli.idpedido WHERE pedidoscli.fecha BETWEEN " + anio2 + " AND " + anio2f + " AND pedidoscli.codcliente = '" + str(model.codcliente) + "' AND lineaspedidoscli.referencia = articulos.referencia) as cant2")
        query["from"] = ("articulos")
        query["where"] = ("(SELECT COALESCE(SUM(lineaspedidoscli.cantidad),0) from lineaspedidoscli INNER JOIN pedidoscli ON lineaspedidoscli.idpedido = pedidoscli.idpedido WHERE pedidoscli.fecha BETWEEN " + anio1 + " AND " + anio1f + " AND pedidoscli.codcliente = '" + str(model.codcliente) + "' AND lineaspedidoscli.referencia = articulos.referencia) <> 0 or (SELECT COALESCE(SUM(lineaspedidoscli.cantidad),0) from lineaspedidoscli INNER JOIN pedidoscli ON lineaspedidoscli.idpedido = pedidoscli.idpedido WHERE pedidoscli.fecha BETWEEN " + anio2 + " AND " + anio2f + " AND pedidoscli.codcliente = '" + str(model.codcliente) + "' AND lineaspedidoscli.referencia = articulos.referencia) <> 0")
        query["groupby"] = " articulos.referencia, articulos.descripcion"
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

    def queryGrid_comparativas(self, model, filters):
        return self.ctx.clientes_inactivos_queryGrid_comparativas(model, filters)

    def getForeignFields(self, model, template=None):
        return self.ctx.clientes_inactivos_getForeignFields(model, template)

    def field_colorRow(self, model):
        return self.ctx.clientes_inactivos_field_colorRow(model)

    def dameDetalleComparativasArticulo(self, model):
        return self.ctx.clientes_inactivos_dameDetalleComparativasArticulo(model)

    def queryGrid_comparativasArticulo(self, model, filters):
        return self.ctx.clientes_inactivos_queryGrid_comparativasArticulo(model, filters)

