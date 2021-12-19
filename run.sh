export FN_AUTH_REDIRECT_URI=http://127.0.0.1:8080/hordanso-google/auth
export FN_BASE_URI=http://127.0.0.1:8080
export FN_CLIENT_ID='177314386585-lebv37p723ls51bkq8e4ak1s118odl1k.apps.googleusercontent.com'
export FN_CLIENT_SECRET="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"
export FLASK_APP=app.py
export FLASK_DEBUG=TRUE
export FN_FLASK_SECRET_KEY=hordanso_web

python -m flask run -p 8080
