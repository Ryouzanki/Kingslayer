###   Enquete de test a retirer  ###

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
    a "Je suis un témoin"
    if (try_objection>0):
        hide screen testimony_scre
        show courtroom_left
        show elusia objection
        e "Objection !"
        show witness_stand
        show alice geez
        a "Qu'y a t'il ?"
        show courtroom_left
        show elusia explaining
        e "Le témoin n'est pas un témoin !"
        e "Et cette pièce à conviction le prouve !"
        show courtroom_right
        show ryouzanki explaining
        r "On va te retirer 10 points et faire comme on avait rien entendu."
        call influence(-10)
        jump test_testimony
    a "Il n'y a pas de couteau dans les pièces a conviction."
    if (try_objection==1):
        hide screen testimony_scre
        show courtroom_left
        show elusia objection
        e "Objection !"
        show witness_stand
        show alice geez
        a "Qu'y a t'il ?"
        show courtroom_left
        show elusia explaining
        e "Il y en a un !"
        show courtroom_right
        show ryouzanki explaining
        r "Such genius. Many clever... Wow"
        show courtroom_left
        show elusia explaining
        e "Je me redonne 10 points !"
        call influence(10)
        jump test_suite
    elif (try_objection>1):
        hide screen testimony_scre
        show courtroom_left
        show elusia objection
        e "Objection !"
        show witness_stand
        show alice geez
        a "Qu'y a t'il ?"
        show courtroom_left
        show elusia explaining
        e "Il y en a un !"
        show courtroom_right
        show ryouzanki explaining
        r "Elusia, ça n'a rien d'un couteau..."
        r "On va te retirer 5 points et faire comme on avait rien entendu."
        call influence(-5)
        jump test_testimony
    scene courtroom_left
    show elusia explaining
    e "Zut.... J'ai du rater un truc important..."
    jump test_testimony
    
label test_suite:

    show courtroom_left
    show elusia explaining
    with fade
    e "Le témoin mentait donc..."
    return
