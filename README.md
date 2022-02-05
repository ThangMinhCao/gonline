# Gonline

#### Online multiplayer Go (Five in a row)

## Run app locally

1. Set up Python virtual environment (if needed)

```bash
# Create env for the project
python3 -m venv gonline_env

# Activate env (for bash)
source ./gonline_env/bin/activate
```

For other patforms: https://docs.python.org/3/library/venv.html

2. Install all requirements

```bash
pip3 install -r requirements.txt
```

3. Export database URI

```bash
DATABASE_URI=<Enter your own SQL database URI>
```

4. Start the Flask server

```bash
python run.py
```

## Technologies

1. Flask
2. SocketIO
3. SQLAlchemy + PostgreSQL
