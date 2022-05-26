import json

class JsonUtils:

    def get(self, fileName, path):
        if not path:
            raise Exception("get: Path is not defined")

        file = self.readJson(fileName)
        return file.get(path)

    def readJson(self, fileName):

        if not fileName:
            raise Exception("readJson: File name is not defined")

        file_contents = ""
        with open(fileName, "r") as f:
            file_contents = json.load(f)
        return file_contents

    def printPretty(self, data):
        if not data:
            raise Exception("printPretty: Data is not defined")

        print(json.dumps(data, indent=4, sort_keys=True))

    def getItemByAttribute(self, data, attribute, key): #Criar teste unitário e validações

        if not attribute:
            raise Exception("getItemByAttribute: Attribute is not defined")
        if not key:
            raise Exception("getItemByAttribute: Key is not defined")
        if not data:
            return None

        item = list(filter(lambda d :  d[1].get(attribute)==key, data.items()))
        
        if item:
            return item[0]
        return None