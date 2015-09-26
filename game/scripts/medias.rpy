#### Dans ce fichier sont déclarés les variables contenant les musiques, les backgrounds et les sprites. ####



### Characters

## Elusia Bravewill

# Sprites
image elusia objection = "medias/sprites/elusia objection.png"
image elusia explaining = "medias/sprites/elusia explaining.png"
image elusia normal = "medias/sprites/elusia normal.png"
image bubble_obj_elu = "medias/interface/bubble_obj_elu.png"
image CG_elusia_thinking = "medias/sprites/elusia thinking CG.png"
image elusia_grey = "medias/sprites/elusia thinking CG grey.png"

# Voice
define elusia_obj = "medias/sounds/elusia object.mp3"

## Ryouzanki Zeldar

# Sprites
image ryouzanki objection = "medias/sprites/ryouzanki objection.png"
image ryouzanki explaining = "medias/sprites/ryouzanki explaining.png"
image bubble_obj_ryou = "medias/interface/bubble_obj_ryou.png"

# Voice
define ryouzanki_obj = "medias/sounds/ryouzanki object.mp3"

## Alice Drezall
image alice normal = im.Composite((200, 520),
                                        (0, 50), "medias/sprites/alice scientist.png",
                                        (0, 50), "medias/sprites/alice normal.png")
image alice sad = im.Composite((200, 520),
                                        (0, 50), "medias/sprites/alice scientist.png",
                                        (0, 50), "medias/sprites/alice sad.png")
image alice angry = im.Composite((200, 520),
                                        (0, 50), "medias/sprites/alice scientist.png",
                                        (0, 50), "medias/sprites/alice angry.png")
image alice happy = im.Composite((200, 520),
                                        (0, 50), "medias/sprites/alice scientist.png",
                                        (0, 50), "medias/sprites/alice happy.png")
image alice geez = im.Composite((200, 520),
                                        (0, 50), "medias/sprites/alice scientist.png",
                                        (0, 50), "medias/sprites/alice geez.png")
image alice satisfied = im.Composite((200, 520),
                                        (0, 50), "medias/sprites/alice scientist.png",
                                        (0, 50), "medias/sprites/alice satisfied.png")

## Alain Provist
image alain normal = "medias/sprites/alain normal.png"
image alain panick = "medias/sprites/alain panick.png"

### Proof

## Testing area
image knife = "medias/interface/knife.png"
image knife1 = "medias/interface/knife1.png"
image spoon = "medias/interface/spoon.png"
image spoon1 = "medias/interface/spoon1.png"
image gun = "medias/interface/gun.png"
image gun1 = "medias/interface/gun1.png"

### Background

# Menus
image main_menu = "medias/interface/mm_ground.png"
image main_menu_idle = "medias/interface/mm_idle.png"
image diff_sel = "medias/interface/diff_idle.png"
image CG_thinking = "medias/backgrounds/thinking.png"

define freq = 0.4  # defini la frequence des engrenages
image CG_thinking_anim:
    "medias/backgrounds/thinking.png"
    pause freq
    "medias/backgrounds/thinking2.png"
    pause freq
    repeat

# Courtroom
image courtroom_left = "medias/backgrounds/courtroom left.png"
image courtroom_right = "medias/backgrounds/courtroom right.png"
image witness_stand = "medias/backgrounds/witness stand.png"
image witness_bar = "medias/backgrounds/witness stand2.png"
image waiting = "medias/backgrounds/waiting room.png"
image judge = "medias/backgrounds/judge.png"

# Misc
image detention_stand = "medias/backgrounds/detention stand.png"
image detention_bar = "medias/backgrounds/detention stand2.png"

## Fonds unis
image black = "#000000"
image white = "#ffffff"

### Music

# Action theme
define intro = "medias/musics/intro.mp3"
define detention = "medias/musics/detention.mp3"


### Sounds

# Menus
define splash = "medias/sounds/splash.mp3"
define select = "medias/sounds/select.ogg"
define paf = "medias/sounds/paf.wav"



