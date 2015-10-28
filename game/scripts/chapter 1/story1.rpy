###  Fichier contenant le tronc de l'enquete  ###

screen tuto_object:

    $ ui.imagebutton("medias/interface/objection.png", "medias/interface/objection.png", yalign = 0.5, clicked=[Jump("tuto_object_end")])
    
label chap1:
    
    $ ryou_attack_1 = False  # confirmation victime en caleçon
    $ ryou_attack_2 = False  # confirmation mauvais lieu du crime
    $ ryou_attack_3 = False
    
    $ inf = 50
    scene waiting with dissolve
    show screen menu_base
    e "Enfin j'y suis... Mon premier procès !"
    e "Je suis à la fois excitée et complètement terrifiée..."
    play sound paf
    show alain panick with hpunch
    alain "Hey ! Ca va pas de dire ça devant moi ?!"
    e "Oops pardon..."
    show alain normal
    e "Mais tout ira bien ! Je te le promets !"
    show elusia_grey
    envl "Lui c'est Alain. Mon premier client."
    envl "C'est aussi un ami à moi depuis l'école primaire."
    envl "Il est typiquement le genre de garçon discret et sans histoire."
    envl "On s'était perdu de vue après le collège \nmais quand j'ai vu qu'il avait besoin d'aide..."
    envl "Je me suis dépêchée d'aller le voir en garde a vue."
    envl "En le voyant tout paniqué, j'ai promis \nde l'aider."
    envl "J'imaginais des retrouvailles plus \nchaleureuses."
    nvl clear
        
# label tuto1:
    # 
    # nvl clear
    # envl "Je me rappelle parfaitement de {a=det_01}ce qu'on s'est dit{/a}"
    # envl "D'ailleurs pour m'en rappeler, je peux cliquer sur les phrases en bleu."
    # envl "Je pourrais toujours me concentrer sur un élément entendu en cliquant dessus."
    # envl "S'il y a matière à réflexion dessus bien sur..."
# 
    # jump tuto1
    
label det_01:
    
    scene black with dissolve
    show text "Quelques jours plus tôt" with dissolve
    $ renpy.pause(1.0)
    
    play sound paf
    play music (detention) fadein 2
    
    scene detention_stand:
        xalign 0.5
    show alain panick:
        xalign 0.5
    show detention_bar:
        xalign 0.5
    with hpunch
    
    alain "C'est vrai ?! Tu vas m'aider ?"
    e "Oui Alain, c'est promis !"
    show alain normal
    alain "Je peux te faire confiance hein..."
    e "Oui mais d'abord, j'aimerais te poser quelques questions..."
    
    $ choix1 = True
    $ choix2 = True
    $ choix3 = True
    $ choix4 = False
    $ choix5 = False
    $ choix6 = False
    $ choix7 = False
    $ choix8 = False
    $ choix9 = False
    $ choix10 = False

label interro1:
    
    menu:
        "De quoi t'accuses t'on exactement ?" if choix1:
            $ choix1 = False
            e "De quoi t'accuses t'on exactement ?"
            alain "Tu vas droit au but pas vrai..."
            alain "On m'accuse d'avoir assassiné l'amant de ma fiancée..."
            $ choix4 = True
            $ choix5 = True
            $ choix10 = True
        "Est-ce que tu l'as fait ?" if choix4:
            $ choix4 = False
            e "Est-ce que tu l'as fait ?"
            play sound paf
            show alain panick with hpunch
            alain "Tu plaisantes ?"
            e "Non, je ne plaisante pas. Tu sais, j'ai promis de t'aider indépendamment de ce qui s'est passé."
            e "De plus, je suis tenue par le secret professionel."
            show alain normal
            alain "Tu me connais depuis tout petit. Tu sais que je ne ferais pas de mal à une mouche !"
            alain "Je ne l'ai pas tué, non. Je ne l'ai même jamais vu."
        "Que s'est-il passé ?" if choix5:
            $ choix5 = False
            e "Que s'est-il passé ?"
            alain "Je ne sais pas. On m'a immédiatement arrêté à la sortie de ma chambre."
            alain "La police m'a dit qu'ils avaient trouvé le corps de la victime sous mon balcon."
            play sound paf
            show alain panick with hpunch
            alain "Ils disent qu'ils ont même un témoin de la scène !"
            show alain normal
            $ choix6 = True
            $ choix7 = True
        "Sais-tu qui est leur témoin ?" if choix6:
            $ choix6 = False
            e "Sais-tu qui est leur témoin ?"
            alain "Non, mais ça me fait peur... "
            play sound paf
            show alain panick with hpunch
            alain "Je suis pourtant resté seul dans ma chambre..."
            play sound paf
            show alain panick with hpunch
            alain "Et je n'ai rien fait ! Je suis innocent !"
            show alain normal
        "Parle moi de toi..." if choix2:
            $ choix2 = False
            e "Parle moi de toi..."
            alain "Oh tu veux dire, depuis qu'on s'est perdu de vue ?"
            alain "Il y a tant à raconter et je n'ai vraiment pas la tête à ça, désolé..."
            e "Oui mais j'ai besoin de plus d'information pour te défendre..."
            $ choix8 = True
            $ choix9 = True
        "Parle moi de ta situation en fait..." if choix8:
            $ choix8 = False
            e "Parle moi de ta situation en fait..."
            alain "Et bien... Je dirige le service d' analyse dans un laboratoire."
            alain "Je gagne plutôt bien ma vie."
            alain "Je suis fiancé et j'ai un enfant naturel."
        "Parle moi de ta fiancée et de son amant..." if (choix9 & choix10):
            $ choix10 = False
            $ choix9 = False
            e "Ecoute, je sais que je remue le couteau dans la plaie."
            e "Mais j'ai besoin d'en savoir plus alors..."
            e "Parle moi de ta fiancée et de son amant..."
            play sound paf
            show alain panick with hpunch
            alain "Je ne savais même pas qu'elle avait un amant !"
            alain "Et je ne l'ai jamais vu de toute ma vie !"
            show alain normal
            alain "Et ma fiancée... Qu'elle aille au diable."
        "Au sujet de mes honoraires..." if choix3:
            $ choix3 = False
            e "Au sujet de mes honoraires..."
            alain "Oui, je les paierais."
            alain "N'as tu pas de question plus importantes ?"
        "Ce sera tout, merci." if choix7:
            e "Ce sera tout merci."
            play sound paf
            show alain panick with hpunch
            alain "Je suis innocent !"
            e "Oui je sais Alain, ne t'en fais pas..."
            e "Je te promets de tout faire pour que tu sois innocenté !"
            e "On se revoit au procès d'accord ?"
            show alain normal
            alain "Dis comme ça, ce n'est pas très encourageant..."
            stop music fadeout 1.0
            jump proc1
            
    jump interro1
            
label proc1:
    
    scene black with dissolve
    $ renpy.pause(1.0)
    
    scene waiting:
        xalign 0.5
    show alain normal:
        xalign 0.5
    with dissolve
    
    alain "Elusia ? Tu m'entends ?"
    e "Ah heu... Oui !"
    alain "Ca fait un moment que l'huissier de justice nous appelle pour qu'on entre."
    e "Allons-y ! Crois en moi qui crois en toi !"
    
    scene black with dissolve
    $ renpy.pause(1.0)
    
    scene judge
    
    play music (courtroom) fadein 2
    j "Maintenant que la défense est enfin présente..."
    j "Je déclare la séance ouverte, pour le procès de Mr Alain Provist."
    j "La défense est-elle prête ?"
    
    # show courtroom_left:
        # xalign 0.5
    # show elusia normal:
        # xalign 0.5
    # show courtroom_right:
        # xalign 1.0 xanchor 0.0
    # show ryouzanki normal:
        # xalign 1.0 xanchor 0.0
    # with None
    
    show courtroom_left
    show elusia normal
    show courtroom_right at offscreenright
    show ryouzanki normal at offscreenright
    
    e "La défense est prête, votre honneur."
    
#    show courtroom_left:
#         xalign 0.0 xanchor 1.0
#    show elusia normal:
#         xalign 0.0 xanchor 1.0
#    show courtroom_right:
#         xalign 0.5
#    show ryouzanki normal:
#         xalign 0.5
#    with move

    show courtroom_left:
        offscreenleft
    show elusia normal:
        offscreenleft
    show courtroom_right:
        center
    show ryouzanki normal:
       center
    with move
    
    r "L'accusation est prête, votre honneur."
    
    scene judge
    
    j "La défense sera donc assurée par... Mlle ?"
    
    show courtroom_left
    show elusia normal
    
    e "Mlle Bravewill, votre honneur, Elusia Bravewill."
    
    scene judge
    
    j "Vous êtes nouvelle n'est-ce pas ?"
    j "Votre performance aujourd'hui décidera du destin de votre client."
    j "Serez vous à la hauteur ?"
    
    show courtroom_left
    show elusia explaining
    
    e "Vous le verrez par vous même, votre honneur !"
    
    scene judge
    
    j "Très bien. Dans ce cas..."
    j "Si l'accusation veut bien se donner la peine d'énoncer les charges à l'encontre de Mr Provist."
    
    scene courtroom_right
    show ryouzanki normal
    
    r "Avec grand plaisir votre honneur."
    
    scene witness_stand
    show alain normal
    show witness_bar
    
    r "Le suspect ici présent est accusé d'homicide sur la personne de Mr Goland."
    r "D'après les premiers éléments d'enquête, le suspect aurait poussé la victime d'un balcon."
    r "La victime était un brillant ingénieur en aéronautique célibataire vivant seul."
    r "Le rapport d'autopsie confirme que la mort est bien due à une chute du 4ème étage."
    r "Tous deux étaient logés dans le même hôtel de vacance Heaven Fall, dans des chambres adjacentes."
    r "Lorsque Mr Goland a été poussé de son balcon, les vacanciers de la chambre du dessous sont montés pour coincer le coupable."
    r "Mr Provist ici présent était l'unique personne à cet étage d'où son arrestation."
    
    scene judge
    
    j "Je vois. Et bien c'est un cas plutôt simple."
    j "Je déclare donc l'accusé..."
    
    show screen tuto_object
    e "(Elusia, tu ne peux pas le laisser finir sa phrase...)"
    e "(Vite, émets une objection !)"
    
label loop_tuto1:
    
    e "(Ce joli bouton qui vient d'appaître à gauche là !)"
    jump loop_tuto1
    
label tuto_object_end:
    
    hide screen tuto_object
    
    $ renpy.music.stop()
    show bubble_obj_elu
    play sound elusia_obj
    $ renpy.pause(0.5)

    show courtroom_left
    show elusia objection
    
    e "OBJECTION !"
    
    show courtroom_left:
        xalign 0.5
    show elusia explaining:
        xalign 0.5
    show courtroom_right:
        xalign 1.0 xanchor 0.0
    show ryouzanki normal:
        xalign 1.0 xanchor 0.0
    with None
    
    e "Votre honneur, ne faisons pas de conclusion hâtive."
    e "(Réfléchissons vite mais réfléchissons bien...)"
    
    menu:
        "Avancer la théorie du suicide.":
            e "Il aurait très bien pu s'agir d'un suicide."
        "Avancer la théorie de l'accident.":
            e "Il aurait très bien pu s'agir d'un accident."
            show courtroom_left:
                xalign 0.0 xanchor 1.0
            show elusia explaining:
                    xalign 0.0 xanchor 1.0
            show courtroom_right:
                xalign 0.5
            show ryouzanki normal:
                xalign 0.5
            with move
            r "Un accident sur une balustrade d' 1m30 ?"
            r "Quelqu'un a dû \"provoquer\" cet accident..."
            show courtroom_left:
                xalign 0.5
            show elusia down:
                xalign 0.5
            show courtroom_right:
                xalign 1.0 xanchor 0.0
            show ryouzanki normal:
              xalign 1.0 xanchor 0.0
            with move
            e "(Comment suis-je censé savoir ce genre de trucs moi ?)"
            e "(Je fais quoi maintenant ?)"
            menu:
                "Insister sur la théorie de l'accident.":
                    call influence(-5)
                    show elusia normal
                    e "Heu... Si je puis me permettre..."
                    e "Peut être que la victime s'entrainait pour faire acrobate dans un cirque ?"
                    show courtroom_left:
                        xalign 0.0 xanchor 1.0
                    show elusia normal:
                         xalign 0.0 xanchor 1.0
                    show courtroom_right:
                         xalign 0.5
                    show ryouzanki normal:
                        xalign 0.5
                    with move
                    r "Dois-je en conclure que vous vous entrainez pour faire clown dans un cirque ?"
                    show courtroom_left:
                        xalign 0.5
                    show elusia down:
                           xalign 0.5
                    show courtroom_right:
                            xalign 1.0 xanchor 0.0
                    show ryouzanki normal:
                        xalign 1.0 xanchor 0.0
                    with move
                    e "Et bien dans ce cas, il ne peut s'agir que d'un suicide !"
                    e "(Je n'ai plus le choix...)"
                "Se rabattre sur la théorie du suicide.":
                    show elusia normal
                    e "Et bien dans ce cas, il ne peut s'agir que d'un suicide !"
                   
        
    r "Ahem..."                
    show courtroom_left:
        xalign 0.0 xanchor 1.0
    show elusia normal:
        xalign 0.0 xanchor 1.0
    show courtroom_right:
        xalign 0.5
    show ryouzanki normal:
        xalign 0.5
    with move
    r "La victime était psychologiquement stable et sans problème."
    r "Tout lui réussissait dans la vie."
    r "Et aucune note de suicide n'a été retrouvée."
    show courtroom_left:
        xalign 0.5
    show elusia explaining:
        xalign 0.5
    show courtroom_right:
        xalign 1.0 xanchor 0.0
    show ryouzanki normal:
        xalign 1.0 xanchor 0.0
    with move
    e "Mais ça ne prouve pas qu'il ne l'a pas fait..."
    show elusia objection
    e "Et encore moins que mon client est coupable !"

    scene judge
    j "Oui, je n'avais pas vu cette éventualité. Est-ce que l'avocat général à quelque chose à répondre à cela ?"
    
    show courtroom_left:
        xalign 0.0 xanchor 1.0
    show elusia normal:
         xalign 0.0 xanchor 1.0
    show courtroom_right:
        xalign 0.5
    show ryouzanki normal:
        xalign 0.5
    with None
    
    r "Dîtes moi Bravewill... Un homicide n'est-il pas un cas un peu difficile à traiter pour débuter ?"
    r "Croyez moi, j'aurais aussi espéré pour vous que cela soit un suicide."
    
    show courtroom_left:
        xalign 0.5
    show elusia normal:
         xalign 0.5
    show courtroom_right:
        xalign 1.0 xanchor 0.0
    show ryouzanki normal:
        xalign 1.0 xanchor 0.0
    with move
    
    e "Dois-je en conclure que vous avez des preuves à l'appui ?"
    
    show courtroom_left:
        xalign 0.0 xanchor 1.0
    show elusia normal:
         xalign 0.0 xanchor 1.0
    show courtroom_right:
        xalign 0.5
    show ryouzanki normal:
        xalign 0.5
    with move
    
    r "Mais j'ai même mieux."
    show ryouzanki explaining
    r "Nous avons un témoin visuel direct de la scène du meutre !"
    r "L'accusation aimerait appeler son premier témoin à la barre."
    
    scene black with dissolve
    play music (courtroom) fadein 2
    $ renpy.pause(1.0)
    
    show witness_stand:
        xalign 0.5
    show lara normal:
        center
    show witness_bar:
        xalign 0.5
    show courtroom_right:
        xalign 1.0 xanchor 0.0
    show ryouzanki normal:
        xalign 1.0 xanchor 0.0
    with dissolve
    
    t1 "Bonjour."
    show lara worried with hpunch
    alain "LARA !"
    
    show witness_stand:
        xalign 0.0 xanchor 1.0
    show lara normal:
        xalign 0.0 xanchor 1.0
    show witness_bar:
        xalign 0.0 xanchor 1.0
    show courtroom_right:
        xalign 0.5
    show ryouzanki explaining:
        xalign 0.5
    with move
    
    r "Silence. Votre tour de parole viendra."
    show ryouzanki normal
    r "Témoin ! Veuillez décliner votre identité civile, votre âge et votre profession"
    
    show witness_stand:
        xalign 0.5
    show lara normal:
        xalign 0.5
    show witness_bar:
        xalign 0.5
    show courtroom_right:
        xalign 1.0 xanchor 0.0
    show ryouzanki normal:
        xalign 1.0 xanchor 0.0
    with move

    t1 "Je m'appelle Lara Tatouille et j'ai 28 ans. Je suis cuisinière dans un restaurant gastronomique."
    
    show witness_stand:
        xalign 0 xanchor 1.0
    show lara normal:
        xalign 0 xanchor 1.0
    show witness_bar:
        xalign 0 xanchor 1.0
    show courtroom_right:
        xalign 0.5
    show ryouzanki normal:
        xalign 0.5
    with move
    
    r "Je vois sur votre état civil que votre nom est Lara Provist."
    r "Avez vous une explication à cela ?"
    
    show witness_stand:
        xalign 0.5
    show lara normal:
        xalign 0.5
    show witness_bar:
        xalign 0.5
    show courtroom_right:
        xalign 1.0 xanchor 0.0
    show ryouzanki normal:
        xalign 1.0 xanchor 0.0
    with move
    
    t1 "Je... Je vais demander un divorce."
    t1 "Et je ne veux plus porter le nom d'un meurtrier."
    
    show witness_stand:
        xalign 0 xanchor 1.0
    show lara normal:
        xalign 0 xanchor 1.0
    show witness_bar: 
        xalign 0 xanchor 1.0
    show courtroom_right:
        xalign 0.5
    show ryouzanki normal:
        xalign 0.5
    with move
    
    r "Très bien. Nous verrons cela plus tard, veuillez faire votre déposition Mme Provist."
    
    scene black with dissolve
    $ renpy.pause(1.0)
    
    scene witness_stand:
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
    with dissolve
    
    t1 "Nous étions en vacances avec Alain dans un petit hôtel en montagne."
    t1 "Il est parti faire de la randonnée sans moi parce que j'étais fatiguée."
    t1 "Je discutais avec notre voisin de palier quand il est rentré ivre dans la chambre."
    show lara hit
    t1 "C'est alors que dans une rage sans raison, il s'est précipité sur la victime !"
    t1 "Il l'a poussé plusieurs fois en hurlant jusqu'à la rambarde d'où la victime est tombée."
    
    scene witness_stand:
        offscreenleft
    show lara hit:
        offscreenleft
    show witness_bar:
        offscreenleft
    show courtroom_right:
        center
    show ryouzanki normal:
        center
    with move
    
    r "Si la cour le permet, l'accusation aimerait présenter des pièces à conviction."
    r "Ces pièces à conviction épaulent plus ou moins la déposition précedante."
    scene A2 with fade
    r "Tout d'abord, le rapport d'autopsie indique que la victime est bien morte d'une chute."
    r "Une chute du 4ème étage pour être précis."
    scene A1 with fade
    r "Comme l'indique ce plan, la chambre du suspect est bel et bien située au 4ème étage de l'hôtel."
    r "Le couple Provist était bien voisin de palier avec Mr Golant."
    scene A4 with fade
    r "Voici une photo de la chambre du suspect."
    r "On y voit les traces de boues que le suspect a ramené de sa randonnée en montagne."
    scene A3 with fade
    r "Pour terminer -âmes sensibles, s'abstenir- , voici une photo prise par l'inspecteur Alizan, chargé de l'enquête."
    r "Il s'agit de la scène située en dessous du balcon de la chambre 404." 
    scene CG_thinking_anim with fade
    show CG_elusia_thinking with moveinleft
    nvl clear
    envl "Mmmh... Je n'ai pas eut le temps d'examiner ces preuves de très près..."
    show screen proof11button
    envl "Mais maintenant, je peux le faire à tout moment en cliquant sur l'onglet preuve en haut à gauche de l'écran."
    envl "Il me permet de regarder de plus près les preuves quand bon me semble..."
    envl "Lara... Elle ment probablement quelque part... Ou alors Alain serait un..."
    envl "Non, je ne dois pas y penser. Je dois \ntrouver la brèche dans ce témoignage \net enfoncer une preuve dedans !"
    nvl clear
    envl "Aller ma grande ! Montre leur que tu n'as pas passé toutes ses années sur les bancs de la fac pour rien !"
    envl "Il faut reprendre le témoignage à zéro. Je pourrais demander des précisions avec le bouton sur la droite de l'écran."
    envl "Et lorsque je verrais une faille dans le témoignage, je pourrais lancer une objection avec une preuve à l'appui."
    envl "Il faut que je réflechisse bien avant de \nlancer une objection..."
    envl "Je ne veux pas me ridiculiser devant \nle juge..."
    nvl clear
    envl "Une objection mal placée me ferait perdre de l'influence sur l'issue du procès."
    $ show_infl = True
    envl "L'influence que j'ai sur le procès est indiqué au dessus."
    envl "Je crois que j'ai tout en tête... C'est parti !"

    scene witness_stand:
        center
    show lara normal:
        center
    show witness_bar:
        center
    with fade
    
    call encounter

    play music (deposition) fadein 2
    
label dep11:

    $ try_objection = 0
    
    show screen testimony_scre11
    
    scene witness_stand:
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
    with dissolve
    
    $ witness_statement = 1
    t1 "Nous étions en vacances avec Alain dans un petit hôtel en montagne."
    
    $ witness_statement = 2
    t1 "Il est parti faire de la randonnée sans moi parce que j'étais fatiguée."
    
    $ witness_statement = 3
    
    if not ryou_attack_1:
        t1 "Je discutais avec notre voisin de palier quand il est rentré ivre dans la chambre."
    else:
        t1 "Je discutais avec notre voisin peu habillé quand il est rentré ivre dans la chambre."

    show lara hit
    
    $ witness_statement = 4
    t1 "C'est alors que dans une rage sans raison, il s'est précipité sur la victime !"
    
    $ witness_statement = 5
    t1 "Il l'a poussé plusieurs fois en hurlant jusqu'à la rambarde d'où la victime est tombée."

    hide screen testimony_scre11
    
    scene judge with fade
    
    j "Le témoignage convient-il à la défense ?"
    
    scene courtroom_left
    show elusia normal
    
    menu:
        "La défense n'a rien à répondre à cela.":
            scene courtroom_left:
                xalign 0.5
            show courtroom_right:
                xalign 1.0 xanchor 0.0
            show ryouzanki normal:
                xalign 1.0 xanchor 0.0
            show elusia normal
            e "La défense n'a rien à répondre à cela."
            show courtroom_left:
                xalign 0.0 xanchor 1.0
            show elusia normal:
                xalign 0.0 xanchor 1.0
            show courtroom_right:
                xalign 0.5
            show ryouzanki normal:
              xalign 0.5
            with move
            r "Vraiment ? Bravewill..."
            r "Si ce témoignage est validé, cela indique clairement que votre client est coupable."
            show courtroom_left:
                xalign 0.5
            show elusia down:
                xalign 0.5
            show courtroom_right:
                xalign 1.0 xanchor 0.0
            show ryouzanki normal:
                 xalign 1.0 xanchor 0.0
            with move
            e "Awawawa..."
            e "La... La défense désire réécouter une nouvelle fois la déposition."
            call influence(-5)
        "Non, J'ai dû rater quelque chose...":
            scene courtroom_left
            show elusia explaining
            e "Non, J'ai dû rater quelque chose..."
            e "Il y a encore quelque chose de suspicieux dans cette déposition."
            e "La défense désire réécouter une nouvelle fois la déposition."
            call influence(-2)
            
    jump dep11

    
label dep11end:
    
    scene judge with fade
    j "Qu'est-ce que cela signifie exactement Mlle Bravewill ?"
    scene courtroom_right:
        offscreenright
    show ryouzanki normal:
        offscreenright
    show courtroom_left:
        center
    show elusia normal:
        center
    with dissolve
    e "La défense pense que l'information suivante a été faussée :"
    menu:
        "Le lieu du crime.":
            e "Le lieu du crime, votre honneur."
            $ ryou_attack_2 = True
        "L'heure du crime.":
            e "L'heure du crime, votre honneur."
            
    show elusia explaining
    e "Si comme le dit Mme Provist, son mari s'est précipité et tué Mr Goland dès son retour..."
    e "Il ne se serait pas arrêté au milieu de la chambre pour aller retirer ses chaussures."
    show courtroom_right:
        center
    show ryouzanki explaining:
        center
    show courtroom_left:
        offscreenleft
    show elusia explaining:
        offscreenleft
    with move
    r "..."
    show ryouzanki normal
    r "L'accusation aimerait appeler Mr Provist à la barre afin d'écouter sa version des faits."
    show judge with dissolve
    j "C'est soudain. La défense désire-t'elle quelques minutes afin de préparer Mr Provist ?"
    show courtroom_left at center
    show elusia normal at center
    hide judge with dissolve
    $ choix1 = True
    $ choix2 = True
    $ choix3 = True
    $ choix4 = True #ivre ?
    $ choix5 = True #vu goland ?
    $ choix6 = True #spyed ?
    menu:
        "Ce ne sera pas nécessaire.":
            show elusia explaining
            call influence(5)
            e "Ce ne sera pas nécessaire."
            e "La défense est prête et l'innocence de mon client le protègera."
            show courtroom_right:
                center
            show ryouzanki explaining:
                center
            show courtroom_left:
                offscreenleft
            show elusia explaining:
                offscreenleft
            with move
            r "Tant d'assurance..."
            show ryouzanki normal
            r "Ce sera un réel plaisir à l'écraser..."
            jump interro11
        "Volontier votre honneur.":
            e "Volontier votre honneur."
    
    play music (recession) fadein 2
    
    scene waiting
    show alain panick
    with fade
    alain "Il va m'interroger ?!"
    
    e "Ne t'inquiète pas, je vais t'aider à te défendre."
    show courtroom_right sepia
    show ryouzanki explaining sepia
    with fade
    e "Cet homme..."
    nvl clear
    show CG_thinking_anim with fade
    show CG_elusia_thinking with moveinleft
    envl "Il a une idée derrière la tête..."
    envl "Peut être qu'il sait des choses sur mon client."
    envl "Des choses gênantes qu'Alain me cache."
    envl "Il faut que je connaisse toute la vérité afin de mieux le défendre."
    envl "Si Alain est innocent, je ne vois pas pourquoi \nil ferait une telle chose."
    nvl clear
    envl "Quoi qu'il en soit, il faut que je prépare Alain."
    envl "Je dois lui indiquer à quelles questions il peut répondre..."
    envl "Et lui parler de son droit au silence."
    envl "En effet, la justice ne peut forcer une\npersonne à témoigner contre elle même."
    envl "Je dois garder en tête qu'un silence est très suspiscieux aussi et donc ne pas en abuser."
    nvl clear
    
    scene waiting
    show alain normal
    with fade
    
    e "Alain..."
    menu:
        "J'ai confiance en toi.":
            call influence(5)
            e "J'ai confiance en toi."
            alain "Merci..."
            alain "Moi aussi j'ai confiance en toi."
        "Me cacherais tu des choses ?":
            e "Me cacherais tu des choses ?"
            show alain panick
            alain "Mais non ! Qu'est-ce qui te fais croire ça ?"
            e "Intuition... Féminine ?"
            alain "Je ne te cache rien Elusia..."
    show alain normal
    alain "A ce propos..."
    alain "Tu t'es super bien débrouillé contre Lara..."
    e "Oh, merci."
    alain "Par où on commence ?"
label preparatif_int_1:
    menu:
        "Le témoignage de Lara" if choix1:
            $ choix1 = False
            e "A propos du témoignage de Lara..."
            e "Est-ce vrai que tu étais ivre ?"
            alain "Oui. Lara n'a pas arrêté de m'emmerder toute la journée."
            alain "Je voulais que l'on parte en vacance ensemble pour se réconcilier."
            alain "Et la pluie est venue pourrir mon dernier petit plaisir."
            alain "Comprends moi, j'avais besoin de décompresser..."
            e "Alain... Je ne suis pas là pour te juger..."
            e "Si le procureur te pose la question..."
            menu:
                "Ne répond pas que tu étais ivre.":
                    $ choix4 = False
                    e "Ne répond pas que tu étais ivre."
                "Dis la vérité.":
                    e "Dis la vérité."
            alain "D'accord."
        "La victime" if choix2:
            $ choix2 = False
            e "La victime..."
            e "Est-ce que tu la connaissais ? Au moins de vue ?"
            alain "J'ai dû la croiser une ou deux fois sans lui parler."
            menu:
                "Tu peux le dire...":
                    e "Tu peux le dire..."
                    e "Je ne pense pas que cela nous soit préjudiciable."
                "Dis que tu ne l'as jamais vu.":
                    $ choix5 = False
                    e "Dis que tu ne l'as jamais vu."
                    e "Ce sera plus simple."
            alain "D'accord."
        "Ce que tu as vu." if choix3:
            $ choix3 = False
            e "A propos de ce que tu as vu..."
            e "Attends une minute mais... Qu'as tu vu en entrant exactement ?"
            alain "Quand je suis rentré, on s'est disputé. Il n'y avait personne d'autre."
            e "Mais alors tu n'as pas vu la victime ?"
            show alain panick
            alain "Mais non ! Tout ce qu'a dit Lara..."
            show alain normal
            alain "Ce n'est qu'un tissu de mensonge."
            e "Je vois... Dis moi Alain..."
            e "Est-ce que... Est-ce que tu savais que ta femme..."
            alain "Ce n'est plus important..."
            menu:
                "Insister.":
                    e "Alain... Je dois savoir."
                    alain "Je l'aimais. Je suis parti plus loin sur le versant."
                    alain "Je voulais qu'elle me voit sous la pluie la regarder au loin."
                    alain "Mais en regardant dans notre chambre, j'ai vu deux personnes."
                    e "Alain. C'est très important ce que tu viens de me dire."
                    menu:
                        "Il faut le cacher.":
                            $ choix6 = False
                            e "Il faut le cacher."
                            e "Ca ne joue pas en notre faveur."
                            alain "Je comprends."
                        "Il faudra dire la vérité.":
                            e "Il faudra dire la vérité."
                            e "Je sais que c'est dur mais il le faut."
                            alain "Je comprends."
                "Laisser.":
                    e "Très bien. Je n'insiste pas."
                    alain "Merci..."
        "Nous sommes prêts.":
            e "Nous sommes prêts."
            e "Bonne chance Alain ! Je suis avec toi !"
            jump interro11
    jump preparatif_int_1
label interro11:
    stop music fadeout 1.0
    scene judge with fade
    j "Très bien, puisque la défense est prête, je ne vois aucune raison d'attendre."
    
    scene courtroom_right:
        offscreenright
    show ryouzanki normal:
        offscreenright
    show courtroom_left:
        offscreenleft
    show elusia normal:
        offscreenleft
    show witness_stand:
        center
    show alain normal:
        center
    show witness_bar:
        center
    with fade
    
    call encounter
    play music (deposition) fadein 2
    alain "Je suis parti en vacance avec ma femme dans l'espoir que l'on s'aime à nouveau."
    
    show courtroom_right:
        center
    show ryouzanki normal:
        center
    show witness_stand:
        offscreenleft
    show alain normal:
        offscreenleft
    show witness_bar:
        offscreenleft
    with move
    r "Vous admettez donc que votre couple était au plan mort ?"
    show courtroom_right:
        offscreenright
    show ryouzanki normal:
        offscreenright
    show witness_stand:
        center
    show alain normal:
        center
    show witness_bar:
        center
    with move
    alain "Oui. C'était trop tard. Elle ne m'aimait plus."
    alain "Elle s'est contenté de pourrir ma moindre tentative."
    show courtroom_right:
        center
    show ryouzanki normal:
        center
    show witness_stand:
        offscreenleft
    show alain normal:
        offscreenleft
    show witness_bar:
        offscreenleft
    with move
    r "Et vous avez bu pour oublier ?"
    show courtroom_right:
        offscreenright
    show ryouzanki normal:
        offscreenright
    show witness_stand:
        center
    show alain normal:
        center
    show witness_bar:
        center
    with move
    alain "Heu... Je..."
    if choix4:
        alain "Oui, j'ai bu avant de rentrer."
        alain "Une bonne heure au bar de l'hôtel."
    else:
        alain "Non, juste un petit verre au bar de l'hôtel."
        alain "Pas assez pour être ivre."
        
    show courtroom_right:
        center
    show ryouzanki normal:
        center
    show witness_stand:
        offscreenleft
    show alain normal:
        offscreenleft
    show witness_bar:
        offscreenleft
    with move
    r "Je vois."
    r "Aviez vous déjà vu Mr Goland avant ?"
    show courtroom_right:
        offscreenright
    show ryouzanki normal:
        offscreenright
    show witness_stand:
        center
    show alain normal:
        center
    show witness_bar:
        center
    with move
    alain "Et bien..."
    if choix5:
        alain "Oui, je l'ai croisé quelques fois."
        alain "Mais on ne s'est jamais adressé la parole."
    else:
        alain "Non, je ne l'ai jamais vu de ma vie."
        alain "Même maintenant, je ne sais pas à quoi il ressemble."
    alain "Je ne l'ai pas vu en entrant dans la chambre."
    show courtroom_right:
        center
    show ryouzanki normal:
        center
    show witness_stand:
        offscreenleft
    show alain normal:
        offscreenleft
    show witness_bar:
        offscreenleft
    with move
    r "Une dernière chose Mr Provist..."
    show ryouzanki explaining
    r "Que faisiez vous dans la montagne seul et avec un temps pareil ?"
    show courtroom_right:
        offscreenright
    show ryouzanki normal:
        offscreenright
    show witness_stand:
        center
    show alain normal:
        center
    show witness_bar:
        center
    with move
    alain "Je ne..."
    if choix6:
        alain "Je... J'espionnais ma femme depuis l'autre versant de montagne."
        show courtroom_left:
            center
        show elusia down:
            center
        show witness_stand:
            offscreenright
        show alain normal:
            offscreenright
        show witness_bar:
            offscreenright
        with move
        e "Awawa... Ce n'est pas ce qui était prévu..."
    else:
        alain "Je prennais l'air pour me changer les idées."
        alain "La montagne me réussis habituellement."
    
    stop music fadeout 1.0
    scene courtroom_right
    show ryouzanki normal
    with fade
    r "Votre honneur, l'accusation désire clore cet interrogatoire."
    show judge with dissolve
    j "Déjà ? Le témoignage vous convient-il donc ?"
    j "Rien ne vous dérange ?"
    hide judge with dissolve
    r "La question serait plutôt ce qui ne me dérange pas."
    show ryouzanki explaining
    r "Ce témoignage chante si faux que j'en ai la migraine."
    r "Tout d'abord, l'accusation désire exposer sa version des faits."
#    scene courtroom_right sepia
#    show ryouzanki explaining sepia
#    with dissolve
#    nvl clear
#    show elusia_grey
#    envl "Il semblerait que la défense d'Alain n'était pas très satisfaisante..."
#    envl "Le procureur a probablement sa théorie."
#    envl "Je ne dois pas le laisser la présenter tranquillement ou c'en est fini de nous !"
#    envl "Des objections bien placées sur les failles de sa théorie devraient nous faire gagner un peu d'influence..."
#    hide elusia_grey with dissolve
    show ryouzanki normal
    show courtroom_right
    show courtroom_left:
        offscreenleft
    show elusia objection:
        offscreenleft
    play music clash fadein 1.0
#    $ witness_statement = 1
    r "Le suspect n'a même pas passé de temps avec sa femme."
#    $ witness_statement = 
    r "Ces \"vacances\" n'étaient qu'un pretexte pour l'emmener dans un endroit avec moins de monde."
#    $ witness_statement = 
    r "Car il serait ainsi plus aisé d'identifier et d'éliminer l'amant de sa femme."
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
        r "Le suspect a lui même avoué qu'il espionnait sa femme !"
        call influence(-4)
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
    
    show ryouzanki normal
    r "Par la suite, il a fait semblant de s'absenter."
    r "Qui de sain d'esprit irait faire de la randonnée sous la tempête ?"
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
    r "Il est rentré ivre après avoir bu pour se donner du courage pour son crime."
    r "Il aurait pu tuer son rival sans scrupule."
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
        r "Son taux d'alcolémie relevé à son arrestation le prouve !"
        call influence(-8)
    else:
        e "Il noyait son chagrin d'amour !"
        e "Boire et tuer une personne sont indépendants !"
        show elusia explaining
        e "La défense aimerait que l'accusation cesse ses conjectures frauduleuses."
        call influence(10)

    show courtroom_right:
        center
    show ryouzanki normal:
        center
    show courtroom_left:
        offscreenleft
    show elusia explaining:
        offscreenleft
    with move
    r "En entrant dans la chambre, il a tout de suite compris ce qu'il se passait."
    r "C'est pourquoi il a couru sur la victime avec des intentions belliqueuses."
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
    show courtroom_right:
        center
    show ryouzanki normal:
        center
    show courtroom_left:
        offscreenleft
    show elusia:
        offscreenleft
    with move
    r "Le suspect ment aussi sur sa relation avec la victime."
    r "Leurs deux noms sont sur la liste du club d'escalade de l'hôtel."
    r "Autrement dit, ils auraient dû passer 5 après-midis ensemble."
    if not choix5:
        show ryouzanki objection
        r "Il est impossible que le suspect n'ait jamais vu la victime !"
        call influence(-10)
        show ryouzanki normal
    else:
        r "Ils auraient très bien pu faire connaissance a ce moment là !"
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
    r "J'espère que vous tenez le coup Bravewill..."
    show ryouzanki explaining
    r "Vous tenez tant à vos preuves."
    show ryouzanki objection
    r "Il se trouve que j'en ai !"
    r "La police a relevé des empreintes digitales de Mr Provist sur la poignée de porte de la chambre de la victime !"
    show courtroom_right:
        offscreenright
    show ryouzanki normal:
        offscreenright
    show courtroom_left:
        center
    show elusia down:
        center
    with hpunch
    e "Awawawa... Comment est-ce possible ?!"
    show elusia normal
    e "(Un instant... Qu'est ce que ça veut dire ?)"
    menu:
        "Ce n'est pas le lieu du crime !":
            show elusia objection
            e "Ce n'est pas le lieu du crime !"
            e "Cette preuve n'est pas pertinente !"
            if ryou_attack_2:
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
                r "Elle l'est !"
                r "La défense a prouvé précédemment que la scène du crime n'était pas la chambre 404 !"
                show ryouzanki explaining
                r "Cette preuve indique que la scène du crime est la chambre d'à côté."
                r "Et que le suspect y était."
                call influence(-10)
            else:
                scene courtroom_right:
                    center
                show ryouzanki normal:
                    center
                show courtroom_left:
                    offscreenleft
                show elusia objection:
                    offscreenleft
                with move
                r "Elle prouve quand même que le suspect et la victime se connaissaient."
                r "De plus, l'accusation aimerait prendre en considération la possibilité que le lieu du crime soit erroné."
                call influence(3)
        "...":
            show elusia down
            e "(C'est pas bon du tout...)"
    scene judge
    j "Si l'on admet que le lieu du crime soit la chambre de la victime..."
    j "Qu'est-ce qui change exactement ?"
    
    return