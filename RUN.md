# create venv
python3 -m venv .venv   # if this errors, install venv: sudo apt-get install -y python3-venv

# activate
source .venv/bin/activate

# install deps
pip install --upgrade pip
pip install -r requirements.txt

# run app
streamlit run app.py --server.headless true


#Windows
python -m venv venv
cmd -venv\Scripts\activate
powershell - .\venv\Scripts\Activate.ps1

if powershell gives error:
1. Run powershell as administrator
2. Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py

