import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'BotaPraRodarETL'))) # Referenciar classe fora do pacote

import unittest, json
from parameterized import parameterized
from unittest.mock import MagicMock
from BotaPraRodarETL import BotaPraRodarETL

class BotaPraRodarETL_test(unittest.TestCase):
   
    config = {"OriginDatabaseURL":"test", "OriginCertificateJson":"test", "OriginJsonFile":"test"}

    def getBotaPraRodarETL(self, configFile, firebaseJson = {}):
        self.ft = MagicMock()
        self.ft.connection.return_value = True
        
        self.jsonUtils = MagicMock()
        self.jsonUtils.readJson.return_value = configFile
        self.jsonUtils.get.return_value = firebaseJson

        self.bt = BotaPraRodarETL(self.ft, self.jsonUtils)

    @parameterized.expand([
        ({"OriginDatabaseURL":"test", "OriginCertificateJson":"test", "OriginJsonFile":"test"},)
    ])
    def test_BotaPraRodarETL_WhenCorrectDatabaseURLAndCertificate_ShouldExecuteOneTime(self,config):

        self.getBotaPraRodarETL(config, {})
        self.ft.connection.assert_called_once()

    @parameterized.expand([
        ({"OriginDatabaseURL":"", "OriginCertificateJson":"test", "OriginJsonFile":"test"},),
        ({"OriginDatabaseURL":"test", "OriginCertificateJson":"", "OriginJsonFile":"test"},),
        ({"OriginDatabaseURL":"test", "OriginCertificateJson":"test", "OriginJsonFile":""},),
        ({"OriginCertificateJson":"test", "OriginJsonFile":"test"},),
        ({"OriginDatabaseURL":"test", "OriginJsonFile":"test"},),
        ({"OriginDatabaseURL":"test", "OriginCertificateJson":"test"},),
        (None,)
    ])
    def test_BotaPraRodarETL_WhenInvalidDatabaseURLAndCertification_ShouldThrowException(self, config):

        ft = MagicMock()
        ft.connection.return_value = True

        json = MagicMock()
        json.readJson.return_value = config
        
        with self.assertRaises(Exception) as context:
            BotaPraRodarETL(ft, json)

        self.assertTrue('is not defined' in str(context.exception))

    @parameterized.expand([
        ({             
            "-MVOCULu55b95RyzmSQK": {
                "address": "Rua teste 2",
                "available": True,
                "communityId": "-MLDOXs3p35DEHg0gdUU",
                "createdDate": "20/07/2021",
                "docNumber": 1234,
                "docPicture": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F1234%20_1615330659.jpg?alt=media&token=093112aa-d782-4966-a545-c3d9fd0fbf83",
                "docPictureBack": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F1234%20_1615330663.jpg?alt=media&token=9b6f5836-fe14-4851-8785-c966e5020280",
                "docType": 0,
                "gender": "Masculino",
                "hasActiveWithdraw": False,
                "id": "-MVOCULu55b95RyzmSQK",
                "isBlocked": True,
                "name": "Thiago",
                "path": "users",
                "profilePicture": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F1234%20_1615330652.jpg?alt=media&token=102790cd-ff09-4a1c-986b-7ad6dc942fe9",
                "profilePictureThumbnail": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F1234%20_thumb_1615330652.jpg?alt=media&token=230aaeff-75ef-4547-a199-625bd6dd6e10",
                "residenceProofPicture": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F1234%20_1615330666.jpg?alt=media&token=a768adb3-c848-4705-9092-52b24bf67247",
                "userQuiz": {
                    "accessOtherTransport": True,
                    "accessOtherTransportOpenQuestion": "teste"
                }
            }
        },{
            "-MVOCULu55b95RyzmSQK": {
                "address": "Rua teste 2",
                "available": True,
                "communityId": "-MLDOXs3p35DEHg0gdUU",
                "createdDate": "20/07/2021",
                "docNumber": 1234,
                "gender": "Masculino",
                "hasActiveWithdraw": False,
                "id": "-MVOCULu55b95RyzmSQK",
                "isBlocked": True,
                "name": "Thiago",
                "path": "users",
                "profilePicture": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F1234%20_1615330652.jpg?alt=media&token=102790cd-ff09-4a1c-986b-7ad6dc942fe9",
                "profilePictureThumbnail": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F1234%20_thumb_1615330652.jpg?alt=media&token=230aaeff-75ef-4547-a199-625bd6dd6e10",
                "userQuiz": {
                    "accessOtherTransport": True,
                    "accessOtherTransportOpenQuestion": "teste"
                }
            }
        },)
    ])
    def test_users(self, userJson, userSent):
        self.getBotaPraRodarETL(self.config, userJson)
        self.bt.users()
        self.bt.ft.set.assert_called_once_with(userSent, "/users")

    @parameterized.expand([
        ({             
            "-MgfYTcrUFsX_NXhhvL2": {
                "available": True,
                "communityId": "-MLDOXs3p35DEHg0gdUU",
                "createdDate": "14/01/2022",
                "devolutions": {},
                "id": "-MgfYTcrUFsX_NXhhvL2",
                "inUse": True,
                "name": "Bike 14455 he",
                "orderNumber": 12345,
                "path": "bikes",
                "photoPath": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fbike%2F12345%20_1628523317.jpg?alt=media&token=03ebd3b4-723d-4c4e-8dca-7c647ef2cbf3",
                "photoThumbnailPath": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fbike%2F12345%20_thumb_1628523317.jpg?alt=media&token=fa5fa903-6c62-4d61-8378-62e624030a01",
                "serialNumber": "12345",
                "withdrawToUser": "-MjZx7cic02AXYevcRnt",
                "withdraws":{}
            }
        },{
            "-MgfYTcrUFsX_NXhhvL2": {
                "available": True,
                "communityId": "-MLDOXs3p35DEHg0gdUU",
                "createdDate": "14/01/2022",
                "id": "-MgfYTcrUFsX_NXhhvL2",
                "inUse": True,
                "name": "Bike 14455 he",
                "orderNumber": 12345,
                "path": "bikes",
                "photoPath": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fbike%2F12345%20_1628523317.jpg?alt=media&token=03ebd3b4-723d-4c4e-8dca-7c647ef2cbf3",
                "photoThumbnailPath": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fbike%2F12345%20_thumb_1628523317.jpg?alt=media&token=fa5fa903-6c62-4d61-8378-62e624030a01",
                "serialNumber": "12345",
                "withdrawToUser": "-MjZx7cic02AXYevcRnt",
            }
        },)
    ])
    def test_bikes(self, bikesJson, bikesSent):

        self.getBotaPraRodarETL(self.config, bikesJson)
        self.bt.bikes()
        self.bt.ft.set.assert_any_call(bikesSent, "/bikes")
        #assert_called_once_with(bikesSent, "/bikes")

    @parameterized.expand([
        (    
            ["-sz1cyZoZN1ZijI9fMB7a", {
                    "date": "13/01/2022 22:28:46",
                    "id": "-sz1cyZoZN1ZijI9fMB7a",
                    "quiz": {
                        "destination": "SJC",
                        "giveRide": "N\\u00e3o",
                        "hasDefects": False,
                        "problemsDuringRiding": "N\\u00e3o",
                        "reason": "Seu local de trabalho"
                    },
                    "user": {
                        "address": "Jose Abrao",
                        "age": "01/01/1978",
                        "available": True,
                        "communityId": "-MLDOXs3p35DEHg0gdUU",
                        "createdDate": "14/01/2022",
                        "docNumber": 85573367432,
                        "docPicture": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F85573367432%20_1631633827.jpg?alt=media&token=382f4527-a60f-4252-a4ea-411e7b290630",
                        "docPictureBack": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F85573367432%20_1631633832.jpg?alt=media&token=122c70aa-51b1-4426-89ab-7cb493d849d4",
                        "docType": 0,
                        "gender": "Outro",
                        "hasActiveWithdraw": False,
                        "id": "-MjZx7cic02AXYevcRnt",
                        "income": "Entre 1100 e 2000",
                        "isBlocked": False,
                        "name": "Joao Santoss",
                        "path": "users",
                        "profilePicture": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F85573367432%20_1631633821.jpg?alt=media&token=758a6eab-2683-4ca3-a4d9-ff54eb768ca1",
                        "profilePictureThumbnail": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F85573367432%20_thumb_1631633821.jpg?alt=media&token=510975f9-bb34-42cc-8296-13796b66309b",
                        "racial": "Preta",
                        "residenceProofPicture": "",
                        "schooling": "Ensino m\\u00e9dio",
                        "schoolingStatus": "Completo",
                        "telephone": "51 99876-4567",
                        "userQuiz": {
                            "accessOtherTransport": True,
                            "accessOtherTransportOpenQuestion": "\\u00d4nibus",
                            "alreadyAccidentVictim": True,
                            "alreadyUseBPR": False,
                            "alreadyUseBPROpenQuestion": "2",
                            "motivationOpenQuestion": "saude",
                            "problemsOnWayOpenQuestion": "estradas",
                            "timeOnWayOpenQuestion": "1h:"
                        }
                    },
                    "withdrawId": "-0ZAU0qzoj0ni7pT4bD3j"
                }
            ],{       
            "-0ZAU0qzoj0ni7pT4bD3j": {
                "date": "13/01/2022 22:08:45",
                "id": "-0ZAU0qzoj0ni7pT4bD3j",
                "user": {
                    "address": "Jose Abrao",
                    "age": "01/01/1978",
                    "available": True,
                    "communityId": "-MLDOXs3p35DEHg0gdUU",
                    "createdDate": "14/01/2022",
                    "docNumber": 85573367432,
                    "docPicture": "https: //firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F85573367432%20_1631633827.jpg?alt=media&token=382f4527-a60f-4252-a4ea-411e7b290630",
                    "docPictureBack": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F85573367432%20_1631633832.jpg?alt=media&token=122c70aa-51b1-4426-89ab-7cb493d849d4",
                    "docType": 0,
                    "gender": "Outro",
                    "hasActiveWithdraw": False,
                    "id": "-MjZx7cic02AXYevcRnt",
                    "income": "Entre 1100 e 2000",
                    "isBlocked": False,
                    "name": "Joao Santoss",
                    "path": "users",
                    "profilePicture": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F85573367432%20_1631633821.jpg?alt=media&token=758a6eab-2683-4ca3-a4d9-ff54eb768ca1",
                    "profilePictureThumbnail": "https://firebasestorage.googleapis.com/v0/b/bpr-dev.appspot.com/o/community%2Fuser%2F85573367432%20_thumb_1631633821.jpg?alt=media&token=510975f9-bb34-42cc-8296-13796b66309b",
                    "racial": "Preta",
                    "residenceProofPicture": "",
                    "schooling": "Ensino m\\u00e9dio",
                    "schoolingStatus": "Completo",
                    "telephone": "51 99876-4567",
                    "userQuiz": {
                        "accessOtherTransport": True,
                        "accessOtherTransportOpenQuestion": "\\u00d4nibus",
                        "alreadyAccidentVictim": True,
                        "alreadyUseBPR": False,
                        "alreadyUseBPROpenQuestion": "2",
                        "motivationOpenQuestion": "saude",
                        "problemsOnWayOpenQuestion": "estradas",
                        "timeOnWayOpenQuestion": "1h:"
                    }
                }
            }
        },{
            "-N2qPv6h4LOthGZfpE9K": {
                "id": "-N2qPv6h4LOthGZfpE9K",
                "user_id": "-MjZx7cic02AXYevcRnt",
                "community_id": "-MLDOXs3p35DEHg0gdUU",
                "bike_id": "-MgfYTcrUFsX_NXhhvL2",
                "initiated_at": "13/01/2022 22:08:45",
                "finished_at": "13/01/2022 22:28:46",
                "on_going": False,
                "destination": "SJC",
                "reason": "Seu local de trabalho",
                "problems_during_riding": "N\\u00e3o",
                "give_ride": "N\\u00e3o",
                "path": "travels",
                "time_on_way_open_question": "1h:",
                "access_other_transport": True,
                "access_other_transport_open_question": "\\u00d4nibus",
                "already_accident_victim": True,
                "motivation_open_question": "saude",
                "problems_on_way_open_question": "estradas"
            }
        },)
    ])
    def test_travels(self, devolutions, withdraws, travelsSent):
        bike = {"id":"-MgfYTcrUFsX_NXhhvL2"}
        self.getBotaPraRodarETL(self.config, {})

        self.ft.getUUID.return_value = "-N2qPv6h4LOthGZfpE9K"
        self.jsonUtils.getItemByAttribute.return_value = devolutions

        travels = self.bt.travels(bike, devolutions, withdraws)
        self.assertEquals(travels, travelsSent)

if __name__ == "__main__":
    unittest.main()