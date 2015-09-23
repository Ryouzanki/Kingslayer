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
    
    scene courtroom_right
    show ryouzanki explaining with fade
    r "Tu as perdu tous tes points..."
    r "Game over."
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

    jump test

    return
