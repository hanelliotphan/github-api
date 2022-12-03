import json
import os
import requests


class Organizations:
    def __init__(self):
        self.git_endpoint = "https://api.github.com"
        self.headers = {"Authorization": f"token {os.environ['GITHUB_PAT']}"}


    def list_users_blocked_by_org(self, org):
        try:
            pass
        except Exception as err:
            pass