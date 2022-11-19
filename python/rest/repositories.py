import requests
import os


class Repositories:
    def __init__(self):
        self.git_endpoint = "https://api.github.com"
        self.headers = {"Authorization": f"token {os.environ['GITHUB_PAT']}"}


    def list_org_repos(self, org):
        """
        list_org_repos -- List all repositories of a Github organization

        @params:
            1. org (str): Name of the organization (from `https://github.com/<org>`)
        @return:
            response.json() (list) -- List of dictionaries, each of which represents information about a repository in the Github organization

        Documentation: https://docs.github.com/en/rest/repos/repos#list-organization-repositories
        """
        try:
            response = requests.get(f"{self.git_endpoint}/orgs/{org}/repos", headers=self.headers)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"[ERROR] Could not get repositories from Github organization `{org}`\nStatus code: {response.status_code}\nReason: {response.reason}")
        except Exception as err:
            print(f"[ERROR] Could not get repositories from Github organization `{org}` with error: {err}")


    def create_org_repo(self, org):
        pass


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