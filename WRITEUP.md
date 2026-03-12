# Write-up 

### Analyze, choose, and justify the appropriate resource option for deploying the app.

###VM vs App Service Analysis for CMS Application
###3Virtual Machine (VM)
Cost:
VMs require paying for compute, storage, and networking even when the resources are not fully used. Maintenance costs such as updates and monitoring also increase operational expenses.
Scalability:
Scaling with VMs usually requires manually creating additional instances and configuring load balancers. This makes scaling slower and requires more infrastructure management.
Availability:
High availability must be configured manually using tools like load balancers and backups. Without proper configuration, a VM failure can cause downtime.
Workflow:
Developers must manage the operating system, install dependencies, and configure the web server. This gives more control but increases management effort.
####App Service
Cost:
App Service uses a managed platform where infrastructure maintenance is handled automatically. This can reduce operational costs compared to managing full virtual machines.
Scalability:
App Service supports built-in auto-scaling, allowing the application to handle traffic changes automatically.
Availability:
It provides built-in high availability and automatic load balancing, improving reliability and uptime.
Workflow:
Deployment is easier because applications can be deployed directly from Git repositories or CI/CD pipelines without managing servers.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 
####Chosen Solution: App Service
App Service is the better option for deploying the CMS application because it simplifies deployment and infrastructure management. It provides automatic scaling, high availability, and reduced operational overhead. This allows developers to focus on improving the CMS application instead of managing servers.
####Application Changes
Since App Service manages the infrastructure, the application will not require manual server configuration or operating system management. Some configuration changes such as environment variables and deployment pipelines may be needed. These adjustments help the application run efficiently within the managed platform environment.
