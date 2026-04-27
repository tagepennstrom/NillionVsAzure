FROM python:3.9-slim

# set the working directory inside the container
WORKDIR /app

# copy requirements first (for better caching)
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the application code
COPY main.py .

# expose port 8000 for the API
EXPOSE 8000

# start the server (0.0.0.0 allows external access)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]