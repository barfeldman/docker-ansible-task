# Base image with Python 3.11 for minimal setup and include all dependecies for python script running easily
FROM python:3.11-slim

# Copy requirements for python script and install dependencies, along with Nmap and OpenSSH, in one layer
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y --no-install-recommends nmap openssh-server && \
    pip install -r requirements.txt && \
    [ -d /var/run/sshd ] || mkdir /var/run/sshd && \
    [ -d /var/log ] || mkdir /var/log && \
    echo 'root:root' | chpasswd && \
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \
    sed -i 's/#Port 22/Port 2244/' /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy health check script into the container
COPY health_check.py /usr/local/bin/health_check.py
RUN chmod +x /usr/local/bin/health_check.py

# Expose SSH on port 2244
EXPOSE 2244

# Start SSH and health check script
CMD ["/bin/sh", "-c", "/usr/sbin/sshd -D & python /usr/local/bin/health_check.py"]
