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
