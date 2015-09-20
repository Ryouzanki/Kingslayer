#### Ce fichier contient le code principal ####


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
    
    window hide None
    call screen diff_imagemap
    window show None
    
    if _return == "easy":
        $ difficulty = 1
        "Tachez de ne pas accuser votre client..."
        
    elif _return == "hard":
        $ difficulty = 2
        "Le monde est contre vous..."

    $ inf = 50

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
    r "..."

    return
