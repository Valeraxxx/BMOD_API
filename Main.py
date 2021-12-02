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
    return "Note: No Redirection needed!"

  pass

class Convert(Resource):
  def get(self):
    ##TODO
    return "Note: This is not a real endpoint!!!!!! This endpoint is to be accessed and redirected to the conversion server. Reason? because I don't feel like sending the request from the client :)" ## "https://conversion.bmodd.ga": No use in connecting to this domain as it'll return a 401, Use the Client! 

  pass

class PackageFetch(Resource):
  def get(self):
    ##TODO
    return "Note: This endpoint redirects to a package specified in the get request of the client. If the package isn't correct the endpoint will return a 404."

    pass




c.add_resource(Convert, "/convert")

c.add_resource(Hooks, '/hooks')

c.add_resource(PackageFetch, '/pkg')

c.add_resource(Reg, '/')


if __name__ == '__main__':
  b.run()