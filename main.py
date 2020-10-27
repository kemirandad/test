def on_button_pressed_a():
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        # # . . .
        . # . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(3000)
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        # # . . .
        . # . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(3000)
    basic.show_leds("""
        # # . . .
        . # . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(3000)
    basic.show_leds("""
        # . . . .
        # # . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(3000)
    basic.show_leds("""
        # . . . .
        . # . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(2000)
    basic.show_leds("""
        . # . . .
        # . . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(3000)
    basic.show_leds("""
        . # . . .
        . # . . .
        # # . . .
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . # . . .
        # . . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(3000)
    basic.show_leds("""
        # . . . .
        . # . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(5000)
    basic.show_leds("""
        # # . . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(3000)
    basic.show_leds("""
        . # . . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(4000)
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    . # . . .
    . # . . .
    # # . . .
    . . . . .
    . . . . .
    """)
basic.pause(1000)
basic.show_leds("""
    # . . . .
    . . . . .
    # . . . .
    . . . . .
    . . . . .
    """)
basic.pause(3000)
basic.show_leds("""
    # . . . .
    . # . . .
    . . . . .
    . . . . .
    . . . . .
    """)
basic.pause(2000)
basic.show_leds("""
    # # . . .
    . # . . .
    # . . . .
    . . . . .
    . . . . .
    """)
basic.pause(3000)
basic.show_leds("""
    . . . . .
    . . . . .
    # # . . .
    . . . . .
    . . . . .
    """)
basic.pause(1000)
basic.show_leds("""
    # # . . .
    . # . . .
    # . . . .
    . . . . .
    . . . . .
    """)
basic.pause(3000)
basic.show_leds("""
    # # . . .
    . # . . .
    # # . . .
    . . . . .
    . . . . .
    """)
basic.pause(3000)
basic.show_leds("""
    . . . . .
    # . . . .
    . . . . .
    . . . . .
    . . . . .
    """)
basic.pause(1000)