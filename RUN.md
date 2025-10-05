# create venv
python3 -m venv .venv   # if this errors, install venv: sudo apt-get install -y python3-venv

# activate
source .venv/bin/activate

# install deps
pip install --upgrade pip
pip install -r requirements.txt

# run app
streamlit run app.py --server.headless true

