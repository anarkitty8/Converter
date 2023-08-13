import base64
import bitarray
from ast import literal_eval


class hexNumber:
    def __init__(self, x):
        if isinstance(x, str):
            self.val = int(x, 16)
        elif isinstance(x, int):
            self.val = int(str(x), 16)

    def __str__(self):
        return hex(self.val)


def convert_from_int(convert_from: int, convert_to: str):
    if convert_to == "Number":
        return "No change"
    elif convert_to == "Text":
        return f"'{convert_from}'"
    elif convert_to == "Hex":
        return hex(convert_from)
    elif convert_to == "Base64":
        return "Unsupported Operation"
    elif convert_to == "Binary":
        convert_from = str(convert_from)
        return ' '.join(format(ord(x), 'b') for x in convert_from)


def convert_from_text(convert_from: str, convert_to: str):
    if convert_to == "Number":
        return "Unsupported Operation"
    elif convert_to == "Text":
        return "No Change"
    elif convert_to == "Hex":
        return "Unsupported Operation"
    elif convert_to == "Base64":
        return base64.b64encode(bytes(convert_from, "utf-8"))
    elif convert_to == "Binary":
        return ' '.join(format(ord(x), 'b') for x in convert_from)


def convert_from_hex(convert_from: str, convert_to: str):
    if convert_to == "Number":
        convert_from = str(hexNumber(convert_from))
        return literal_eval(convert_from)
    elif convert_to == "Text":
        return "Unsupported Operation"
    elif convert_to == "Hex":
        return "No Change"
    elif convert_to == "Base64":
        convert_from = str(hexNumber(convert_from))
        return base64.b64encode(bytes(convert_from, "utf-8"))
    elif convert_to == "Binary":
        return ' '.join(format(ord(x), 'b') for x in convert_from)


def convert_from_binary(convert_from: str, convert_to: str):
    if convert_to == "Number":
        return int(convert_from, 2)
    elif convert_to == "Text":
        test = bitarray(convert_from)
        ascs = test.tobytes().decode("ascii")
        return ascs
    elif convert_to == "Hex":
        return hex(int(convert_from, 2))
    elif convert_to == "Base64":
        return "Unsupported operation"
    elif convert_to == "Binary":
        return "No Change"


def convert_from_base64(convert_from: str, convert_to: str):
    if convert_to == "Text":
        return base64.b64decode(bytes(convert_from), "utf-8")
    elif convert_to == "Number":
        return "Unsupported Operation"
    elif convert_to == "Hex":
        return "Unsupported Operation"
    elif convert_to == "Binary":
        return ' '.join(format(ord(x), 'b') for x in convert_from)
    elif convert_to == "Base64":
        return "No Change"
