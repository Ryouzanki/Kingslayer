#### Ce fichier gère l' UI commune  ####

screen menu_base:
    
    $ ui.imagebutton("medias/interface/menu.png", "medias/interface/menu.png", xalign = 1.0, clicked=ShowMenu("preferences"))
    
screen diff_imagemap:
    imagemap:
        auto "medias/interface/diff_%s.png"
        
        hotspot (100, 366, 400, 600) action Return("easy")
        hotspot (400, 366, 700, 600) action Return("hard")

        
screen button:
    
    $ ui.imagebutton("medias/interface/menu.png", "medias/interface/menu.png", xalign = 1.0, clicked=ShowMenu("preferences"))
    $ ui.imagebutton("medias/interface/proof.png", "medias/interface/proof.png", clicked=ShowMenu("proof1"))

screen testimony_scre:

    $ ui.imagebutton("medias/interface/objection.png", "medias/interface/objection.png", yalign = 0.5, clicked=[Jump("proof_selector")])
    $ ui.imagebutton("medias/interface/press.png", "medias/interface/press.png", yalign = 0.5, xalign = 1.0, clicked=[Jump("press_test")])
    
label proof_selector:
    
    hide screen testimony_scre
    
    # trop kikoo ? :s
    
    #show CG_thinking
    #show CG_elusia_thinking with moveinleft
    
    call screen proof_select
    
screen proof_select:
    
    grid 3 1:
        xalign 0.5
        yalign 0.5
        $ ui.imagebutton("medias/interface/knife.png", "medias/interface/knife.png",  clicked=[SetVariable("try_objection",1),Jump("aiguillage")])
        $ ui.imagebutton("medias/interface/spoon.png", "medias/interface/spoon.png",  clicked=[SetVariable("try_objection",2),Jump("aiguillage")])
        $ ui.imagebutton("medias/interface/gun.png", "medias/interface/gun.png",  clicked=[SetVariable("try_objection",3),Jump("aiguillage")])
        
label aiguillage:
    
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
        jump object_1_X
    else:
        jump object_2_X
    
            
screen say:

    # Valeurs par défaut de 'side_image' et 'two_window'
    default side_image = None
    default two_window = False

    # Options selon le que l'on soit en mode une fenêtre ou deux fenêtres.
    if not two_window:

        # Cas avec une fenêtre.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # Cas avec deux fenêtres.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # Si il y a une image latérale, on la montre au dessus du texte.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Utilisation du menu rapide.
    use quick_menu


##############################################################################
# Choix
#
# Écran utilisé pour les menus au sein du jeu
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Entrée
#
# Écran utilisé lors de l'utilisation de renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Écran utilisé pour les dialogues et les menus en mode NVL
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Affiche un dialogue
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Affiche un menu si il y en a un
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Menu principal
#
# Écran utilisé pour le menu principal, quand Ren'Py démarre
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # Pour être sûr que tout autre menu est remplacé
    tag menu
    
    imagemap:
        auto "medias/interface/mm_%s.png"
        hotspot (5, 400, 170, 600) action Start()
        hotspot (175, 400, 345, 600) action ShowMenu("load")
        hotspot (350, 400, 525, 600) action ShowMenu("preferences")
        hotspot (530, 400, 658, 600) action NullAction()
        hotspot (659, 400, 780, 600) action Quit(confirm=False)

init -2 python:

    # Donne la même taille à tous les boutons du menu.
    style.mm_button.size_group = "mm"


##############################################################################
# Navigation
#
# Écran inclue dans d'autres écrans pour afficher le menu jeu,  
# et le fond.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # Fond du menu jeu
    window:
        style "gm_root"

    # Boutons de navigation.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Retour") action Return()
        textbutton _("Option") action ShowMenu("preferences")
        textbutton _("Sauvegarder partie") action ShowMenu("save")
        textbutton _("Charger partie") action ShowMenu("load")
        textbutton _("Menu principal") action MainMenu()
        textbutton _("Quitter") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"


##############################################################################
# Sauvegarder, Charger
#
# Écrans permettant à l'utilisateur de sauvegarder ou charger un jeu
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Puisque la sauvegarde et le chargement sont deux actions proches
# nous utilisons un seul écran pour les deux. On utilise un l'écran
# file_picker depuis les écrans de sauvegarde et et de chargement.

screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # Les boutons en haut permettent à l'utilisateur
        # de sélectionner une page de fichiers.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Affiche une grille d'emplacements de sauvegarde
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Montre dix emplacements, numérotés de 1 à 10.
            for i in range(1, columns * rows + 1):

                # Chaque emplacement est un bouton.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Ajoute un screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save:

    # Pour être sûr que tout autre menu est remplacé.
    tag menu

    use navigation
    use file_picker

screen load:

    # Pour être sûr que tout autre menu est remplacé.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)



##############################################################################
# Préférences
#
# Écran permettant à l'utilisateur de changer les préférences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    # Inclus la navigation.
    use navigation

    # Met les colonnes de navigation dans une grille de largeur 3.
    grid 3 1:
        style_group "prefs"
        xfill True

        # Colonne de gauche.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Menu Oui/Non
#
# Écran proposant à l'utilisateur une question oui ou non
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Clic droit ou échap pour "non"
    key "game_menu" action no_action

init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5
    style.yesno_label_text.layout = "subtitle"


##############################################################################
# Menu rapide
#
# Écran inclus par défaut pour les dialogues, ajoutant un accès rapide à 
# plusieurs fontions utiles
screen quick_menu:

    # Ajoute un menu rapide au sein du jeu
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Prefs") action ShowMenu('preferences')

init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
