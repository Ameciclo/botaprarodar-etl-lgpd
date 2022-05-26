import firebase_admin
from firebase_admin import db

class FirebaseTool:

    def connection(self, databaseURL, certificateJson):
        try:
            print("Firebase connecting...")
            cred = firebase_admin.credentials.Certificate(certificateJson)
            firebase_admin.initialize_app(cred, {
                'databaseURL': databaseURL
            })
            print("Firebase connected")
        except Exception as e:
            print("Firebase error in connect"+e)

    def get(self, reference = "/"):
        ref = db.reference(reference)
        return ref.get()

    def set(self, data, reference="/"):
        ref = db.reference(reference)
        ref.set(data)
        print(" Data pushed and commited to Firebase")
    
    def push(self, data, reference="/"):
        ref = db.reference(reference)
        ref.push(data)
        print(" Data pushed and commited to Firebase")

    def getUUID(self, reference="/"):
        ref = db.reference(reference)
        return ref.push().key

    def pushPartial(self, data, reference="/", child="users"):
        ref = db.reference(reference)
        ref.child(child).set(data)

    def update(self, data,reference="/"):
        ref = db.reference(reference)
        ref.update(data) # {'chave': 'valor', ...} or {'posts':None}

    def delete(self, reference = "/"):
        ref = db.reference(reference)
        return ref.delete()


