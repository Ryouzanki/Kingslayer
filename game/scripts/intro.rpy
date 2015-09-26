###   Introduction du jeu   ###

label intro:
    
    # TODO
    scene black with dissolve
    show text "{b}{i}Fiat justicia pereat mundus{/i}{/b} \n\n       (Ferdinand 1er)" with dissolve
    $ renpy.pause(3.0)
    
    play music (intro) fadein 2
    scene CG_thinking_anim with fade
    show CG_elusia_thinking with moveinleft
    envl "Je m'appelle Elusia Bravewill."
    envl "Depuis toute petite, j'ai toujours été très férue de justice."
    envl "C'est pourquoi, j'avais décidé de devenir \navocate au barreau."
    envl "Afin de défendre les faibles des injustices !"
    envl "J'accomplie enfin mon rêve de paladin des \ntemps modernes..."
    envl "Enfin, si seulement c'était aussi simple \nque ça..."
    nvl clear
    show CG_elusia_thinking
    envl "Ca faisait bientot 6 mois que j'avais ouvert mon cabinet."
    envl "Et toujours pas de client."
    envl "Quand \"il\" est arrivé."
    envl "Je n'espérais pas le revoir dans ce genre \de circonstance mais..."
    envl "Le destin en avait décidé autrement."
    envl "C'est ainsi que commença ma carrière,\navec ce premier procès !"
    nvl clear
    
    scene black with dissolve
    stop music fadeout 1.0
    $ renpy.pause(1.0)
    
    #show screen button
    
    return
