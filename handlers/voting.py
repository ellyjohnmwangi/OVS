# Import necessary libraries (e.g., for database connectivity)
import mysql.connector
from mysql.connector import connect

class VoteHandler:
    def __init__(self, request_handler):
        self.request_handler = request_handler
        self.db = DBConnector(
            host="localhost",
            user="root",
            password="",
            database="ovs_student"
        )
        self.auth = Authenticator(self.db.get_connection())

    def get_vote_delegate(self):
        # check user with that id has voted
        voted = True
        if voted:
            # server the homepage
        else:
            #serve the voting template

    def vote_delegate(self):
        # check user with that id has voted
        voted = True
        if voted:
            #return false or some jsonnindicating false
        else:
            # proceed to delegate voting

    def get_voting_counsil(self):
        # check if delegate
        # check if voted
        voted = True
        if voted:
            # return somw json data indicating false/already voted or times up
        else:
            #redirect to voting

    def vote_counsil(self):
        # check if delegate
        # check if voted
        voted = True
        if voted:
            # redirect to results page
        else:
            #redirect to voting
