###   Enquete de test a retirer  ###

label test:
    
    $ gun_seen = False
    $ inf = 50
    
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
    
    play sound ryouzanki_obj
    show bubble_obj_ryou
    $ renpy.pause(0.5)
    hide bubble_obj_ryou
    
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
    r "Tiens, affichons ton influence..."
    $ show_infl = True
    show ryouzanki objection
    r "Puis baissons un peu ton influence pour commencer..."
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
    r "Appelons a présent le premier témoin"
    $ try_objection = 0
    
label test_testimony:
    
    show screen testimony_scre
    $ try_objection = 0
    scene witness_stand
    show alice normal
    show witness_bar
    with fade
    $ witness_statement = 1
    a "Je suis un témoin"
    $ witness_statement = 2
    a "Il n'y a pas de couteau dans les pièces a conviction."
    
    hide screen testimony_scre
    scene witness_stand
    show alice satisfied
    show witness_bar
    with fade
    a "Mon témoignage convient-il ?"
    a "Je peux rentrer chez moi ?"
    menu:
        "Vous pouvez partir.":
            scene courtroom_left:
                xalign 0.5
            show courtroom_right:
                xalign 1.0 xanchor 0.0
            show ryouzanki explaining:
                xalign 1.0 xanchor 0.0
            show elusia explaining
            e "Vous pouvez partir."
            show courtroom_left:
                xalign 0.0 xanchor 1.0
            show elusia explaining:
                xalign 0.0 xanchor 1.0
            show courtroom_right:
                xalign 0.5
            show ryouzanki explaining:
              xalign 0.5
            with move
            r "T'es sérieuse là ? On devrait te retirer des points pour ça..."
            r "Réécoute un peu..."
            
        "Non, J'ai du rater quelque chose...":
            scene courtroom_left
            show elusia explaining
            e "Non, J'ai du rater quelque chose..."
            
    jump test_testimony

label object_1_X:
    
    show witness_stand
    show alice geez
    show witness_bar
    a "Qu'y a t'il ?"
    scene courtroom_left:
        xalign 0.5
    show courtroom_right:
        xalign 1.0 xanchor 0.0
    show ryouzanki objection:
        xalign 1.0 xanchor 0.0
    with None
    show elusia explaining
    e "Le témoin n'est pas un témoin !"
    play sound ryouzanki_obj
    show bubble_obj_ryou
    $ renpy.pause(0.5)
    hide bubble_obj_ryou
    show courtroom_left:
        xalign 0.0 xanchor 1.0
    show elusia explaining:
         xalign 0.0 xanchor 1.0
    show courtroom_right:
        xalign 0.5
    show ryouzanki objection:
        xalign 0.5
    with move
    r "OBJECTION !"
    r "Elusia, ce n'est qu'un test, on s'en fout sérieusement..."
    show ryouzanki explaining
    r "On va te retirer 10 points et faire comme on avait rien entendu."
    call influence(-10)
    jump test_testimony
    
label object_2_X:
    
    if (try_objection==1):
        show witness_stand
        show alice geez
        show witness_bar
        a "Qu'y a t'il ?"
        scene courtroom_left:
            xalign 0.5
        show courtroom_right:
            xalign 1.0 xanchor 0.0
        show ryouzanki explaining:
            xalign 1.0 xanchor 0.0
        show elusia explaining
        e "Il y en a un !"
        show courtroom_left:
            xalign 0.0 xanchor 1.0
        show elusia explaining:
            xalign 0.0 xanchor 1.0
        show courtroom_right:
            xalign 0.5
        show ryouzanki explaining:
            xalign 0.5
        with move
        r "Such genius. Many clever... Wow"
        show courtroom_left:
            xalign 0.5
        show courtroom_right:
            xalign 1.0 xanchor 0.0
        show ryouzanki explaining:
            xalign 1.0 xanchor 0.0
        show elusia explaining:
            xalign 0.5
        with move
        e "Je me redonne 10 points !"
        call influence(10)
        jump test_suite
    else:
        show witness_stand
        show alice geez
        show witness_bar
        a "Qu'y a t'il ?"
        scene courtroom_left:
            xalign 0.5
        show courtroom_right:
            xalign 1.0 xanchor 0.0
        show ryouzanki explaining:
            xalign 1.0 xanchor 0.0
        show elusia explaining
        e "Il y en a un !"
        if (try_objection==2):
            e "Et cette cuillère le prouve !"
        else:
            e "Et ce pistolet le prouve !"
        show courtroom_left:
            xalign 0.0 xanchor 1.0
        show elusia explaining:
            xalign 0.0 xanchor 1.0
        show courtroom_right:
            xalign 0.5
        show ryouzanki explaining:
            xalign 0.5
        with move
        r "Elusia, ça n'a rien d'un couteau..."
        r "On va te retirer 5 points et faire comme on avait rien entendu."
        call influence(-5)
        jump test_testimony
        
label press_test:
    
    hide screen testimony_scre
    if(witness_statement == 1):
        scene courtroom_left
        show elusia explaining
        e "C'est quoi un témoin ?"
        show witness_stand
        show alice geez
        show witness_bar
        a "C'est quelqu'un qui ment toujours."
    else:
        scene courtroom_left
        show elusia explaining
        e "Comment pouvez vous en être sure ?"
        show witness_stand
        show alice geez
        show witness_bar
        a "Je connais toutes les preuves..."

    call influence(-1)
    jump test_testimony
    
label test_suite:

    scene courtroom_left
    show elusia explaining
    with fade
    e "Le témoin mentait donc..."
    return
