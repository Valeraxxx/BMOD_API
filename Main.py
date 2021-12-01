from flask import Flask

from flask_restful import Resource, Api, reqparse

##Authentication for the API will be added soon.
##API Is hosted at: "api.bmodd.ga/"
b = Flask(__name__)
c = Api(b)

class Reg(Resource):

  def get(self):
    ##Root server folder.
    return "Resource found"

    pass


class Hooks(Resource):
  ##Hook DataSet as yet to be created.
  def get(self):
    ##TODO
    return "WOwooooo hooks endpoint works!"

  pass

class Convert(Resource):
  def get(self):
    ##TODO
    return "THE CONVERT ENDPOINT WORKS!!!!"

  pass

class PackageFetch(Resource):
  def get(self):
    ##TODO
    return "Nice"

    pass




c.add_resource(Convert, "/convert")

c.add_resource(Hooks, '/hooks')

c.add_resource(PackageFetch, '/pkg')

c.add_resource(Reg, '/')


if __name__ == '__main__':
  b.run()