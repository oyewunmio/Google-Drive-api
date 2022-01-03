export FN_AUTH_REDIRECT_URI=http://127.0.0.1:8080/hordanso-google/auth
# export FN_BASE_URI=http://127.0.0.1:8080/
export FLASK_APP=app.py
export FLASK_DEBUG=TRUE
export FN_FLASK_SECRET_KEY=hordanso_web

python -m flask run -p 8080
