label press11:
    
    # TODO mettre le squelette des "UN INSTANT" ici
    
    scene witness_stand:
        center
    show lara worried:
        center
    show witness_bar:
        center
    show courtroom_left:
        offscreenleft
    show elusia explaining:
        offscreenleft
    with None
    
    hide screen testimony_scre11
    
    if(witness_statement == 1):
        show witness_stand:
            offscreenright
        show lara normal:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            center
        show elusia explaining:
            center
        with move
        e "Et donc vous êtes partis en vacances ?"
        show witness_stand:
            center
        show lara normal:
            center
        show witness_bar:
            center
        show courtroom_left:
            offscreenleft
        show elusia explaining:
            offscreenleft
        with move
        t1 "Oui."
        show witness_stand:
            offscreenright
        show lara normal:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            center
        show elusia explaining:
            center
        with move
        e "Avec Mr Alain Provist ?"
        show witness_stand:
            center
        show lara normal:
            center
        show witness_bar:
            center
        show courtroom_left:
            offscreenleft
        show elusia explaining:
            offscreenleft
        with move
        t1 "Oui."
        show witness_stand:
            offscreenright
        show lara normal:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            center
        show elusia normal:
            center
        with move
        e "Dans un hôtel à la montagne ?"
        show witness_stand:
            center
        show lara normal:
            center
        show witness_bar:
            center
        show courtroom_right:
            offscreenright
        show ryouzanki normal:
            offscreenright
        show courtroom_left:
            offscreenleft
        show elusia normal:
            offscreenleft
        with move
        t1 "Oui..."
        show witness_stand:
            offscreenleft
        show lara normal:
            offscreenleft
        show witness_bar:
            offscreenleft
        show courtroom_right:
            center
        show ryouzanki normal:
            center
        with move
        r "Je crois que quelqu'un ici aurait bien besoin de vacances..."
        
    elif(witness_statement == 2):
        show witness_stand:
            offscreenright
        show lara normal:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            center
        show elusia explaining:
            center
        with move
        e "Pourquoi n'est-il pas resté à vos côtés plutôt ?"
        e "Je trouve cela étrange qu'il vous laisse ainsi seule..."
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
        t1 "Nous ne nous entendions plus depuis quelques mois..."
        show lara normal
        t1 "Il voulait que l'on parte en vacance ensemble mais me laisse derrière dès le premier obstacle."
        t1 "En plus, il pleuvait des cordes..."
        show lara worried
        t1 "C'est dire à quel point il veut m'éviter."
        
    elif(witness_statement == 3):
        show witness_stand:
            offscreenright
        show lara normal:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            center
        show elusia normal:
            center
        with move
        e "Quand cela est-il arrivé ?"
        show witness_stand:
            center
        show lara normal:
            center
        show witness_bar:
            center
        show courtroom_left:
            offscreenleft
        show elusia normal:
            offscreenleft
        with move
        t1 "Si ma mémoire est bonne..."
        t1 "Il était partit depuis deux heures et il pleuvait toujours autant."
        t1 "Il devait être quelque chose comme 22h."
        show witness_stand:
            offscreenright
        show lara normal:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            center
        show elusia explaining:
            center
        with move
        menu:
            "Ce sera tout.":
                e "Ce sera tout."
            "Connaissiez vous donc la victime ?":
                e "Connaissiez vous donc la victime ?"
                show witness_stand:
                    center
                show lara normal:
                       center
                show witness_bar:
                       center
                show courtroom_left:
                       offscreenleft
                show elusia normal:
                       offscreenleft
                with move
                t1 "Non. Je m'ennuyais en attendant le retour de mon mari."
                t1 "Il m'a juste tenu compagnie et on a juste discuté dans le couloir."
                t1 "Puis voulant m'asseoir, je l'ai invité à prendre un verre à ma table."
            "Comment est rentré Mr Provist ?":
                e "Comment est rentré Mr Provist ?"
                show witness_stand:
                    center
                show lara hit:
                       center
                show witness_bar:
                       center
                show courtroom_left:
                       offscreenleft
                show elusia normal:
                       offscreenleft
                with move
                t1 "Il est rentré en hurlant comme un taré !"
                show lara worried
                t1 "Il était plein de boue et puait l'alcool."
                t1 "Et puis il... Il l'a fait sous mes yeux..."
                
    elif(witness_statement == 4):
        show witness_stand:
            offscreenright
        show lara normal:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            center
        show elusia normal:
            center
        with move
        e "Vous voulez dire que dès qu'il a ouvert la porte, il a couru pour attaquer la victime ?"
        show courtroom_right:
            offscreenright
        show ryouzanki explaining:
            offscreenright
        show witness_stand:
            center
        show lara hit:
            center
        show witness_bar:
            center
        show courtroom_left:
            offscreenleft
        show elusia normal:
            offscreenleft
        with move
        t1 "Oui..."
        t1 "Il n'avait même pas pris la peine de fermer la porte derrière lui..."
        show courtroom_right:
            center
        show ryouzanki explaining:
            center
        show witness_stand:
            offscreenleft
        show lara hit:
            offscreenleft
        show witness_bar:
            offscreenleft
        with move
        r "Comme c'est dramatque..."
        show ryouzanki normal
        r "Un homme ivre entre et croit voir sa femme le tromper avec un inconnu..."
        r "Votre honneur, voici votre motif !"
        call influence(-2)
    elif(witness_statement == 5):
        show witness_stand:
            offscreenright
        show lara normal:
            offscreenright
        show witness_bar:
            offscreenright
        show courtroom_left:
            center
        show elusia normal:
            center
        with move
        e "Il y a quelque chose qui me gêne là..."
        menu:
            "Vous dîtes qu'il hurlait sans arrêt ?":
                e "Vous dîtes qu'il hurlait sans arrêt ?"
                show witness_stand:
                      center
                show lara hit:
                   center
                show witness_bar:
                       center
                show courtroom_left:
                           offscreenleft
                show elusia normal:
                          offscreenleft
                with move
                t1 "Il hurlait des trucs sans queues ni têtes d'ivrognes..."
                t1 "Du genre \"PRAISE THE SUN\", tout ça, tout ça..."
            "Qu'a fait la victime ?":
                e "Qu'a fait la victime ?"
                show courtroom_right:
                    offscreenleft
                show elusia explaining:
                    offscreenleft
                show witness_stand:
                      center
                show lara hit:
                   center
                show witness_bar:
                       center
                with move
                t1 "Ca s'est passé si vite..."
                t1 "Mr Goland reculait en demandant à Alain de reprendre son calme pour lui expliquer la situation."
                t1 "Mais Alain ne voulait rien entendre et continuait de le bousculer en hurlant."
    else:
        "ERROR PRESS NOT FOUND"


    scene black with dissolve
    call influence(-1)
    jump dep11
