init python:

    proof1 = Gallery()

    proof1.button("knife")
    proof1.image("knife1")
    
    proof1.button("spoon")
    proof1.image("spoon1")

    proof1.button("gun")
    proof1.condition("gun_seen")
    proof1.image("gun1")
    
    
    proof1.transition = dissolve

screen proof1:

    tag menu
    add "white"

    grid 4 1:

        xfill True
        yfill True

        add proof1.make_button("knife", "knife", xalign=0.5, yalign=0.5)
        add proof1.make_button("spoon", "spoon", xalign=0.5, yalign=0.5)
        add proof1.make_button("gun", "gun", xalign=0.5, yalign=0.5)

        vbox xalign 0.5 yalign 0.5:
            textbutton "Retour" action Return() xalign 0.5 yalign 0.5
