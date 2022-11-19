import requests
import json
import os


class Organizations:
    def __init__(self):
        self.git_endpoint = "https://api.github.com"
        self.headers = {"Authorization": f"token {os.environ['GITHUB_PAT']}"}
    
    def list_github_orgs(self):
        pass
    
    def get_org_info(self, org):
        """
        get_org_info -- Retrieve information about a Github organization

        @params:
            1. org (str): Name of the organization (from `https://github.com/<org>`)
        @return: 
            response.json() (dict) -- The dictionary of the JSONable object of the requests.get call

        Documentation: https://docs.github.com/en/rest/orgs/orgs#get-an-organization
        """
        try:
            response = requests.get(f"{self.git_endpoint}/orgs/{org}", headers=self.headers)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"[ERROR] Count not retrieve information of Github organization {org}.\nStatus code: {response.status_code}\nReason: {response.reason}")
        except Exception as err:
            print(f"[ERROR] Could not retrieve information of Github organization {org}: {err}")
    
    def update_org_info(self, org, info):
        pass
    
    def list_org_apps(self, org):
        pass
    
    def enable_disable_org_security_product(self, org):
        pass
    
    def list_auth_user_orgs(self, org):
        pass
    
    def list_user_orgs(self, username):
        pass