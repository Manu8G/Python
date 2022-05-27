from distutils.core import setup
import py2exe
import glob
import os
import sqlite3
from pathlib import Path
from time import sleep
from random import randrange
import re

setup(zipfile=None,
      options={"py2exe": {"bundle_files": 1}},
      windows=["script.py"]) # console para que salga una consola