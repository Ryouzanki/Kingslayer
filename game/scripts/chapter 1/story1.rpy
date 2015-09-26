###  Fichier contenant le tronc de l'enquete  ###

label chap1:
    
    scene waiting with dissolve
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
    
    j "Maintenant que la défense est enfin présente..."
    j "Je déclare la séance ouverte, pour le procès de Mr Alain Provist."
    j "La défense est-elle prête ?"
    
    
    show courtroom_left:
        xalign 0.5
    show elusia normal:
        xalign 0.5
    show courtroom_right:
        xalign 1.0 xanchor 0.0
    show ryouzanki explaining:
        xalign 1.0 xanchor 0.0
    with None
    
    
    e "La défense est prête, votre honneur."
    
    show courtroom_left:
        xalign 0.0 xanchor 1.0
    show elusia normal:
         xalign 0.0 xanchor 1.0
    show courtroom_right:
        xalign 0.5
    show ryouzanki explaining:
        xalign 0.5
    with move
    
    r "L'accusation est prête, votre honneur."
    
    scene judge
    
    j "La défense sera donc assurée par... Mlle ?"
    
    show courtroom_left
    show elusia normal
    
    e "Elusia Bravewill, votre honneur."
    
    scene judge
    
    j "Vous êtes nouvelle n'est-ce pas ?"
    j "Serez vous à la hauteur ?"
    
    show courtroom_left
    show elusia explaining
    
    e "Vous le verrez pas vous même, votre honneur !"
    
    scene judge
    
    j "Très bien. Dans ce cas..."
    j "Si l'accusation veut bien se donner la peine d'énoncer les charges à l'encontre de Mr Provist."
    
    scene courtroom_right
    show ryouzanki explaining
    
    r "Avec grand plaisir votre honneur."
    
    return
