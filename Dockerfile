FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm
EXPOSE 80
CMD ["python", "-m", "http.server", "80"]
