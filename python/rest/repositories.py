import json
import logging
import os
import requests


class Repositories:
    def __init__(self):
        self.git_endpoint = "https://api.github.com"
        self.headers = {"Authorization": f"token {os.environ['GITHUB_PAT']}"}


    def list_repos_in_org(self, org):
        """
        list_repos_in_org -- List all repositories of a Github organization

        @params:
            1. org (str): Name of the organization (from `https://github.com/<org>`)
        @return:
            response.json() (list) -- List of dictionaries, each of which represents information about a repository in the Github organization

        Documentation: https://docs.github.com/en/rest/repos/repos#list-organization-repositories
        """
        try:
            response = requests.get(f"{self.git_endpoint}/orgs/{org}/repos", headers=self.headers)
            if 200 <= response.status_code < 300:
                return response.json()
            else:
                print(f"[ERROR] Could not get repositories from Github organization `{org}`\nStatus code: {response.status_code}\nReason: {response.reason}")
        except Exception as err:
            print(f"[ERROR] Could not get repositories from Github organization `{org}` with error: {err}")


    def create_repo_in_org(self, org, info):
        """
        create_repo_in_org -- Create a repository in a Github organization
        Note: You must be an organization owner and your PAT must have `repo` enabled

        @params:
            1. org (str): Name of the organization (from `https://github.com/<org>`)
            2. info (dict): Information about the repository to create (`name` in `info` is required)
        @return:
            None
        
        Documentation: https://docs.github.com/en/rest/repos/repos#create-an-organization-repository
        """
        try:
            response = requests.post(f"{self.git_endpoint}/orgs/{org}/repos", data=json.dumps(info), headers=self.headers)
            if 200 <= response.status_code < 300:
                print(f"[INFO] Successfully created the repository `{info['name']}` in Github orgnanization `{org}`\nStatus code: {response.status_code}")
            else:
                print(f"[ERROR] Could not create a repository in Github organization `{org}`\nStatus code: {response.status_code}\nReason: {response.reason}")
        except Exception as err:
            print(f"[ERROR] Could not create a repository in Github organization `{org}` with error: {err}")


    def get_repo_info(self, owner, repo):
        pass


    def update_repo_info(self, owner, repo):
        pass


    def delete_repo(self, owner, repo):
        pass


    def enable_repo_automated_security_fixes(self, owner, repo):
        pass

    
    def disable_repo_automated_security_fixes(self, owner, repo):
        pass