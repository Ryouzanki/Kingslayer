#### Dans ce fichier, on déclare les personnages ####

init python:
    def callbackcontinue(ctc, **kwargs):
        if ctc == "end":
            renpy.music.play("medias/sounds/click.mp3",channel="sound")
            
init python:

    style.nvl_window.xpadding = 130
    style.nvl_window.ypadding = 110
    style.nvl_vbox.box_spacing = 18
    style.nvl_window.background = "medias/interface/nvl.png"
    config.window_hide_transition = fade
    config.window_show_transition = dissolve

# Avocat du barreau Elusia
define e = Character(what_color="#009900", window_background="medias/interface/textbox elusia.png",callback=callbackcontinue)
define envl = Character(kind=nvl, color="#009900",callback=callbackcontinue)

# Procureur Ryouzanki
define r = Character(what_color="#EE0000", window_background="medias/interface/textbox ryouzanki.png",callback=callbackcontinue)

# Judge
define j =  Character(what_color="#555555",callback=callbackcontinue)

# Témoins
define a =  Character(what_color="#EE8811",callback=callbackcontinue) # (test)
define alain =  Character(what_color="#445566",callback=callbackcontinue)
define t1 = Character(what_color="#7788EE",callback=callbackcontinue) # témoin a redéclarer a chaque enquete
