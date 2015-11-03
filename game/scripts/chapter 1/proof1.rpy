screen testimony_scre12:

    $ ui.imagebutton("medias/interface/objection.png", "medias/interface/objection.png", yalign = 0.5, clicked=[Jump("aiguillage12")])
    
screen testimony_scre11:

    $ ui.imagebutton("medias/interface/objection.png", "medias/interface/objection.png", yalign = 0.5, clicked=[Jump("proof_selector11")])
    $ ui.imagebutton("medias/interface/press.png", "medias/interface/press.png", yalign = 0.5, xalign = 1.0, clicked=[Jump("press11")])
  
label proof_selector11:
    
    hide screen testimony_scre11
    
    # trop kikoo ? :s
    
    #show CG_thinking
    #show CG_elusia_thinking with moveinleft
    
    call screen proof_select11
    
screen proof_select11:
    
    grid 5 1:
        xalign 0.5
        yalign 0.5
        $ ui.imagebutton("medias/interface/MA1.png", "medias/interface/MA1.png",  clicked=[SetVariable("try_objection",1),Jump("aiguillage11")])
        $ ui.imagebutton("medias/interface/MA2.png", "medias/interface/MA2.png",  clicked=[SetVariable("try_objection",2),Jump("aiguillage11")])
        $ ui.imagebutton("medias/interface/MA3.png", "medias/interface/MA3.png",  clicked=[SetVariable("try_objection",3),Jump("aiguillage11")])
        $ ui.imagebutton("medias/interface/MA4.png", "medias/interface/MA4.png",  clicked=[SetVariable("try_objection",4),Jump("aiguillage11")])
        $ ui.imagebutton("medias/interface/return.png", "medias/interface/return.png",  clicked=Jump("dep11"))
        
label aiguillage12:
    
    if (witness_statement == 1):
        jump object1_2_1
    elif (witness_statement == 2):
        jump object1_2_2
    elif (witness_statement == 3):
        jump object1_2_3
    elif (witness_statement == 4):
        jump object1_2_4
    elif (witness_statement == 5):
        jump object1_2_5
    else:
        "ERREUR AIGUILLAGE OBJECTION 2"
      
      
label aiguillage11:
    
    hide CG_thinking
    hide CG_elusia_thinking
    $ renpy.music.stop()
    show bubble_obj_elu
    play sound elusia_obj
    $ renpy.pause(0.5)
    scene courtroom_left
    show elusia objection
    
    e "OBJECTION !"
    
    if (witness_statement == 1):
        jump object1_1_1
    elif (witness_statement == 2):
        jump object1_1_2
    elif (witness_statement == 3):
        jump object1_1_3
    elif (witness_statement == 4):
        jump object1_1_4
    elif (witness_statement == 5):
        jump object1_1_5
    else:
        "ERREUR AIGUILLAGE OBJECTION"

screen proof11button:
    
   $ ui.imagebutton("medias/interface/proof.png", "medias/interface/proof.png", clicked=ShowMenu("proof11"))

init python:

    proof11 = Gallery()

    proof11.button("MA1")
    proof11.image("A1")
    
    proof11.button("MA2")
    proof11.image("A2")    
    
    proof11.button("MA3")
    proof11.image("A3")    
    
    proof11.button("MA4")
    proof11.image("A4")
    
    proof11.transition = dissolve

screen proof11:

    tag menu
    add "CG_thinking_anim"

    grid 5 1:

        xfill True
        
        yalign 0.5
        # yfill True

        add proof11.make_button("MA1", "MA1", xalign=0.5, yalign=0.5)
        add proof11.make_button("MA2", "MA2", xalign=0.5, yalign=0.5)
        add proof11.make_button("MA3", "MA3", xalign=0.5, yalign=0.5)
        add proof11.make_button("MA4", "MA4", xalign=0.5, yalign=0.5)

        vbox xalign 0.5 yalign 0.5:
            textbutton "Retour" action Return() xalign 0.5 yalign 0.5
