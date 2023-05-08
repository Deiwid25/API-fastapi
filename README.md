# Project init

```sh
git branch -M main

git remote add origin git@github.com:Deiwid25/API-fastapi.git



git pull origin main --allow-unrelated-histories



git add .
git commit -m ""
git push -u origin main


git push -u origin main

python3 -m venv env
source env/bin/activate

```


sudo lsof -t -i tcp:8000 | xargs kill -9
uvicorn main:app --reload --host 0.0.0.0
