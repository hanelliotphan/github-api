import json
import logging
import os
import requests


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
            if 200 <= response.status_code < 300:
                return response.json()
            else:
                print(f"[ERROR] Could not retrieve information of Github organization `{org}`\nStatus code: {response.status_code}\nReason: {response.reason}")
        except Exception as err:
            print(f"[ERROR] Could not retrieve information of Github organization `{org}` with error: {err}")
    
    
    def update_org_info(self, org, info):
        pass
    
   
    def list_org_apps(self, org):
        """
        list_org_apps -- List all app installations for a Github organization
        Note: You must be the organization owner and your PAT must have `admin:read`

        @params:
            1. org (str): Name of the organization (from `https://github.com/<org>`)
        @return:
            response.json() (dict) -- Dictionary of general information about the apps in Github 
            organization and information about each of the apps 

        Documentation: https://docs.github.com/en/rest/orgs/orgs#list-app-installations-for-an-organization
        """
        pass
    
    
    def enable_disable_org_security_product(self, org):
        pass
    
    
    def list_auth_user_orgs(self, org):
        pass
    
    
    def list_user_orgs(self, username):
        """
        list_user_orgs -- List all public organizations of a Github user

        @params:
            1. username (str): Github username (from `https://github.com/<username>`)
        @return:
            response.json() (list) -- List of dictionaries, each of which represents information about a Github organization that the user belongs to

        Documentation: https://docs.github.com/en/rest/orgs/orgs#list-organizations-for-a-user
        """
        try:
            response = requests.get(f"{self.git_endpoint}/users/{username}/orgs", headers=self.headers)
            if 200 <= response.status_code < 300:
                return response.json()
            else:
                print(f"[ERROR] Could not retrieve organizations of Github user `{username}`\nStatus code: {response.status_code}\nReason: {response.reason}")
        except Exception as err:
            print(f"[ERROR] Could not retrieve organizations of Github user `{username}` with error: {err}")



class BlockingUsers:
    def __init__(self):
        self.git_endpoint = "https://api.github.com"
        self.headers = {"Authorization": f"token {os.environ['GITHUB_PAT']}"}

    
    def list_users_blocked_by_org(self, org):
        """
        list_user_blocked_by_org -- List all users blocked by a Github organization
        Note: You must have to be an organization admin with `admin:org` in your PAT

        @params:
            1. org (str): Name of the organization (from `https://github.com/<org>`)
        @return:
            response.json() (list) -- List of dictionaries including information of each block user
        
        Documentation: https://docs.github.com/en/rest/orgs/blocking?apiVersion=2022-11-28#list-users-blocked-by-an-organization
        """
        try:
            response = requests.get(f"{self.git_endpoint}/orgs/{org}/blocks", headers=self.headers)
            if 200 <= response.status_code < 300:
                return response.json()
            else:
                print(f"[ERROR] Could not retrieve blocked users of Github organization `{org}`\nStatus code: {response.status_code}\nReason: {response.reason}")
        except Exception as err:
            print(f"[ERROR] Could not retrieve blocked users of Github organization `{org}` with error: {err}")


    def check_if_user_blocked_by_org(self, org, username):
        """
        check_if_user_blocked_by_org -- Check if a user is blocked by
            a Github organization
        Note: You must have to be an organization admin with `admin:org` in your PAT

        @params:
            1. org (str): Name of the organization (from `https://github.com/<org>`)
            2. username (str): Github username of the user
        @ return:
            (bool) True/False if the user is blocked by the organization
        
        Documentation: https://docs.github.com/en/rest/orgs/blocking?apiVersion=2022-11-28#check-if-a-user-is-blocked-by-an-organization
        """
        try:
            response = requests.get(f"{self.git_endpoint}/orgs/{org}/blocks/{username}", headers=self.headers)
            if 200 <= response.status < 300:
                return True
            else:
                print(f"[WARNING] The user `{username}` might not be blocked by Github organization `{org}` or some error might have occurred\nStatus code: {response.status_code}")
        except Exception as err:
            print(f"[ERROR] Could not check if the user `{username}` is blocked by Github organization `{org}` with error: {err}")