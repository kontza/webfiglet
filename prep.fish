if ! test -d venv
    python3 -mvenv venv
end
. venv/bin/activate.fish
pip install -r requirements.txt
