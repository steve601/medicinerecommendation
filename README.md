# MEDICINE RECOMMENDER SYSTEM

## Overview
->The purpose of this project is to recommend to users five more medicine based on disease it cure.

### Prerequisites
*- Python 3.x*
*- Pip (Python package installer)*
*AWS Account*: Ensure you have an active AWS account.
*-EC2 Key Pair*: Create a key pair in your preferred region for SSH access.
*-Medicine Recommender System:* Ensure the application code is ready for deployment.
*-Domain Name (optional):* For a user-friendly URL.
### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/steve601/medicinerecommendation.git
    cd medicinerecommendation
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the .py file**
    ```sh
    python medapp.py
    ```

### Step-by-Step Deployment Guide
#### 1. Launch EC2 Instance
**Login to AWS Console.**
**Navigate to EC2 Dashboard.**
**Launch an Instance:**
    *Choose Amazon Linux 2 AMI.*
    *Select an instance type (e.g., t2.micro for testing, t2.medium or higher for production).*
    *Configure instance details as needed.*
    *Add storage (default is typically sufficient).*
    *Add tags (optional).*
    *Configure security group:*
    *Allow SSH (port 22) from your IP.*
    *Allow HTTP (port 80) and HTTPS (port 443) from all IPs.*
**Review and Launch:**
    ***Select the key pair created earlier.***
    **Launch the instance.*
#### 2. Connect to EC2 Instance
**SSH into the Instance:**
sh
Copy code
ssh -i "your-key-pair.pem" ec2-user@your-ec2-public-dns
#### 3. Install Dependencies
**Update System Packages:**

sh
Copy code
sudo yum update -y
Install Python and Pip:

sh
Copy code
sudo yum install python3 -y
sudo yum install python3-pip -y
Install Required Libraries:
Navigate to your project directory and install dependencies:

sh
Copy code
pip3 install -r requirements.txt
#### 4. Configure the Application
**Upload Application Code:**

    Use scp or an SFTP client to upload your application code to the EC2 instance.
    Place the code in a suitable directory, e.g., /home/ec2-user/medicine-recommender.
    
**Environment Variables**

    Create a .env file or export necessary environment variables.
    Ensure sensitive data like database credentials and API keys are secured.
#### 5. Set Up a Web Server
**Install Nginx:**

sh
Copy code
sudo amazon-linux-extras install nginx1.12 -y
sudo systemctl start nginx
sudo systemctl enable nginx
**Configure Nginx:**

Edit the Nginx configuration to reverse proxy to your application.
Example configuration for /etc/nginx/nginx.conf:
nginx
Copy code
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
**Restart Nginx:**
sh
Copy code
sudo systemctl restart nginx
#### 6. Start the Application
**Run the Application:**
Navigate to your application directory.
Start the application, for example using Gunicorn:
sh
Copy code
gunicorn --workers 3 app:app
Ensure the application listens on 127.0.0.1:8000.
#### 7. Security and Monitoring
**Set Up Firewall:**

Use AWS Security Groups to restrict access.
Consider using AWS WAF for additional security.
Monitoring:

Enable AWS CloudWatch to monitor system metrics.
Set up alarms for critical metrics.
Backup and Recovery:

Implement regular backups of your data.
Test recovery procedures.
#### Conclusion
Your Medicine Recommender System should now be deployed and accessible via your EC2 instance's public DNS or your configured domain name. Make sure to regularly update your system, monitor its performance, and secure it against potential threats.