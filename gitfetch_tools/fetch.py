# Copyright (c) 2021 Itz-fork
# Gitfetch

import os
import requests
import subprocess


class GitFetch():
    def __init__(self, user) -> None:
        self.user = user
    
    def fetch_user_data(self):
        req = requests.get(f"https://api.github.com/users/{self.user}").json()
        # User data
        # make a dictionary that contains SOME DATA of the user (idk why i am supposed to do this)
        location = req["location"] if not req["location"] is None else " "
        blog = req["blog"] if not req["blog"] is None else " "
        twitter = f"https://twitter.com/{req['twitter_username']}" if not req["twitter_username"] is None else " "

        info_dict = {
            "name": req["name"],
            "bio": req["bio"],
            "location": location,
            "public_repos": req["public_repos"],
            "gists": req["public_gists"],
            "followers": req["followers"],
            "following": req["following"],
            "github_profile": req["html_url"],
            "blog_url": blog,
            "twitter_url": twitter
        }
        return info_dict


class Gitfetch_CLI():
    def __init__(self, user) -> None:
        self.user_name = user

    def make_cmd(self, git_dict):
        command = f"bash '{os.path.dirname(__file__)}/display'"
        for k, y in git_dict.items():
            command += f""" "{k.replace("_", " ").capitalize()}: {y}" """
        return command
    
    def output_data(self):
        fetch = GitFetch(self.user_name)
        get_info = fetch.fetch_user_data()
        cmd = self.make_cmd(get_info)
        bash_out = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        output = bash_out.stdout.read()[:-1].decode("utf-8")
        return output