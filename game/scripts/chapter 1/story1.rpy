###  Fichier contenant le tronc de l'enquete  ###

screen tuto_object:

    $ ui.imagebutton("medias/interface/objection.png", "medias/interface/objection.png", yalign = 0.5, clicked=[Jump("tuto_object_end")])
    
label chap1:
    
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
    r "Lorsque Mr Berthold a été poussé de son balcon, les vacanciers de la chambre du dessous sont montés pour coincer le coupable."
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
            r "Quelqu'un a du \"provoquer\" cet accident..."
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
        xalign 0.5
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
    envl "Non, je ne dois pas y penser. Je dois \ntrouver la brèche dans ce témoignage \net enfoncer une preuvce dedans !"
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
    envl "Je crois que j'ai tout en tête... C'est partit !"
    
    
    

    
    return
