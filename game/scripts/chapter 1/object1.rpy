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
        show elusia explaining:
           offscreenleft
        show courtroom_right:
            center
        show ryouzanki normal:
            center
        with move
        r "C'est ce qu'affirme le témoin en effet."
        show ryouzanki explaining
        r "Bravewill, dîtes nous donc ce qui vous chagrine tant."
        show courtroom_left:
            xalign 0.5
        show elusia explaining:
            xalign 0.5
        show courtroom_right:
            xalign 1.0 xanchor 0.0
        show ryouzanki normal:
            xalign 1.0 xanchor 0.0
        with move
        # TODO IMAGEMAP POUR CLIQUER SUR LA CIBLE
        e "La victime..."
        show elusia objection
        e "Elle est en caleçon !"
        show courtroom_left:
            offscreenleft
        show elusia explaining:
           offscreenleft
        show courtroom_right:
            center
        show ryouzanki normal:
            center
        with move
        r "Je ne vois pas en quoi cette information fait avancer l'enquête."
        show courtroom_left:
            xalign 0.5
        show elusia explaining:
            xalign 0.5
        show courtroom_right:
            xalign 1.0 xanchor 0.0
        show ryouzanki normal:
            xalign 1.0 xanchor 0.0
        with move
        e "Cela prouve que le témoin ici présent nous ment."
        show elusia normal
        e "A moins qu'aller discuter avec une inconnue en caleçon soit à la mode..."
        scene witness_stand:
            offscreenleft
        show lara worried:
            offscreenleft
        show witness_bar:
            offscreenleft
        show courtroom_left:
            offscreenleft
        show elusia normal:
           offscreenleft
        show courtroom_right:
            center
        show ryouzanki explaining:
            center
        with move
        r "Je vous croyais moins naïve, Bravewill..."
        show ryouzanki normal
        r "Reprenons donc."
        r "Mr Provist entre dans la salle et surprend sa femme en plein adultère."
        scene witness_stand:
            center
        show lara worried:
            center
        show witness_bar:
            center
        show courtroom_left:
            offscreenleft
        show elusia down:
           offscreenleft
        show courtroom_right:
            offscreenright
        show ryouzanki normal:
            offscreenright
        with move
        show lara hit
        t1 "Hey ! Je..."
        scene witness_stand:
            offscreenleft
        show lara worried:
            offscreenleft
        show witness_bar:
            offscreenleft
        show courtroom_left:
            offscreenleft
        show elusia down:
           offscreenleft
        show courtroom_right:
            center
        show ryouzanki explaining:
            center
        with move
        r "Silence ! Qu'il vous surprenne en adultère ou en tentative d'adultère..."
        show ryouzanki normal
        r "Ne change pas le fait qu'il était peu habillé."
        r "L'accusation aimerait que cela soit contenu dans la dépostion." 
       
        $ ryou_attack_1 = True
        
        jump dep11
    else:
        jump object1_1_1
        
label object1_1_4:
    # vide mais dispo si besoin # TODO
    jump object1_1_1
label object1_1_5:
    # vide mais dispo si besoin # TODO
    jump object1_1_1
    
