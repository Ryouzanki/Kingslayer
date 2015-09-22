#### Ce fichier contient le code principal ####


init -1 python:
    config.main_menu_music = "medias/musics/main menu.mp3"
    
label splashscreen:
    
    play sound splash
    scene black
    play music "medias/musics/main menu.mp3"
    show main_menu with Dissolve(1)
    $ renpy.pause(2.0)
    show main_menu_idle with dissolve
    return

label influence(modificateur):
    
    if (modificateur < 0):
        $ inf = inf + difficulty * modificateur
    else:
        $ inf = inf + modificateur
    
    if (inf > 100):
        $ inf = 100
        
    if (inf < 0):
        jump game_over
        
    return
    
label game_over:  # TODO
    
    show courtroom_right
    show ryouzanki explaining
    r "Game over"
    $ renpy.full_restart()
    
label start:
    
    call screen diff_imagemap
    play sound select
    show diff_sel
    show main_menu with dissolve
    if _return == "easy":
        $ difficulty = 1
        e "Tachons juste de ne pas accuser notre propre client..."
        
    elif _return == "hard":
        $ difficulty = 2
        e "Misère... Il semblerait que le monde soit contre nous..."

    $ gun_seen = False
    $ inf = 50
    stop music fadeout 1.0
    show black with dissolve
    show screen button
    

    
    
label test:
    
    show courtroom_left:
        xalign 0.5
    show courtroom_right:
        xalign 1.0 xanchor 0.0
    show ryouzanki objection:
        xalign 1.0 xanchor 0.0
    with None
    
    show elusia objection
    e "Objection votre honneur !"
    
    show elusia explaining
    e "Il nous est impossible de faire un procès...."
    e "Sans crime !"
    
    show courtroom_left:
        xalign 0.0 xanchor 1.0
    show elusia explaining:
         xalign 0.0 xanchor 1.0
    show courtroom_right:
        xalign 0.5
    show ryouzanki objection:
        xalign 0.5
    with move
    
    r "Objection !"
    show ryouzanki explaining
    r "On peut toujours faire un procès pour ton incompétence..."
    r "Tiens, baissons un peu ton influence pour commencer..."
    show ryouzanki objection
    r "Enlevons [difficulty] X 30 à tes [inf] misérables points !"
    call influence(-30)
    show ryouzanki explaining
    r "Il t'en reste donc [inf] de tes 50..."
    voice "medias/voices/ryoutest.ogg"
    r "J'ai une voix, c'est trop cool !"
    r "Voyons les preuves..."
    call screen proof1
    r "Mmmh..."
    r "Ajoutons une preuve..."
    $ gun_seen = True
    call screen proof1
    
    return
