import os
import sys

def keycode_to_string(keycode):
    KEYCODE_STRING_MAPPING = {
        308: "L_ALT",
        307: "R_ALT",
        305: "L_CTRL",
        306: "R_CTRL",
        304: "L_SHIFT",
        303: "R_SHIFT",
        309: "L_SUPER",
        1073742055: "R_SUPER",

        273: "UP",
        274: "DOWN",
        276: "LEFT",
        275: "RIGHT",

        280: "PAGE_UP",
        281: "PAGE_DOWN",

        278: "HOME",
        279: "END",

        301: "CAPS_LOCK",
        300: "NUM_LOCK",
        145: "SCREEN_LOCK",

        8: "BACKSPACE",
        311: "COMPOSE",
        127: "DELETE",
        13: "ENTER",
        27: "ESCAPE",
        277: "INSERT",
        19: "PAUSE",
        144: "PRINT",

        32: "SPACE",
        9: "TAB",

        256: "NUMPAD_0",
        257: "NUMPAD_1",
        258: "NUMPAD_2",
        259: "NUMPAD_3",
        260: "NUMPAD_4",
        261: "NUMPAD_5",
        262: "NUMPAD_6",
        263: "NUMPAD_7",
        264: "NUMPAD_8",
        265: "NUMPAD_9",
        270: "NUMPAD_ADD",
        266: "NUMPAD_DECIMAL",
        267: "NUMPAD_DIVIDE",
        271: "NUMPAD_ENTER",
        268: "NUMPAD_MULTIPLY",
        269: "NUMPAD_SUBTRACT",

        282: "F1",
        283: "F2",
        284: "F3",
        285: "F4",
        286: "F5",
        287: "F6",
        288: "F7",
        289: "F8",
        290: "F9",
        291: "F10",
        292: "F11",
        293: "F12",
        294: "F13",
        295: "F14",
        296: "F15",
    }

    if keycode in KEYCODE_STRING_MAPPING:
        return KEYCODE_STRING_MAPPING[keycode]
    elif keycode < 256:
        return chr(keycode)
    else:
        return "unsupported_keycode"

def make_sure_dir(dir_path):
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)