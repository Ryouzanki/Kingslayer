#### Dans ce fichier, on déclare les personnages ####

init python:

    style.nvl_window.xpadding = 130
    style.nvl_window.ypadding = 110
    style.nvl_vbox.box_spacing = 18
    style.nvl_window.background = "medias/interface/nvl.png"
    config.window_hide_transition = fade
    config.window_show_transition = dissolve

# Avocat du barreau Elusia
define e = Character(what_color="#009900", window_background="medias/interface/textbox elusia.png")
define envl = Character(kind=nvl, color="#009900")

# Procureur Ryouzanki
define r = Character(what_color="#EE0000", window_background="medias/interface/textbox ryouzanki.png")

# Judge
define j =  Character(what_color="#555555")

# Témoins
define a =  Character(what_color="#EE8811") # (test)
define alain =  Character(what_color="#445566")
