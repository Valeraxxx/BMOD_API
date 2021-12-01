from flask import Flask

from flask_restful import Resource, Api, reqparse


##Domain Needed 
b = Flask(__name__)
c = Api(b)

class Hooks(Resource):
  ##Hook DataSet as yet to be created.
  def get(self):
    ##TODO
    print("")

  pass

class Convert(Resource):
  def get(self):
    ##TODO
    print("")

  pass

class PackageFetch(Resource):
  def get(self):
    ##TODO
    print("")


c.add_resource(Convert, "/convert")

c.add_resource(Hooks, '/hooks')

c.add_resource(PackageFetch, '/pkg')


if __name__ == '__main__':
  b.run()