# TES Character Generator

## Contents
This is where all the documentation for the project will be:

### Brief
The brief provided for this project presented an objective to create a service-orientated architecture for an application and must be composed of at least 4 services that work together. Service 1, the frontend, is the core service- it will render the Jinja2 templates required to interact with the application. Furthermore, the service will also be responsible for communicating with the 3 backend services. Service 2 and 3 are both tasked with generating random "objects" and direct them to the (frontend service 1). Finally, Service 4 is responsible for combining Services 2 and 3's results to create an outcome of which will be sent to the frontend.  

#### Additional Requirements
In order to do this, the follwowing was required:
- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
- A Risk Assessment
- An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built     through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the Service-oriented architecture that has been asked for.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to     run.
- The project must make use of a reverse proxy to make your application accessible to the user.

### My Approach
To achieve the project's objective, I decided to create a Character Generator based on Bethesda's 'The Elder Scrolls V: Skyrim'.
- Service 1:
  - Provides the Jinja2 template to display the generation page.
- Service 2:
  - Generates a random race.
- Service 3:
  - Generates a random class.
- Service 4:
  - Creates a character build and sends it to the frontend where it will be presented to the user.

### Architecture
#### Database Structure

#### Service Architecture
