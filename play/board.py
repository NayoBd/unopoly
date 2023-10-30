cases = {
    "start": {
        "getMoney": 100,
        "getCard": 1,
    },
    "gray": {
        0: {
            "type": "home",
            "name": "1",
            "price": None,
            "taxe": None,
        },
        1: {
            "type": "communotaire",
            "name": "CommUNOtaire",
            "getCommunotaireCard": 1,
        },
        2: {
            "type": "home",
            "price": None,
            "taxe": None,
        },
        3: {
            "type": "unpot",
            "name": "Un pot sur le revenu",
            "takeMoney": 100,
            "takeCard": 1,
        }
    },
    "gare1": {
        "name": "UNI",
        "price": None,
        "taxe": 25,
    },
    "green": {
        0: {
            "type": "home",
            "name": "1",
            "price": None,
            "taxe": None,
        },
        1: {
            "type": "luck",
            "name": "Coup de poly",
            "getLuckCard": 1,
        },
        2: {
            "type": "home",
            "name": "1",
            "price": None,
            "taxe": None,
        },
        3: {
            "type": "home",
            "name": "1",
            "price": None,
            "taxe": None,
        },
    },
    "jail": {
        0: {
            "type": "visit",
            "possibilities": {
                0: {

                },
                1: {
                    "takeMoney": 100,
                    "stealCard": 1,
                }
            }
        },
        1: {
            "type": "jailed",
            "getCard": 1,
            "tours": 3,
            "possibilities": {
                0: {
                    
                },
                1: {
                    "takeMoney": 100,
                    "getcard":1,
                }
            }
        }
    }
}
