import board

from kmk.extensions.rgb import AnimationModes, RGB
from kmk.handlers.sequences import simple_key_sequence
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation


keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
encoder_handler.map = (
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
    ((KC.DOWN, KC.UP, KC.MUTE),),
    ((KC.VOLD, KC.VOLU, KC.N1),),
    ((KC.VOLD, KC.VOLU, KC.N1),),
)
layers_ext = Layers()

keyboard.modules = [layers_ext, encoder_handler]

rgb_ext = RGB(
    pixel_pin=board.NEOPIXEL,
    num_pixels=1,
    hue_default=60,
    sat_default=230,
    val_default=20,
    animation_mode=AnimationModes.RAINBOW  # STATIC  # RAINBOW
)
# keyboard.extensions.append(rgb_ext)
# rgb_ext.set_rgb_fill((200, 255, 0))  # this sets the values correctly, but is overridden by values from RGB

# Alish Pins for KB2040
keyboard.col_pins = (
board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D10, board.MOSI, board.D9, board.D8, board.D7, board.D6)
keyboard.row_pins = (board.A1, board.A0, board.SCK, board.MISO)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Alish Encoder Pins for KB2040
encoder_handler.pins = ((board.A3, board.A2, board.SDA, False),)

rse_esc = KC.LT(1, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=250)
lwr = KC.MO(4)

# Macros
ide_term = KC.RALT(KC.F12)
brc_ins = simple_key_sequence((KC.LBRC, KC.RBRC, KC.LEFT))
prn_ins = simple_key_sequence((KC.LPRN, KC.RPRN, KC.LEFT))
grave_ins = simple_key_sequence((KC.GRAVE, KC.GRAVE, KC.LEFT))

keyboard.keymap = [
    # Qwerty
    # ,-----------------------------------------------------------------------------------.
    # | Tab  |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  | Bksp |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # |Esc M1|   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |   '  | Enter|
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # | Shift|   Z  |   X  |   C  |   V  |   B  |   ;  |   N  |   M  |   ,  |   .  |   /  |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # | Ctrl | Alt  |  GUI |XXXXXX| MO1  |XXXXXX|XXXXXX| Space|XXXXXX|  MO2 |ALTF12| Ctrl |
    # `-----------------------------------------------------------------------------------'
    [
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC,
        rse_esc, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.QUOT, KC.ENT,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.SCOLON, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLASH,
        KC.LCTL, KC.LALT, KC.LGUI, KC.NO, lwr, KC.NO, KC.NO, KC.SPC, KC.NO, KC.MO(2), ide_term, KC.RGHT,
    ],
    # Number Layer (Raise Layer)
    # ,-----------------------------------------------------------------------------------.
    # |  ~ ` |   1  |   2  |   3  |   4  |   5  |   6  |   7  |   8  |   9  |   0  | Del  |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |  ; : |  [ { |  ] } |  ' " |  ; : |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |  - _ | = +  |      |      | Enter|
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      | |||> |      |      | Space|      |      |      |      |
    # `-----------------------------------------------------------------------------------'
    [  
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.SCLN, KC.LBRC, KC.RBRC, KC.LBRC, KC.RBRC, KC.SCLN,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MINS, KC.EQL, KC.TRNS, KC.SLASH, KC.BSLASH,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.NO, KC.MEDIA_PLAY_PAUSE, KC.NO, KC.NO, KC.MEDIA_PLAY_PAUSE, KC.LCTL, KC.LEFT, KC.RGHT,
    ],
    # Function Layer
    # ,-----------------------------------------------------------------------------------.
    # |      |      |      |      |      |      |      |      |      |      |      |      |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |      |      |      |      |      |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |      |      |      |      |      |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |      |      |      |      |      |
    # `-----------------------------------------------------------------------------------'
    [
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.TRNS,
        KC.CAPSLOCK, KC.F11, KC.F12, KC.TRNS, KC.TRNS, KC.TRNS, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.TRNS, KC.TRNS,
        KC.TRNS, brc_ins, prn_ins, grave_ins, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.NO, KC.MEDIA_PLAY_PAUSE, KC.NO, KC.NO, KC.SPC, KC.NO, KC.LCTL, KC.LEFT, KC.RGHT,
    ],
    # Gaming Layer (Left and right space)
    # ,-----------------------------------------------------------------------------------.
    # |      |      |      |      |      |      |      |      |      |      |      |      |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |      |      |      |      |      |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |      |      |      |      |      |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |      |      |      |      |      |
    # `-----------------------------------------------------------------------------------'
    [
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.QUOT, KC.ENT,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.RSFT,
        KC.LCTL, KC.TRNS, KC.LALT, KC.NO, KC.SPC, KC.NO, KC.NO, KC.SPC, KC.NO, KC.LCTL, KC.LEFT, KC.RGHT,
    ],
    # Experimental Symbol Layer (Lower Layer)
    # ,-----------------------------------------------------------------------------------.
    # | ~ `  |   !  |   @  |   #  |   $  |   %  |   ^  |   &  |   *  |   (  |   )  |  Del |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # |      |   -  |   =  |      |      |      |      |   ?  |   /  |   |  |   \  |   ~  |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |   _  |   +  |      |      |      |      |   {  |   }  |   [  |   ]  |      |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |      |      |      |      |      |
    # `-----------------------------------------------------------------------------------'
    [
        KC.GRAVE, KC.EXLM, KC.AT, KC.HASH, KC.DOLLAR, KC.PERCENT, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.DELETE,
        KC.NO, KC.KP_MINUS, KC.KP_EQUAL, KC.NO, KC.NO, KC.NO, KC.NO, KC.QUESTION, KC.SLASH, KC.PIPE, KC.BSLASH, KC.TILDE,
        KC.NO, KC.UNDERSCORE, KC.PLUS, KC.NO, KC.NO, KC.NO, KC.NO, KC.LCBR, KC.RCBR, KC.LBRC, KC.RBRC, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    ]
    # Experimental Number Layer (Raise Layer)
    # ,-----------------------------------------------------------------------------------.
    # |      |      |      |      |      |      |      |   7  |   8  |   9  |   0  | Del  |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |   4  |   5  |   6  |   .  |  =   |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |   1  |   2  |   3  |      | Enter|
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |      |      |      |      |      |
    # `-----------------------------------------------------------------------------------'
]


if __name__ == '__main__':
    # rgb_ext.set_rgb_fill((200, 255, 0))
    keyboard.go()
