# FROM python:3.11-slim


# # WORKDIR /app

# COPY ./ .

# RUN pip install --upgrade pip && pip install -r requirements.txt


# # COPY ./ app

# EXPOSE 80

# CMD [ "uvicorn","app.main:app","--host","0.0.0.0","--port","80"]



FROM python:3.11-slim

WORKDIR /news_doc

COPY ./ .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 80

CMD [ "uvicorn","app.main:app","--host","0.0.0.0","--port","80" ]