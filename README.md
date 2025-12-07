# PlayerAPI
This is a PlayerAPI created for the backend course final test.

## Features

- view all players
- create new player
- view player by id
- view events by player id
- create events for certain player
- view all events.

## Setup
To run this, I recommend using a virtual environment with venv. The following steps provide guidance on how to use the app with venv.

### 1. Download or Clone project

- **Option 1: Download ZIP**
Choose Code from github and download to ZIP. Then extract to folder of your choice.

**Option 2: Clone with Git**
Open your preferred command prompt, example **PowerShell** (Windows) or **Terminal** (macOS/Linux). Then navigate to the folder where you want to store the project and clone project from github to there (you need to have git installed). For example.

```bash
cd  path\to\your\desired\folder
git clone git@github.com:HessuJJ/PlayerAPI.git
cd playerAPI
```
### 2. Download venv
```bash
python -m venv venv
```

## 3. Activate virtual enviroment venv

**Windows Command Prompt**
```bash
venv\Scripts\activate
```

**Windows PowerShell**
```bash
.\venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
source venv/bin/activate
```

## 4. Install dependencies
```bash
pip install -r requirements.txt
```

## 5. Run FastAPI in development mode 
```bash
fastapi dev app/main.py
```
This starts FastAPI in development mode locally. You can connect to the API:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

## 6. Closing FastAPI 
When in bash press ctrl+c 

## 7. Closing virtual enviroment venv
```bash
deactivate
```




