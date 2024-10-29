#Hercules

# Use Ubuntu as base image
FROM ubuntu:20.04

# Install Nginx and OpenSSH server, configure SSH and Nginx, and clean up unnecessary files and packages from operation system
RUN apt-get update && \
    apt-get install -y --no-install-recommends nginx openssh-server && \
    mkdir /var/run/sshd && \
    echo 'root:root' | chpasswd && \
    sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config && \
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config && \
    echo 'Hello World' > /var/www/html/index.html && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Expose ports for Nginx 80 and SSH (2222)
EXPOSE 80 2222

# Start Nginx and SSH services inside container
CMD ["bash", "-c", "service nginx start && service ssh start && bash"]
