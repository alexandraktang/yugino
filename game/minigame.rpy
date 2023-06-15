init python:
    def icons_update():
        pass

    def icons_events():
        pass

transform half_size: # halving resolution for background
    zoom 0.5

label setup_icons:
    python:
        for i in range(grid_size):
            rand_image = icon_images[renpy.random.randint(0,4)]
            idle_path = "Icons/{}.png".format(rand_image)
            hover_path = "Icons/{}_hover.png".format(rand_image)
            idle_image = Image(idle_path)
            hover_image = Image(hover_path)
            icons_list.append(icons.create(Transform(child = idle_image, zoom = 0.5)))

            icons_list[-1].index = i
            icons_list[-1].icon_type = rand_image
            icons_list[-1].idle_image = idle_image
            icons_list[-1].hover_image = hover_image

    call screen SameGame

screen SameGame:
    $frame_xsize = (icons_per_row * icon_size) + (icons_per_row * icon_padding) + icon_padding + 4
    $frame_ysize = ((grid_size / icons_per_row) * icon_size) + ((grid_size / icons_per_row) * icon_padding) + icon_padding + 4

    frame:
        background "#ffffff50"
        xalign 0.2
        yalign 0.5
        xsize frame_xsize
        ysize frame_ysize

        $crow = 0
        $ccolumn = 0

        for i in range(grid_size):
            $xp = (icon_size * ccolumn) + (icon_padding * ccolumn)
            $yp = (icon_size * crow) + (icon_padding * crow)

            image "Icons/grid-cell.png" xpos xp ypos yp zoom 0.5

            python:
                if ccolumn % (icons_per_row - 1) != 0 or ccolumn == 0:
                    ccolumn += 1
                else:
                    ccolumn = 0
                    crow += 1

label minigame:
    $grid_size = 100
    $icon_size = 50
    $icon_padding = 2
    $icons_per_row = 10

    $icons = SpriteManager(update = icons_update, events = icons_events)

    $icon_images = ["icon_1", "icon_2", "icon_3", "icon_4", "icon_5"]
    $icons_list = []

    scene background at half_size
    jump setup_icons


    return