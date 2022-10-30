
PATH1 = "music"
PATH2 = "images"

VERSION = "0.10alpha"
ICON = f"{PATH2}/program_icon.png"
track_names = [
                "Monster Hunter - Proof of a Hero", "Monster Hunter Freedom 2 - Proof of a Hero",
                "Monster Hunter Tri - Proof of a Hero", "Monster Hunter 4 - Proof of a Hero", 
                "Monster Hunter Generations Ultimate - Proof of a Hero", "Monster Hunter World - Proof of a Hero",
                "Monster Hunter Rise - Proof of a Hero"
]
images_names = ["commander", "Gore", "Valstrax", "Nergignate", "Magnamalo"]
tracks = [f"{PATH1}/{name}.mp3" for name in track_names]
images = [f"{PATH2}/{name}.jpg" for name in images_names]
