import os

BASE_URL = "https://igrovoy.rt.ru"

DEFAULT_TIMEOUT = 15
IMPLICIT_WAIT = 0

HEADLESS = os.getenv("HEADLESS", "0") == "1"

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
