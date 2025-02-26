import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://faceattendancerealtime-49a13-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    "321654":
    {
            "nom": "Murtaza Hassan",
            "filière": "Financier&Audit",
            "inscription": 2021,
            "total_attendance": 17,
            "emploi": "Pt",
            "genre": "M",
            "dernière présence": "2024-07-16 17:54:32"

    },

    "651423":
        {
            "nom": "Houssam El Azami",
            "filière": "Informatique",
            "inscription": 2021,
            "total_attendance":20,
            "emploi": "Pl",
            "genre":"M",
            "dernière_présence": "2024-07-20 14:10:29"

        },

    "681354":
        {
            "nom": "Elon Musk",
            "filière": "Direction",
            "inscription": 2020,
            "total_attendance": 36,
            "emploi": "Pl",
            "genre": "M",
            "dernière présence": "2024-08-01 20:49:53"

        },
    "852741":
        {
            "nom": "Emly Blunt",
            "filière": "Marketing&Vente",
            "inscription": 2023,
            "total_attendance": 47,
            "emploi": "Pt",
            "genre": "F",
            "dernière_présence": "2024-08-17 08:54:32"

        }
}

for key,value in data.items():
    ref.child(key).set(value)


