FROM python:3.9.16-slim
ARG PORT
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt \
    && python manage.py migrate \
    && python manage.py collectstatic --noinput

CMD gunicorn --bind 0.0.0.0:$PORT oc_lettings_site.wsgi
