init python: 

    # Variable pour cacher et afficher la barre
    show_infl=False

    def stats_overlay():               
        if show_infl:
            ui.frame( xalign = 0.5,  ypos = 0, )
            ui.vbox(xalign = 0.5)
            # ui.text ("Points d'influence : %d" %inf, xalign = 0.5)  # Pour le debug seulement
            ui.bar(100, inf, style="infl_bar")
            
            ui.close()
           
    config.overlay_functions.append(stats_overlay)
    
init -5 python:
    
    # Custom bar
    style.infl_bar = Style(style.default)
    style.infl_bar.xalign = 0.5
    style.infl_bar.xmaximum = 304 # largeur 315
    style.infl_bar.ymaximum = 35 # hauteur 30
    style.infl_bar.left_gutter = 78 # 5 bord reel
    style.infl_bar.right_gutter = 81 # 5 bord reel
    
    style.infl_bar.left_bar = Frame("medias/interface/bar_full.png", 0, 0)
    style.infl_bar.right_bar = Frame("medias/interface/bar_empty.png", 0, 0)
    style.infl_bar.hover_left_bar = Frame("medias/interface/bar_hover.png", 0, 0)
    
    style.my_bar.thumb = "ui/thumb.png"
    style.infl_bar.thumb_shadow = None
    style.infl_bar.thumb_offset = 5
    
label influence(modificateur):

#########   TROP LENT POUR ANDROID
#
#    if (modificateur < 0):
#        $ count = difficulty * modificateur
#        while count < 0:
#            $ inf = inf - 1
#            $ count = count + 1
#            play sound "medias/sounds/gauge.wav"
#            pause 0.01
#    else:
#        $ count = modificateur
#        while count > 0:
#            $ inf = inf + 1
#            $ count = count - 1
#            play sound "medias/sounds/gauge.wav"
#            pause 0.01
#
#######    VERSION LIGHT            
    if (modificateur < 0):
        $ inf = inf + (difficulty * modificateur)

    else:
        $ inf = inf + modificateur
#######    VERSION LIGHT END
    
    if (inf > 100):
        $ inf = 100
        
    if (inf < 0):
        jump game_over
        
    return