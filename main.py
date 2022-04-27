def pulsador_a():
    basic.show_icon(IconNames.HAPPY)

def pulsador_b():
    basic.show_icon(IconNames.SAD)

input.on_button_pressed(Button.A, pulsador_a)
input.on_button_pressed(Button.B, pulsador_b)
   
