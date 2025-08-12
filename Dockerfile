# 1) Start from a tiny Linux with Python preinstalled
FROM python:3.11-slim

# 2) Create and switch to a working directory inside the image
WORKDIR /app

# 3) Copy only requirements first (improves build caching)
COPY requirements.txt .

# 4) Install Python dependencies inside the image
RUN pip install --no-cache-dir -r requirements.txt

# 5) Copy the rest of your source code
COPY . .

# 6) Document that our app listens on 8000
EXPOSE 8001

# 7) Command that runs when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
