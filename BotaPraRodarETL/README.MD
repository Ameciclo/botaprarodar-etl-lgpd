# PROJETO BOTA PRA RODAR 

### INSTALL 
- Connect to firebase 
    - (MAC) `python3 -m pip install firebase_admin` 
    - (Others) `pip install firebase_admin`

- TO run tests
    - (MAC) `python3 -m pip install parameterized `
    - (Others) `pip install parameterized` 

### GENERATE CREDENTIALS (From the bank you want to put the data)
- Go to Firebase-console -> Project Overview -> Service accounts -> Generate new private key (Put in resource `OriginCertificateJson.json`)
- Get the `databaseURL` from Realtime Database that are showing  (Put the URL in `resources/config.json/OriginDatabaseURL`)

### EXPORT DATABASE
- Export the json from Realtime Database, to do that you need to go to realtime database -> data -> three dots -> Export Json (Put in resorce `OriginJson.json`)

### TO RUN 
- (Test) You can go to `test/BotaPraRodarETL_test.py` to execute unit test, just execute the class with Python3
- (Prod) `BotaPraRodarETL.py` just run the class main

### REFERENCES
- https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/
- https://github.com/wolever/parameterized
- https://docs.python.org/3/library/unittest.mock.html
