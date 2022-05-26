from tools.FirebaseTool import FirebaseTool
from tools.JsonUtils import JsonUtils
import json

configFile = "resources/config.json"

class BotaPraRodarETL:
    
    def __init__(self,ft = FirebaseTool(), jsonUtils = JsonUtils() ):

        self.ft = ft
        self.jsonUtils = jsonUtils
        self.config = self.jsonUtils.readJson(configFile)

        if not self.config:
            raise Exception("File config.json file is not defined")
        if not self.config.get("OriginDatabaseURL"):
            raise Exception("OriginDatabaseURL is not defined")
        if not self.config.get("OriginCertificateJson"):
            raise Exception("OriginCertificateJson is not defined")
        if not self.config.get("OriginJsonFile"):
            raise Exception("OriginJsonFile is not defined")

        self.ft.connection(self.config["OriginDatabaseURL"], self.config["OriginCertificateJson"])

    def processing(self):

        self.admins()
        self.users()
        self.communities()
        self.bikes()
    
        #self.jsonUtils.printPretty(self.ft.get())
        print("ALL REGISTERS SAVED IN FIREBASE =)")

    def admins(self):
        print("Saving admins..")
        admin = self.jsonUtils.get(self.config["OriginJsonFile"], "admins") 
        self.ft.set(admin, "/admins")

    def users(self):
        print("Saving users..")
        users = self.jsonUtils.get(self.config["OriginJsonFile"], "users") 
        for key, val in users.items():
                         
            del users[key]["docPicture"]
            del users[key]["docPictureBack"]
            del users[key]["docType"]
            del users[key]["residenceProofPicture"]

        self.ft.set(users, "/users")

    def communities(self):
        print("Saving communities..")
        communities = self.jsonUtils.get(self.config["OriginJsonFile"], "communities") 

        for key, val in communities.items():
            communities[key]["community_admin_id"] = ""

        self.ft.set(communities, "/communities")  

    def bikes(self):
        print("Saving bikes..")
        bikes = self.jsonUtils.get(self.config["OriginJsonFile"], "bikes") 
        self.ft.delete("/travels") #Remove duplication, if you run more than one time

        travels = {}
        for key, val in bikes.items():
            devolutions = None
            withdraws = None

            if bikes[key].get("devolutions") != None:
                devolutions = bikes[key]["devolutions"]
            if bikes[key].get("withdraws") != None:
                withdraws = bikes[key]["withdraws"]
            
            travels.update(self.travels(bikes[key], devolutions, withdraws))

            if bikes[key].get("devolutions") != None:
                del bikes[key]["devolutions"]
            if bikes[key].get("withdraws") != None:
                del bikes[key]["withdraws"]

        self.ft.set(bikes, "/bikes")
        self.ft.set(travels, "/travels")
    
    def travels(self, bike, devolutions, withdraws):
        print("Waiting saving travels..")
        travels = {}
        for key, val in withdraws.items():
            uuid = self.ft.getUUID("/travels")

            devolution = self.jsonUtils.getItemByAttribute(devolutions, "withdrawId", key)
            
            #devolution
            finished_at = None
            destination = None
            reason = None
            problemsDuringRiding = None
            giveRide = None

            if devolution and devolution[1]:
                finished_at = devolution[1].get("date")
                if devolution[1].get("quiz"):
                    destination = devolution[1]["quiz"].get("destination")
                    reason = devolution[1]["quiz"].get("reason")
                    problemsDuringRiding = devolution[1]["quiz"].get("problemsDuringRiding")
                    giveRide = devolution[1]["quiz"].get("giveRide")

            #withdraw
            userId = None
            communityId = None
            timeOnWayOpenQuestion = None
            accessOtherTransport = None
            accessOtherTransportOpenQuestion = None
            alreadyAccidentVictim = None
            motivationOpenQuestion = None
            problemsOnWayOpenQuestion = None

            if val.get("user") and val["user"].get("userQuiz"):

                userId = val["user"].get("id")
                communityId = val["user"].get("communityId")

                userQuiz = val["user"]["userQuiz"]
                timeOnWayOpenQuestion = userQuiz.get("timeOnWayOpenQuestion")
                accessOtherTransport = userQuiz.get("accessOtherTransport")
                accessOtherTransportOpenQuestion = userQuiz.get("accessOtherTransportOpenQuestion")
                alreadyAccidentVictim = userQuiz.get("alreadyAccidentVictim")
                motivationOpenQuestion = userQuiz.get("motivationOpenQuestion")
                problemsOnWayOpenQuestion = userQuiz.get("problemsOnWayOpenQuestion")

            travel = {
                    "id": uuid,
                    "user_id": userId, # se nao houver o dado, o que fazer?
                    "community_id": communityId,
                    "bike_id": bike["id"],
                    #"community_admin_id": "pelo id da comunidade, olhar communities e pegar o org_email??",
                    "initiated_at": val.get("date"),
                    "finished_at": finished_at,
                    "on_going": devolution == None,
                    "destination": destination,
                    "reason": reason,
                    "problems_during_riding": problemsDuringRiding,
                    "give_ride": giveRide,
                    "path": "travels",
                    "time_on_way_open_question": timeOnWayOpenQuestion,
                    "access_other_transport": accessOtherTransport,
                    "access_other_transport_open_question": accessOtherTransportOpenQuestion,
                    "already_accident_victim": alreadyAccidentVictim,
                    "motivation_open_question": motivationOpenQuestion,
                    "problems_on_way_open_question": problemsOnWayOpenQuestion
            }
            
            travels[uuid] = travel
        return travels

if __name__ == "__main__":
    etl = BotaPraRodarETL()
    etl.processing()
