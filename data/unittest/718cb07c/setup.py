import time
import requests
import os
from pathlib import Path

config_dirs = {"default": Path("/etc/softwareabc/configs"), "custom": Path("/usr/local/softwareabc/configs")}