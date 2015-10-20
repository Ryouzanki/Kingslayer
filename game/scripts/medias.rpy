#### Dans ce fichier sont déclarés les variables contenant les musiques, les backgrounds et les sprites. ####



### Characters

## Elusia Bravewill

# Sprites
image elusia objection = "medias/sprites/elusia objection.png"
image elusia down = "medias/sprites/elusia down.png"
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
image ryouzanki normal = "medias/sprites/ryouzanki normal.png"
image bubble_obj_ryou = "medias/interface/bubble_obj_ryou.png"
image ryouzanki explaining sepia = im.MatrixColor("medias/sprites/ryouzanki explaining.png", 
        im.matrix.saturation(0.0) * im.matrix.tint(1.0, .94, .76))
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

## Lara Tatouille
image lara normal = im.Composite((200, 520),
                                        (0, 50), "medias/sprites/alice scientist.png",
                                        (0, 50), "medias/sprites/alice normal.png")
image lara worried = im.Composite((200, 520),
                                        (0, 50), "medias/sprites/alice scientist.png",
                                        (0, 50), "medias/sprites/alice sad.png")
image lara hit = im.Composite((200, 520),
                                        (0, 50), "medias/sprites/alice scientist.png",
                                        (0, 50), "medias/sprites/alice angry.png")
image lara broken = im.Composite((200, 520),
                                        (0, 50), "medias/sprites/alice scientist.png",
                                        (0, 50), "medias/sprites/alice geez.png")

### Proof

## Testing area
image knife = "medias/interface/knife.png"
image knife1 = "medias/interface/knife1.png"
image spoon = "medias/interface/spoon.png"
image spoon1 = "medias/interface/spoon1.png"
image gun = "medias/interface/gun.png"
image gun1 = "medias/interface/gun1.png"

## Chapter1
image A1 = "medias/interface/A1.png"
image A2 = "medias/interface/A2.png"
image A3 = "medias/interface/A3.png"
image A4 = "medias/interface/A4.png"
image MA4 = "medias/interface/MA4.png"
image MA1 = "medias/interface/MA1.png"
image MA2 = "medias/interface/MA2.png"
image MA3 = "medias/interface/MA3.png"

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
image courtroom_right sepia = im.MatrixColor("medias/backgrounds/courtroom right.png", 
        im.matrix.saturation(0.0) * im.matrix.tint(1.0, .94, .76))
# Misc
image detention_stand = "medias/backgrounds/detention stand.png"
image detention_bar = "medias/backgrounds/detention stand2.png"

# Encounter
image enc_elu = "medias/interface/encounter_elusia.png"
image enc_ryou = "medias/interface/encounter_ryouzanki.png"
image enc_vs = "medias/interface/encounter_vs.png"

## Fonds unis
image black = "#000000"
image white = "#ffffff"

### Music

# Action theme
define intro = "medias/musics/intro.mp3"
define detention = "medias/musics/detention.mp3"
define courtroom = "medias/musics/courtroom.mp3"
define deposition = "medias/musics/deposition.mp3"
define recession = "medias/musics/pause.mp3"
define clash = "medias/musics/clash.mp3"


### Sounds

# Menus
define splash = "medias/sounds/splash.mp3"
define select = "medias/sounds/select.ogg"
define paf = "medias/sounds/paf.wav"
define duel = "medias/sounds/duel.mp3"

### Positions


init:
    $ hcd = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

