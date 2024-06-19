FROM nikolaik/python-nodejs:python3.10-nodejs19

# 1. Add a non-root user
RUN groupadd -r myuser && useradd -r -g myuser myuser

# 2. Install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 3. Copy files and set permissions
COPY . /app/
WORKDIR /app/
RUN chown -R myuser:myuser /app

# 4. Upgrade pip and install requirements
RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir -U -r requirements.txt

# 5. Define CMD instruction
USER myuser
CMD bash start
