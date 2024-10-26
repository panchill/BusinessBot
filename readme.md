# Project Overview  
This project provides tools for generating business plans with integrated calculation functionalities and an interactive bot interface. The project includes several Python scripts for API interactions, document editing, calculations, and bot commands, each designed to support different aspects of business plan creation.  

## Installation
To start using this project, clone the repository and install the required dependencies:

```bash
git clone git@github.com:panchill/BusinessBot.git
cd BusinessBot
```

## Key Files and Functions
### api_dwnld.py
Handles API calls to download necessary resources:


### calculating_functions.py
Contains calculations of key metrics for your business plan.


### edit_docx_functions.py
Provides functions to edit .docx files.

### bot_cmds_list.py and reply.py
These files define bot commands and replies for user interaction. Customize bot_cmds_list.py to change bot responses and functions in reply.py to handle different bot requests.

### main_func.py
This is the main entry point of the project. Run this file to start the bot and access all functionality.

### requirements.txt
Lists all dependencies needed for the project. Make sure to install them before starting:

```python
pip install -r requirements.txt
```
### .env
The .env file stores sensitive information like API keys, access tokens, and other settings required for the project.

```python
TOKEN=tg_bot_token
API=yandex_drive_api
```

In this project, you need to replace 'tg_token_bot' with the token of your telegram bot, the 'API' with the API of your Yandex disk