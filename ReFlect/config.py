import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgres://ulovmdcpclxghy:4871be934d91d47d4ad79eb02d72cc1485342a286734b966015ec746f1be3370@ec2-107-22-234-103.compute-1.amazonaws.com:5432/dbu7kqsbb0nqhn"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    SECRET_KEY = "ReFlectApp"