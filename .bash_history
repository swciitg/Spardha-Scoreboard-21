ls
cd Backend/
ls
ls ../../gymkhana/
ls ../../gymkhana/SWC-Gymkhana-Portal/
cd spardhaAPI/
virtualenv --python=/usr/bin/python3.8 venv
virtualenv --python=/usr/bin/python3.7 venv
sudo su
exit
ls
cd Backend/spardhaAPI/
virtualenv --python=/usr/bin/python3.8 venv
sudo chown spardha ../../../../usr/bin/python3.8
exit
ls
cd Backend/
virtualenv --python=/usr/bin/python3.8 venv
exit
ls
cd webapps/
cd Spardha-Scoreboard-21/
ls
cd Backend/
ls
cd Sp
cd spardhaAPI/
virtualenv --python=/usr/bin/python3.8 venv
pip install gunicorn
cp ../../../gymkhana/SWC-Gymkhana-Portal/venv/bin/gunicorn_start.bash venv/bin/gunicorn_start.bash
ls
cd venv/bin/
;s
ls
nano gunicorn_start.bash 
sudo chmod u+x b0unicorn_start
exit
;s
ls
cd Backend/
ls
cd spardhaAPI/
ls
source venv/bin/activate
pip install gunicorn
deactivate
venv/bin/gunicorn_start.bash
exit
ls
cd Backend/
ls
cd spardhaAPI/
venv/bin/gunicorn_start.bash 
nano venv/bin/gunicorn_start.bash 
venv/bin/gunicorn_start.bash 
source venv/bin/activate
pip install -r ../requirements.txt 
deactivate
venv/bin/gunicorn_start.bash 
exit
ls
cd Backend/
ls
cd spardhaAPI/
ls
source venv/bin/activate
ls
python manage.py collectstatic
cat ../../../gymkhana/SWC-Gymkhana-Portal/gymkhana/settings.py 
nano spardhaAPI/settings.py 
deactivate
exit
source venv/bin/activate
python manage.py makemigrations
python manage.py migrate
cat spardhaAPI/settings.py 
cat ../../../gymkhana/SWC-Gymkhana-Portal/gymkhana/settings.py 
ls
ls spardhaAPI/
cd ..
cd spardhaAPI/
ls
cp spardhaAPI/static/ static/
cp -r spardhaAPI/static/ static/
ls
ls static/
deactivate
exit
ls
source venv/bin/activate
ls
python manage.py createsuperuser
exit
git pull
git remote -v
nano spardha/serializers.py 
exit
