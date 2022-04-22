import board

from kmk.extensions.rgb import AnimationModes, RGB
from kmk.handlers.sequences import simple_key_sequence
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation


keyboard = KMKKeyboard()
# Alish Pins for KB2040
keyboard.col_pins = (
    board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D10, board.MOSI, board.D9, board.D8, board.D7, board.D6)
keyboard.row_pins = (board.A1, board.A0, board.SCK, board.MISO)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

layers_ext = Layers()
keyboard.modules = [layers_ext]

# KB2040 Neopixel configuration
rgb_ext = RGB(
    pixel_pin=board.NEOPIXEL,
    num_pixels=1,
    hue_default=60,
    sat_default=230,
    val_default=20,
    animation_mode=AnimationModes.RAINBOW  # STATIC  # RAINBOW
)
keyboard.extensions.append(rgb_ext)

DEFAULT = 0
NUMBER = 1
FUNCTION = 2
GAMING = 3
EXP_SYMBOL = 4
EXP_NUM = 5

RSE_ESC = KC.LT(NUMBER, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=250)
FN = KC.MO(FUNCTION)
LWR = KC.MO(EXP_SYMBOL)
_______ = KC.TRNS
XXXXXXX = KC.NO


# Macros
BRACE_INSERT = simple_key_sequence((KC.LBRC, KC.RBRC, KC.LEFT))
CBR_INSERT = simple_key_sequence((KC.LCBR, KC.RCBR, KC.LEFT))
CODE_INSERT = simple_key_sequence((
    KC.GRAVE, KC.GRAVE, KC.GRAVE,
    KC.ENT, KC.ENT,
    KC.GRAVE, KC.GRAVE, KC.GRAVE,
    KC.UP
))
GRAVE_INSERT = simple_key_sequence((KC.GRAVE, KC.GRAVE, KC.LEFT))
PAREN_INSERT = simple_key_sequence((KC.LPRN, KC.RPRN, KC.LEFT))
VIM_COPY = simple_key_sequence((KC.DQT, KC.ASTR, KC.Y))

# TODO screen brightness up/down

# Modifier Helpers
BACK = KC.LGUI(KC.LBRC)
CMD_SFT = KC.LGUI(KC.LSFT)
FORWARD = KC.LGUI(KC.RBRC)
IDEA_TERM = KC.RALT(KC.F12)
SCREENSHOT_CLIP = KC.LGUI(KC.LCTL(KC.LSFT(KC.N4)))  # SCRN_CLIP
SCREENSHOT_FILE = KC.LGUI(KC.LSFT(KC.N4))  # SCRN_FILE


keyboard.keymap = [
    # 0:  Qwerty
    # ,-----------------------------------------------------------------------------------.
    # | Tab  |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  | Bksp |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # |Esc M1|   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |   '  | Enter|
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # | Shift|   Z  |   X  |   C  |   V  |   B  |EX_NUM|   N  |   M  |   ,  |   .  |   /  |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # | Ctrl | Alt  |  GUI |XXXXXX| MO1  |XXXXXX|XXXXXX| Space|XXXXXX|  MO2 |ALTF12| Ctrl |
    # `-----------------------------------------------------------------------------------'
    [
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC,
        RSE_ESC, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.QUOT, KC.ENT,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.MO(EXP_NUM), KC.N, KC.M, KC.COMM, KC.DOT, KC.SLASH,
        KC.LCTL, KC.LALT, KC.LGUI, KC.NO, LWR, KC.NO, KC.NO, KC.SPC, KC.NO, FN, IDEA_TERM, CMD_SFT,
    ],
    # 1:  Number Layer (Raise Layer)
    # ,-----------------------------------------------------------------------------------.
    # |  ~ ` |   1  |   2  |   3  |   4  |   5  |   6  |   7  |   8  |   9  |   0  | Del  |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # |      |Vol Up| Mute |      |      |      |      |  ; : |  [ { |  ] } |  ' " |  ; : |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |Vol Dn|      |Trck B|Trck F|      |      |  - _ | = +  |      |      | Enter|
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      | |||> |      |      | Space|      |      |      |      |
    # `-----------------------------------------------------------------------------------'
    [
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.DELETE,
        KC.TRNS, KC.VOLU, KC.MUTE, KC.TRNS, KC.TRNS, KC.TRNS, KC.SCLN, KC.LBRC, KC.RBRC, KC.LBRC, KC.RBRC, KC.SCLN,
        KC.TRNS, KC.VOLD, KC.TRNS, KC.MRWD, KC.MFFD, KC.TRNS, KC.TRNS, KC.MINS, KC.EQL, KC.TRNS, KC.SLASH, KC.BSLASH,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.NO, KC.MEDIA_PLAY_PAUSE, KC.NO, KC.NO, KC.SPC, KC.LCTL, KC.LEFT, KC.RGHT,
    ],
    # 2:  Function Layer
    # ,-----------------------------------------------------------------------------------.
    # |  Esc |  F1  |  F2  |  F3  |  F4  |  F5  |  F6  |  F7  |  F8  |  F9  | F10  | Bksp |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # | Caps | F11  | F12  | Back | Frwrd|      | Left |  Up  | Down | Right|      |      |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      | [x]  | (x)  | `x`  |      |      |      |      |      |SCRCLP|SCRFIL|      |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |      |      |      |      |      |
    # `-----------------------------------------------------------------------------------'
    [
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.TRNS,
        KC.CAPSLOCK, KC.F11, KC.F12, BACK, FORWARD, KC.TRNS, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.TRNS, KC.TRNS,
        KC.TRNS, BRACE_INSERT, PAREN_INSERT, GRAVE_INSERT, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, SCREENSHOT_CLIP, SCREENSHOT_FILE, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.NO, KC.MEDIA_PLAY_PAUSE, KC.NO, KC.NO, KC.SPC, KC.NO, KC.LCTL, KC.LEFT, KC.RGHT,
    ],
    # 3:  Gaming Layer (Left and right space)
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
    # 4:  Experimental Symbol Layer (Lower Layer)
    # ,-----------------------------------------------------------------------------------.
    # |  ~   |   !  |   @  |   #  |   $  |   %  |   ^  |   &  |   *  |   (  |   )  |  Del |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # |      |   -  |   =  |      |      |      |      |   ?  |   /  |   [  |   ]  |   ~  |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |   _  |   +  |      |      |      |      |   |  |   \  |   {  |   }  |      |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |      |      |      |      |      |
    # `-----------------------------------------------------------------------------------'
    [
        KC.TILDE, KC.EXLM, KC.AT, KC.HASH, KC.DOLLAR, KC.PERCENT, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.DELETE,
        KC.NO, KC.KP_MINUS, KC.KP_EQUAL, KC.NO, KC.NO, KC.NO, KC.NO, KC.QUESTION, KC.SLASH, KC.LBRC, KC.RBRC, KC.TILDE,
        KC.NO, KC.UNDERSCORE, KC.PLUS, KC.NO, KC.NO, KC.NO, KC.NO, KC.PIPE, KC.BSLASH, KC.LCBR, KC.RCBR, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    ],
    # 5:  Experimental Number Layer (Raise Layer)
    # ,-----------------------------------------------------------------------------------.
    # |      |      |      |      |      |      |   +  |   7  |   8  |   9  |   *  | Del  |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # |      |      |      |      |      |      |   -  |   4  |   5  |   6  |   /  |  =   |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |   0  |   1  |   2  |   3  |   .  | Enter|
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |      |      |      |      |      |      |      |      |      |
    # `-----------------------------------------------------------------------------------'
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.N9, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    ]
]


if __name__ == '__main__':
    keyboard.go()
