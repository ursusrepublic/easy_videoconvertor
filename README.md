# easy_video_converter

1. Get aws key id / access key and put it in credentials.py
2. Install packages with $ pip install -r requirements.txt
3. Run utils.py just ONCE to get api endpoint, and put it in credentials.py
4. Setup and run flask app:
   * linux, macos:
     1. $ export FLASK_APP=app.py 
     2. $ flask run
   * windows:
     1. $ set FLASK_APP=app.py 
     2. $ flask run

nb: default aws region hardcoded as eu-west-1