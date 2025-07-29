import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/cloudlabs-dev/api/cloudlabs-text-to-speech'

mcp = FastMCP('cloudlabs-text-to-speech')

@mcp.tool()
def synthesize(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''This endpoint is used to perform the text to audio conversion process'''
    url = 'https://cloudlabs-text-to-speech.p.rapidapi.com/synthesize'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'cloudlabs-text-to-speech.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def languages() -> dict: 
    '''This endpoint is used to get a list of available languages'''
    url = 'https://cloudlabs-text-to-speech.p.rapidapi.com/languages'
    headers = {'x-rapidapi-host': 'cloudlabs-text-to-speech.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def voices(language_code: Annotated[Union[str, None], Field(description='Use this parameter to filter the results by language code. Leave blank if you want to retrieve all available speakers')] = None) -> dict: 
    '''This endpoint is used to get a list of available speakers'''
    url = 'https://cloudlabs-text-to-speech.p.rapidapi.com/voices'
    headers = {'x-rapidapi-host': 'cloudlabs-text-to-speech.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'language_code': language_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
