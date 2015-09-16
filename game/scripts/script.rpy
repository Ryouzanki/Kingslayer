#### Ce fichier contient le code principal ####


label start:

    show courtroom_left:
        xalign 0.5
    show courtroom_right:
        xalign 1.0 xanchor 0.0        # Partie droite de l'image en hors champ
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

    return
