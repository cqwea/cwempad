import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import Keys

keyboard = KMKKeyboard()


keyboard.matrix = Keys(
    pins=[
        board.D0,
        board.D1,
        board.D2,
        board.D3,
    ],
    value_when_pressed=False,
)


keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
    ]
]

if __name__ == '__main__':
    keyboard.go()
