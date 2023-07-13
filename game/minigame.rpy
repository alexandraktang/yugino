define a = Character("Amina", color ="#660e60")
define p = Character("Paya", color = "#9f9393")

image card_back = "card_back.png"

define e = Character("")

init python:
    def drag_placed(drags, drop):
        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        return True

# The game starts here.

label minigame:

    scene cardgame_background

    show screen drag_sample1A
    e ""
    show screen drag_sample1B
    e ""
    
    hide screen drag_sample1A
    hide screen drag_sample1B
    call screen drag_sample2


    show screen drag_sample3
    if droppable == "Left Card Back":
        $ xpos_var = 150
    elif droppable == "Right Card Back":
        $ xpos_var = 790
    else:
        $ xpos_var = 640
    if draggable == "Amina":
        show Amina:
            xpos xpos_var ypos 460
    elif draggable == "Enemy":
        show Enemy:
            xpos xpos_var ypos 460
    elif draggable == "Card Front":
        show Card Front:
            xpos xpos_var ypos 460
    #e "{color=#000}{vspace=75}TEXT HERE{/color}"
    e "The [draggable] was put in [droppable]"



    # This ends the game.

    return

screen drag_sample1A:
    fixed:
        drag:
            xpos 0.25
            ypos 0.25
            drag_raise True
            draggable True
            frame:
                xpadding 20
                ypadding 20
                text "Draggable"
        drag:
            xpos 0.5
            ypos 0.25
            drag_raise True
            draggable True
            frame:
                xpadding 20
                ypadding 20
                text "Draggable"
        drag:
            xpos 0.75
            ypos 0.25
            drag_raise True
            draggable True
            frame:
                xpadding 20
                ypadding 20
                text "Draggable"

screen drag_sample1B:
    draggroup:
        drag:
            xpos 0.25
            ypos 0.25
            draggable True
            drag_raise True
            frame:
                xpadding 20
                ypadding 20
                text "Draggable"
        drag:
            xpos 0.5
            ypos 0.25
            draggable True
            drag_raise True
            frame:
                xpadding 20
                ypadding 20
                text "Draggable"
        drag:
            xpos 0.75
            ypos 0.25
            draggable True
            drag_raise True
            frame:
                xpadding 20
                ypadding 20
                text "Draggable"

screen drag_sample2:
    draggroup:
        drag:
            drag_name "Amina"
            child "card_amina.png"
            xpos 100
            ypos 100
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Enemy"
            child "card_enemy.png"
            xpos 400
            ypos 100
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Card Front"
            child "card_front.png"
            xpos 700
            ypos 100
            draggable True
            droppable True
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Left Card Back"
            xpos 0.1
            ypos 0.6
            child "card_back.png"
            draggable False
            droppable True
        drag:
            drag_name "Right Card Back"
            xpos 0.6
            ypos 0.6
            child "card_back.png"
            draggable False
            droppable True


screen drag_sample3:
    draggroup:
        drag:
            drag_name "Left Card Back"
            xpos 0.1
            ypos 0.6
            child "card_back.png"
            draggable False
            droppable False
        drag:
            drag_name "Right Card Back"
            xpos 0.6
            ypos 0.6
            child "card_back.png"
            draggable False
            droppable False