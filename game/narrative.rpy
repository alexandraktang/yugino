# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Amina", color ="#660e60")
define p = Character("Paya", color = "#9f9393")
define r = Character("River", color = "#b1734f") 

image river placeholder = "river_placeholder.png"
image river happy = "river_happy.png"
image river sad = "river_sad.png"

image amina placeholder = "amina_placeholder.png"
image amina happy = "amina_happy.png"
image amina sad = "amina_sad.png"

image paya placeholder = "paya_placeholder.png"
image paya happy = "paya_happy.png"
image paya sad = "paya_sad.png"
image paya sweatdrop = "paya_sweatdrop.png"
image paya love = "paya_love.png"
image paya shock = "paya_shock.png"
image paya confused = "paya_confused.png"
image paya tired = "paya_tired.png"

#defining image position states here
transform center:
    xalign 0.5
    yalign 0.5

transform leftcenter:
    xalign 0.0
    yalign 0.5

transform rightcenter:
    xalign 1.0
    yalign 0.5

# The game starts here.

label narrative:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene outside_school

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "..." "Hey Paya? Earth to Paya!"

    scene classroom
    with dissolve

    pause 0.5
    
    show river placeholder at center
    with dissolve 

    r "Hey, are you in there? It's your turn."

    show river placeholder at rightcenter
    with move

    show paya tired at leftcenter
    with dissolve

   
    p "Ahh, sorry River! I must have been spacing out again."

    show river happy
    with dissolve
    
    r "Leave it to you to start falling asleep in the middle of a game."

    hide river
    show paya sweatdrop at center
    with dissolve

    "Yeah, that's me, all right. Paya, the 22 year old college student who spaces even in my favorite card game."
    "My best friend River found this game NAME OF CARD GAME HERE a few months ago and now it seems like everyone's playing it!"
    "Though, I think for us, it's honestly just been nice to have a fun way to destresss from everything else we have going on lately."