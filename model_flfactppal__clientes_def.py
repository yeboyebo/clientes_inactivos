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

    def clientes_inactivos_queryGrid_clientesInactivos(self, model):
        query = {}
        query["tablesList"] = ("clientes,pedidoscli")
        query["select"] = ("c.codcliente, c.nombre, c.email, c.telefono1, MAX(antes.fecha) as fecha, d.direccion")
        query["from"] = ("clientes AS c INNER JOIN pedidoscli AS antes ON c.codcliente = antes.codcliente AND antes.fecha < CURRENT_DATE LEFT OUTER JOIN pedidoscli AS despues ON c.codcliente = despues.codcliente AND despues.fecha >= CURRENT_DATE INNER JOIN dirclientes d ON c.codcliente = d.codcliente and d.domfacturacion is true")
        query["where"] = "antes.codcliente IS NOT NULL and despues.codcliente IS NULL"
        query["groupby"] = " c.codcliente, c.nombre, c.email, c.telefono1, d.direccion"
        query["orderby"] = "c.nombre DESC"
        return query

    def clientes_inactivos_queryGrid_ventasClientes(self, model):
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
        print('emails: ' + emails)
        return True

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

    def queryGrid_clientesInactivos(self, model):
        return self.ctx.clientes_inactivos_queryGrid_clientesInactivos(model)

    def queryGrid_ventasClientes(self, model):
        return self.ctx.clientes_inactivos_queryGrid_ventasClientes(model)

    def dameDetalleVentasPorCliente(self, model):
        return self.ctx.clientes_inactivos_dameDetalleVentasPorCliente(model)

    def dameEmails(self, model, oParam):
        return self.ctx.clientes_inactivos_dameEmails(model, oParam)


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
