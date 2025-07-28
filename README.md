### Python Libraries for Devops Usecases
```
paramiko: “Paramiko is a low‑level Python library... great for tasks where you need to manage the connections, authentication... in a granular manner.”
Used paramiko for this exception handling paramiko.ssh_exception.AuthenticationException
Fabric: Fabric is built on top of Paramiko and abstracts many of the more complex aspects of direct SSH communication.
Use Case: connected EC2 instances which are in us-east-1 and performed sytem updates. For this, I have used boto3 & Fabric python libraries
Example: fabfile.py in useful-modules-for-devops-->fabric
Boto3 AWS SDK for Python: This is used to connect AWS from python script
Use case: Used this module for multiple tasks like Cost management, upload files to AWS S3, created AWS infrastructure etc.,
Example: Refer useful-modules-for-devops-->boto3




```
