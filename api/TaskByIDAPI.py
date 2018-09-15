from flask_restful import Resource
import logging as logger

class TaskByID(Resource):

    def post(self,taskId):
        logger.debug("Inside the post method of TaskById")
        return {"message" : "Inside post method of TaskByID. TaskId : {}".format(taskId)},200


    def get(self,taskId):
        logger.debug("Inisde the get method of TaskById. TaskID = {}".format(taskId))
        return {"message" : "Inside get method of TaskByID. TaskByID = {}".format(taskId)},200


    def put(self,taskId):
        logger.debug("Inisde the put method of TaskByID. TaskID = {}".format(taskId))
        return {"message" : "Inside put method of TaskById. TaskID = {}".format(taskId)},200


    def delete(self,taskId):
        logger.debug("Inisde the delete method of TaskByID. TaskID = {}".format(taskId))
        return {"message" : "Inside delete method"},200






