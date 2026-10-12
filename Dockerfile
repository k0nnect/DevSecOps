FROM python:3.12-slim

# install deps
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy code
COPY . .

# run as non-root
RUN useradd -m appuser && chown -R appuser /app
USER appuser

ENV HOST=0.0.0.0
EXPOSE 5000
CMD ["python", "app.py"]