import random
import json
import string
import cherrypy


class Calculator():

    def __init__(self):
        self.op1 = []
        self.op2 = []
        self.result = 0
        self.instance = {'operation': [], 'operand1': [], 'operand2': [], 'result': []}

    def add(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        self.result = op1+op2

    def sub(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        self.result = op1-op2

    def mul(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        self.result = op1*op2

    def div(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        try:
            self.result = op1/op2
        except ZeroDivisionError:
            print("Error per zero division\n")


class add(Calculator):
    exposed = True

    def GET(self, *uri, **params):
        op = Calculator()
        op.add(params['op1'], params['op2'])
        json_data = json.dumps(op.istance)
        return json_data


class sub(Calculator):
    exposed = True

    def GET(self, *uri, **params):
        op = Calculator()
        op.sub(params['op1'], params['op2'])
        json_data = json.dumps(op.istance)
        return json_data


class mul(Calculator):
    exposed = True

    def GET(self, *uri, **params):
        op = Calculator()
        op.mul(params['op1'], params['op2'])
        json_data = json.dumps(op.istance)
        return json_data


class div(Calculator):
    exposed = True

    def GET(self, *uri, **params):
        op = Calculator()
        op.div(params['op1'], params['op2'])
        json_data = json.dumps(op.istance)
        return json_data


if __name__ == '__main__':

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }

    cherrypy.tree.mount(add(), '/add', conf)
    cherrypy.tree.mount(sub(), '/sub', conf)
    cherrypy.tree.mount(mul(), '/mul', conf)
    cherrypy.tree.mount(div(), '/div', conf)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()
