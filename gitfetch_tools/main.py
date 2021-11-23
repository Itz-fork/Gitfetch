# Copyright (c) 2021 Itz-fork
# Gitfetch

import sys
import requests
from gitfetch_tools import Gitfetch_CLI

try:
    cli = Gitfetch_CLI(sys.argv[1])
    data = cli.output_data()
    sys.stdout.write(data)
except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
    print("☹ No Internet Connection")
except BaseException as e:
    usage = """
\033[1;36mGitFetch\033[0;0m \033[;1m Usage

 gitfetch [username]
  
 Ex:
     gitfetch Itz-fork
"""
    sys.stdout.write(usage)