import board

from kmk.extensions.rgb import AnimationModes, RGB
from kmk.handlers.sequences import simple_key_sequence
from kmk.keys import KC, Key
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

# Layer indexes
DEFAULT = 0
FUNCTION = 1
SYMBOL = 2
NUMBER = 3

RSE_ESC = KC.LT(NUMBER, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=250)
FN = KC.MO(FUNCTION)
LWR = KC.MO(SYMBOL)
_______ = KC.TRNS
XXXXXXX = KC.NO


# Macros
BRC_INST = simple_key_sequence((KC.LBRC, KC.RBRC, KC.LEFT))
CBR_INST = simple_key_sequence((KC.LCBR, KC.RCBR, KC.LEFT))
CODE_INST = simple_key_sequence((
    KC.GRV, KC.GRV, KC.GRV,
    KC.ENT, KC.ENT,
    KC.GRV, KC.GRV, KC.GRV,
    KC.UP
))
GRV_INST = simple_key_sequence((KC.GRAVE, KC.GRAVE, KC.LEFT))
PRN_INST = simple_key_sequence((KC.LPRN, KC.RPRN, KC.LEFT))
QUO_INST = simple_key_sequence((KC.DQUO, KC.DQUO, KC.LEFT))
VIM_COPY = simple_key_sequence((KC.DQT, KC.ASTR, KC.Y))

# Modifier Helpers
BACK = KC.LGUI(KC.LBRC)
CMD_SFT = KC.LGUI(KC.LSFT)
FWD = KC.LGUI(KC.RBRC)
JB_TRM = KC.RALT(KC.F12)
SCRN2CLP = KC.LGUI(KC.LCTL(KC.LSFT(KC.N4)))
SCRN2FL = KC.LGUI(KC.LSFT(KC.N4))

# TODO sync up documented layers with actual layouts
keyboard.keymap = [
    # 0:  Qwerty
    # ,-----------------------------------------------------------------------------------.
    # | Tab  |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  | Bksp |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # |EscRse|   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |  ; : |  ' " |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # | Shift|   Z  |   X  |   C  |   V  |   B  |EX_NUM|   N  |   M  |   ,  |   .  | Enter|
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # | Ctrl | Alt  |  GUI |XXXXXX| MO1  |XXXXXX|XXXXXX| Space|XXXXXX|  MO2 |JB_TRM| Ctrl |
    # `-----------------------------------------------------------------------------------'
    [
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R, KC.T,    KC.Y,    KC.U,   KC.I,    KC.O,    KC.P,    KC.BSPC,
        RSE_ESC, KC.A,    KC.S,    KC.D,    KC.F, KC.G,    KC.H,    KC.J,   KC.K,    KC.L,    KC.SCLN, KC.QUOT,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V, KC.B,    KC.NO,   KC.N,   KC.M,    KC.COMM, KC.DOT,  KC.ENT,
        KC.LCTL, KC.LALT, KC.LGUI, XXXXXXX, LWR,  XXXXXXX, XXXXXXX, KC.SPC, XXXXXXX, FN,      JB_TRM,  CMD_SFT,
    ],
    # 1:  Function Layer
    # ,-----------------------------------------------------------------------------------.
    # |  Esc |  F1  |  F2  |  F3  |  F4  |  F5  |  F6  |  F7  |  F8  |  F9  | F10  | Bksp |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # | Caps | F11  | F12  | Back | Frwrd|      | Left |  Up  | Down | Right|      |      |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      | [x]  | (x)  | {x}  | "x"  | `x`  | ``x``|      |      |SCRN2F|SCRN2C|      |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |XXXXXX|      |XXXXXX|XXXXXX|      |XXXXXX|      |      |      |
    # `-----------------------------------------------------------------------------------'
    [
        KC.ESC,  KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,     KC.F7,   KC.F8,   KC.F9,    KC.F10,   KC.TRNS,
        KC.CAPS, KC.F11,   KC.F12,   BACK,     FWD,      KC.TRNS,  KC.LEFT,   KC.DOWN, KC.UP,   KC.RIGHT, KC.TRNS,  KC.TRNS,
        KC.TRNS, BRC_INST, PRN_INST, CBR_INST, QUO_INST, GRV_INST, CODE_INST, _______, _______, SCRN2FL,  SCRN2CLP, KC.TRNS,
        KC.TRNS, KC.TRNS,  KC.TRNS,  XXXXXXX,  KC.MPLY,  XXXXXXX,  XXXXXXX,   KC.SPC,  XXXXXXX, KC.RGUI,  KC.RALT,  KC.RCTL,
    ],
    # 2:  Symbol Layer (Lower Layer)
    # ,-----------------------------------------------------------------------------------.
    # |   `  |   !  |   @  |   #  |   $  |   %  |   ^  |   &  |   *  |   (  |   )  |  Del |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # |      |   -  |   =  |   ;  |   :  |      |      |   ?  |   /  |   [  |   ]  |   ~  |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |LShift|   _  |   +  |      |      |      |      |   \  |   |  |   {  |   }  | Enter|
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # | LCtl | LAlt | LGui |XXXXXX|      |XXXXXX|XXXXXX|      |XXXXXX| RGui | RAlt | RCtl |
    # `-----------------------------------------------------------------------------------'
    [
        KC.GRAVE, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.DEL,
        KC.NO,    KC.PMNS, KC.PEQL, KC.SCLN, KC.COLN, KC.NO,   KC.NO,   KC.QUES, KC.SLSH, KC.LBRC, KC.RBRC, KC.TILDE,
        KC.LSFT,  KC.UNDS, KC.PLUS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.BSLS, KC.PIPE, KC.LCBR, KC.RCBR, _______,
        KC.LCTL,  KC.LALT, KC.LGUI, XXXXXXX, KC.NO,   XXXXXXX, XXXXXXX, KC.SPC,  XXXXXXX, KC.RGUI, KC.RALT, KC.RCTL,
    ],
    # 3:  Number Layer (Raise Layer)
    # ,-----------------------------------------------------------------------------------.
    # |      |   1  |   2  |   3  |  4   |  5   |   6  |   7  |   8  |   9  |   0  | Bkpc |
    # |------+------+------+------+------+-------------+------+------+------+------+------|
    # |      |Vol Up| Mute | Back |  Fwd |      |   /  |   4  |   5  |   6  |   -  |   =  |
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |Vol Dn|      | T Bak| T Fwd|      |   *  |   1  |   2  |   3  |   +  | Enter|
    # |------+------+------+------+------+------+------+------+------+------+------+------|
    # |      |      |      |XXXXXX| |||> |XXXXXX|XXXXXX| Space|XXXXXX|   0  |   .  |      |
    # `-----------------------------------------------------------------------------------'
    [
        _______, KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,  KC.N8,   KC.N9, KC.N0,   KC.BSPC,
        KC.NO,   KC.VOLU, KC.MUTE, KC.NO,   KC.NO,   KC.NO,   KC.PSLS, KC.N4,  KC.N5,   KC.N6, KC.PMNS, KC.PEQL,
        KC.NO,   KC.VOLD, KC.NO,   KC.MRWD, KC.MFFD, KC.NO,   KC.PAST, KC.N1,  KC.N2,   KC.N3, KC.PPLS, KC.PENT,
        KC.LCTL, KC.LALT, KC.LGUI, XXXXXXX, KC.MPLY, XXXXXXX, XXXXXXX, KC.SPC, XXXXXXX, KC.N0, KC.PDOT, _______,
    ]
]

if __name__ == '__main__':
    keyboard.go()
