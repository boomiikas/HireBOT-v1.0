cd ~

mkdir HireBOT

cd "HireBOT"

code .

---------------------------------------------------------------------
sudo apt update

sudo apt install python3-venv -y

python3 -m venv venv

source venv/bin/activate

-------------------------------------------------
cd backend

python3 -m venv venv

source venv/bin/activate  # (on Windows use venv\Scripts\activate)

pip install fastapi uvicorn python-dotenv supabase pyjwt

-------------------------------------------------------------------
cd ../

cd frontend

npm create vite@latest .

# → Choose React + JavaScript

=========

sudo apt remove nodejs -y
sudo apt install npm

curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
source ~/.bashrc
nvm --version
nvm install 22
nvm use 22
nvm alias default 22

node -v

npm -v

npm install

=========
npm list tailwindcss

node ./node_modules/tailwindcss/dist/lib.js init -p

---------
check 

find . -maxdepth 3 -type f -name "tailwind.config.js"

find . -maxdepth 3 -type f -name "postcss.config.js"

------
Manually create tailwind.config.js and postcss.config.js

===================
Run it:

npm run dev
----------------------------------------------------------------------
Build img:
Dockerfile in backend folder
==============================
docker build -t hirebot-backend .
Run container:
docker run -d -p 8000:8000 hirebot-backend
----------------------------------------------------------------------------
Runs both front and back end

cd ~/HireBOT/deployment
docker compose up --build
------------------------
in ubuntu 
docker compose up -d --build
docker ps -a

