# Flask Distributed File Storage System with Load Balancing
This project implements a distributed file storage system using Flask, a Python microframework, along with a load balancer for distributing incoming requests across multiple Flask servers. The system provides users with the ability to upload and download files through a web interface while ensuring efficient load distribution across server instances.

## Features
Upload and Download Functionality: Users can upload files to the system using a web form and download previously uploaded files by selecting them from a dropdown menu.

### Load Balancing: 
A custom load balancer distributes incoming requests among multiple Flask server instances to ensure optimal resource utilization and response times. The load balancer dynamically adjusts the load distribution based on the current load on each server.

### Fault Tolerance: 
The system incorporates fault tolerance mechanisms to handle server failures gracefully. In the event of a server failure, the load balancer redirects requests to other available servers, ensuring uninterrupted service.

### File Management: 
Uploaded files are stored in a designated directory on the server and are uniquely identified to prevent overwriting. Users can download files securely with options for renaming and downloading.

### Scalability: 
The system is designed to scale horizontally by adding more Flask server instances as the demand for file storage and retrieval increases. The load balancer seamlessly distributes requests across all available servers, enabling the system to handle a large volume of concurrent users.

## Usage
### Clone the Repository: 
Clone the repository to your local machine using the following command:

### bash
`git clone https://github.com//RameshBabuAsh/distributed_file_storage_systems.git`

### Set up Flask Servers:
Run the server scripts on different ports (e.g., 5000, 5001) to set up multiple Flask server instances.

### Start the Load Balancer: 
Run the load balancer script to handle incoming requests and distribute them across the Flask servers.

`python load_balancer.py`

### Access the Web Interface: 
Open a web browser and navigate to the appropriate URL to access the web interface. You can upload and download files through the interface.

### Monitor Server Loads: 
Monitor server loads and system performance to ensure efficient operation. You can adjust server configurations or add more instances as needed to optimize performance.
