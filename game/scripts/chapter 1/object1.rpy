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
    play music (deposition) fadein 2
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
        play music (deposition) fadein 2
        jump dep11
    else:
        jump object1_1_1
        
label object1_1_4:
    if (try_objection==4):
        show witness_stand:
            offscreenright
        show lara worried:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            xalign 0.5
        show elusia explaining:
            xalign 0.5
        show courtroom_right:
            xalign 1.0 xanchor 0.0
        show ryouzanki normal:
            xalign 1.0 xanchor 0.0
        with None
        e "Je trouve cela très difficile à croire..."
        show courtroom_left:
            offscreenleft
        show elusia explaining:
           offscreenleft
        show courtroom_right:
            center
        show ryouzanki normal:
            center
        with move
        r "Et pourriez vous nous éclairer Bravewill ?"
        show courtroom_left:
            xalign 0.5
        show elusia explaining:
            xalign 0.5
        show courtroom_right:
            xalign 1.0 xanchor 0.0
        show ryouzanki normal:
            xalign 1.0 xanchor 0.0
        with move
        e "Témoin !"
        e "Affirmez vous que dès son entrée, Mr Provist s'est précipité sur la victime ?"
        show witness_stand:
            center
        show lara worried:
            center
        show witness_bar:
            center
        show courtroom_left:
            offscreenleft
        show elusia explaining:
           offscreenleft
        with move
        t1 "Oui ?"
        show witness_stand:
            offscreenright
        show lara worried:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            center
        show elusia explaining:
           center
        with move
        e "Et affirmez vous aussi qur Mr Provist revenait d'une randonnée en montagne..."
        e "Sous une pluie torrentielle ?"
        show witness_stand:
            center
        show lara worried:
            center
        show witness_bar:
            center
        show courtroom_left:
            offscreenleft
        show elusia explaining:
           offscreenleft
        with move
        t1 "Oui mais je ne vois pas en quoi c'est important..."
        show witness_stand:
            offscreenright
        show lara worried:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            center
        show elusia objection:
           center
        with move
        e "Ca l'est !"
        # TODO IMAGEMAP POUR CLIQUER SUR LA CIBLE
        show elusia explaining
        e "C'est la preuve que l'une des deux affirmations est un mensonge."
        e "Si les deux étaient vraies, alors Mr Provist..."
        show elusia objection
        e "Aurait laissé des traces de boue jusqu'au balcon !"
        call influence(+15)
        jump dep11end
    else:
        jump object1_1_1

label object1_1_5:
    if (try_objection==4):
        show witness_stand:
            offscreenright
        show lara worried:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            xalign 0.5
        show elusia explaining:
            xalign 0.5
        show courtroom_right:
            xalign 1.0 xanchor 0.0
        show ryouzanki normal:
            xalign 1.0 xanchor 0.0
        with None
        e "Je trouve cela très difficile à croire..."
        show courtroom_left:
            offscreenleft
        show elusia explaining:
           offscreenleft
        show courtroom_right:
            center
        show ryouzanki normal:
            center
        with move
        r "Et pourriez vous nous éclairer Bravewill ?"
        show courtroom_left:
            xalign 0.5
        show elusia explaining:
            xalign 0.5
        show courtroom_right:
            xalign 1.0 xanchor 0.0
        show ryouzanki normal:
            xalign 1.0 xanchor 0.0
        with move
        e "Témoin !"
        e "Affirmez vous que dès son entrée, Mr Provist s'est précipité sur la victime ?"
        show witness_stand:
            center
        show lara worried:
            center
        show witness_bar:
            center
        show courtroom_left:
            offscreenleft
        show elusia explaining:
           offscreenleft
        with move
        t1 "Oui ?"
        show witness_stand:
            offscreenright
        show lara worried:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            center
        show elusia explaining:
           center
        with move
        e "Et affirmez vous aussi qur Mr Provist revenait d'une randonnée en montagne..."
        e "Sous une pluie torrentielle ?"
        show witness_stand:
            center
        show lara worried:
            center
        show witness_bar:
            center
        show courtroom_left:
            offscreenleft
        show elusia explaining:
           offscreenleft
        with move
        t1 "Oui mais je ne vois pas en quoi c'est important..."
        show witness_stand:
            offscreenright
        show lara worried:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            center
        show elusia objection:
           center
        with move
        e "Ca l'est !"
        # TODO IMAGEMAP POUR CLIQUER SUR LA CIBLE
        show elusia explaining
        e "C'est la preuve que l'une des deux affirmations est un mensonge."
        e "Si les deux étaient vraies, alors Mr Provist..."
        show elusia objection
        e "Aurait laissé des traces de boue jusqu'au balcon !"
        call influence(+15)
        jump dep11end
    else:
        jump object1_1_1
        
label object1_2_1:
    hide screen testimony_scre12
    show bubble_obj_elu
    play sound elusia_obj
    $ renpy.pause(0.5)
    hide bubble_obj_elu
    show courtroom_right:
        offscreenright
    show ryouzanki normal:
        offscreenright
    show courtroom_left:
        center
    show elusia objection:
        center
    with move
    e "OBJECTION !"
    show elusia explaining
    e "Mon client n'était pas au courant pour l'adultère !"
    
    if choix6:
        show bubble_sil_ryou
        play sound ryouzanki_sil
        $ renpy.pause(0.5)
        scene courtroom_right:
            center
        show ryouzanki objection:
            center
        show courtroom_left:
            offscreenleft
        show elusia explaining:
            offscreenleft
        with move
        r "SILENCE !"
        r "Le suspect a lui même avoué qu'il espionnait sa femme !"
        call influence(-10)
    else:
        show bubble_obj_ryou
        play sound ryouzanki_obj
        $ renpy.pause(0.5)
        scene courtroom_right:
            center
        show ryouzanki objection:
            center
        show courtroom_left:
            offscreenleft
        show elusia explaining:
            offscreenleft
        with move
        r "OBJECTION !"
        r "Vous n'avez aucune preuve de ce que vous avancez."
        r "Personne n'avouerait une telle chose !"
    jump retour121
    
label object1_2_2:
    hide screen testimony_scre12
    show bubble_obj_elu
    play sound elusia_obj
    $ renpy.pause(0.5)
    scene courtroom_right:
        offscreenright
    show ryouzanki normal:
        offscreenright
    show courtroom_left:
        center
    show elusia objection:
        center
    with move
    e "OBJECTION !"
    show elusia explaining
    e "Il l'aimait encore et voulait la laisser se reposer plutot que de se disputer avec !"
    if choix6:
        show bubble_obj_ryou
        play sound ryouzanki_obj
        $ renpy.pause(0.5)
        scene courtroom_right:
            center
        show ryouzanki objection:
            center
        show courtroom_left:
            offscreenleft
        show elusia explaining:
            offscreenleft
        with move
        r "OBJECTION !"
        call influence(-3)
    scene courtroom_right:
        center
    show ryouzanki normal:
        center
    show courtroom_left:
        offscreenleft
    show elusia explaining:
        offscreenleft
    with move
    r "Il voulait juste voir si les souris dansaient quand le chat partait !"
    jump retour122
label object1_2_3:
    hide screen testimony_scre12
    show bubble_obj_elu
    play sound elusia_obj
    $ renpy.pause(0.5)
    scene courtroom_right:
        offscreenright
    show ryouzanki normal:
        offscreenright
    show courtroom_left:
        center
    show elusia objection:
        center
    with move
    if not choix4:
        e "Il n'était pas ivre !"
        show bubble_sil_ryou
        play sound ryouzanki_sil
        $ renpy.pause(0.5)
        scene courtroom_right:
            center
        show ryouzanki objection:
            center
        show courtroom_left:
            offscreenleft
        show elusia objection:
            offscreenleft
        with move
        r "SILENCE !"
        r "Son taux d'alcolémie relevé à son arrestation le prouve !"
        call influence(-10)
    else:
        e "Il noyait son chagrin d'amour !"
        e "Boire et tuer une personne sont indépendants !"
        show elusia explaining
        e "La défense aimerait que l'accusation cesse ses conjectures frauduleuses."
        call influence(10)
    jump retour123
    
label object1_2_4:
    hide screen testimony_scre12
    show bubble_obj_elu
    play sound elusia_obj
    $ renpy.pause(0.5)
    scene courtroom_right:
        offscreenright
    show ryouzanki normal:
        offscreenright
    show courtroom_left:
        center
    show elusia objection:
        center
    with move
    e "OBJECTION !"
    e "On ne peut rien déduire de deux personnes en train de prendre un verre !"
    if ryou_attack_1:
        show bubble_sil_ryou
        play sound ryouzanki_sil
        $ renpy.pause(0.5)
        scene courtroom_right:
            center
        show ryouzanki objection:
            center
        show courtroom_left:
            offscreenleft
        show elusia objection:
            offscreenleft
        with move
        r "OBJECTION !"
        show ryouzanki explaining
        r "Prendre un verre ?"
        show ryouzanki objection
        r "La défense a prouvé elle même que la victime était en sous-vêtements au moment des faits !"
        scene courtroom_left
        show elusia down
        with hpunch
        e "Awawawa..."
        call influence(-12)
    elif choix6:
        show bubble_obj_ryou
        play sound ryouzanki_obj
        $ renpy.pause(0.5)
        scene courtroom_right:
            center
        show ryouzanki objection:
            center
        show courtroom_left:
            offscreenleft
        show elusia objection:
            offscreenleft
        with move
        r "OBJECTION !"
        show ryouzanki explaining
        r "Dois-je rappeler que le suspect les espionnait ?"
        show ryouzanki objection
        r "Une fois l'adultère confirmé, il est rentré pour perpétrer son meurtre !"
        show courtroom_right:
            offscreenright
        show ryouzanki normal:
            offscreenright
        show courtroom_left:
            center
        show elusia down:
            center
        with hpunch
        call influence(-6)
        e "Awawawa..."
    jump retour124
    
label object1_2_5:
    hide screen testimony_scre12
    show bubble_obj_elu
    play sound elusia_obj
    $ renpy.pause(0.5)
    scene courtroom_right:
        offscreenright
    show ryouzanki normal:
        offscreenright
    show courtroom_left:
        center
    show elusia objection:
        center
    with move
    e "L'accusation ne cesse de parler au conditionnel !"
    call influence(2)
    show courtroom_right:
        center
    show ryouzanki normal:
        center
    show courtroom_left:
        offscreenleft
    show elusia explaining:
        offscreenleft
    with move
    jump retour125
    