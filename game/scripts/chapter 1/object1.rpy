label object1_1_1:
    show courtroom_left:
        xalign 0.5
    show elusia explaining:
        xalign 0.5
    show courtroom_right:
        xalign 1.0 xanchor 0.0
    show ryouzanki normal:
        xalign 1.0 xanchor 0.0
    with None
    e "J'ai la preuve formelle, ici présente..."
    show elusia objection
    e "Que !"
    show elusia down
    e "Heu... Que..."
    show courtroom_left:
        offscreenleft
    show elusia down:
       offscreenleft
    show courtroom_right:
        center
    show ryouzanki explaining:
        center
    with move
    r "Que tu manques soit d'expérience ou soit de cervelle."
    show ryouzanki normal
    r "Peut être des deux en fait."
    call influence(-10)
    jump dep11
label object1_1_2:
    # vide mais dispo si besoin
    jump object1_1_1
label object1_1_3:
    if (try_objection==3):
        show courtroom_left:
            xalign 0.5
        show elusia explaining:
            xalign 0.5
        show courtroom_right:
            xalign 1.0 xanchor 0.0
        show ryouzanki normal:
            xalign 1.0 xanchor 0.0
        with None
        e "Il y a quelque chose de très bizarre ici..."
        e "La victime est bien morte immédiatement après l'entrée de Mr Provist n'est-ce pas ?"
        show courtroom_left:
            offscreenleft
        show elusia down:
           offscreenleft
        show courtroom_right:
            center
        show ryouzanki normal:
            center
        with move
        r "C'est ce qu'affirme le témoin en effet."
        show courtroom_left:
            xalign 0.5
        show elusia explaining:
            xalign 0.5
        show courtroom_right:
            xalign 1.0 xanchor 0.0
        show ryouzanki normal:
            xalign 1.0 xanchor 0.0
        with None
        e "apoil lol
        call influence(-10)
        jump dep11
    
    
    jump object1_1_1
label object1_1_4:
    # vide mais dispo si besoin
    jump object1_1_1
label object1_1_5:
    # vide mais dispo si besoin
    jump object1_1_1
    
