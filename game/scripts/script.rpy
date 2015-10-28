#### Ce fichier contient le code principal ####

init -1 python:
    config.main_menu_music = "medias/musics/main menu.mp3"
    
label encounter:
    
    stop music fadeout 1.0
    play sound duel
    
    show enc_elu:
        offscreenleft
    show enc_ryou:
        offscreenright
    with None
    
    show enc_elu:
        center
    show enc_ryou:
        center
    with ease
    
    show enc_vs with dissolve
    
    $ renpy.pause(0.5)
    
    hide enc_vs with dissolve
    
    show enc_elu:
        offscreenright
    show enc_ryou:
        offscreenleft
    with ease
    
    return
    
label splashscreen:
    
    play sound splash
    scene black
    play music "medias/musics/main menu.mp3"
    show main_menu with Dissolve(1)
    $ renpy.pause(2.0)
    show main_menu_idle with dissolve
    return
    
label game_over:  # TODO
    
    scene courtroom_right
    show ryouzanki explaining
    with fade
    r "Cette farce a suffisemment duré Bravewill."
    show judge with dissolve
    j "Je suis tout à fait d'accord."
    j "Cette court déclare l'accusé coupable d'homicide."
    scene black with dissolve
    show text "Ce n'est pas possible..." with dissolve
    $ renpy.pause(2.0)
    show text "Non... Ce monde... Il..." with dissolve
    $ renpy.pause(2.0)
    show text "Il a juste besoin de justice..." with dissolve
    $ renpy.pause(2.0)
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

    stop music fadeout 1.0
    show black with dissolve
    
    # jump test
    
    call intro
    jump chap1

    return
