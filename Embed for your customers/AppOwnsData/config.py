# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from dotenv import load_dotenv
load_dotenv()
import os

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = os.environ["AUTHENTICATION_MODE"]

    # Workspace Id in which the report is present
    WORKSPACE_ID = os.environ["WORKSPACE_ID"]
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = os.environ["REPORT_ID"]
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = os.environ["TENANT_ID"]
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = os.environ["CLIENT_ID"]
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = os.environ["CLIENT_SECRET"]
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = os.environ["AUTHORITY_URL"]
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = os.environ["POWER_BI_USER"]
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''