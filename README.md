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
For this project, I was required to utilise a database to persist some data in Service 1. I elected to create a simple non-relational database with one table. As shown below, a Character table was created with the attributes race, player class and build as they are all imperative to the application's main functionality. The database enabled for storing all builds generated within the application.

![ed](./documentation/ED.png)

#### Service Architecture
In order for the application to work correctly, all four services were required to communicate accordingly. The diagram below showcases how the services interact with each other.


Breaking down the diagram: Service 1 sends a 'GET' request to Services 2 and 3 in order to retrieve a randomly generated race and class, Services 2 and 3 adhere to this and return a data object at random, Service 1 then sends a 'POST' request to Service 4 with the generated race and class from the aformentioned Services. Service 4 then sends a 'POST' request to return the final build for the character.

#### VCS- Branch Modelling
Correct provisioning of the Git Feature branch model was one of the most important aspects of this project. As it required a rolling update, it was imperative that I seperated the two different implementations of the application. This meant building the first version of the application on a 'Feature-1' branch and building another feature branch ('Feature-2') from it to create the second implementation. Meanwhile, every other new implementation such as the Jenkinsfile was created on new branches and finally merged into the 'Development' branch once tested and declared ready.

#### CI Pipeline


### Project Tracking
For the project, I chose Trello as my main project tracking tool. This is where the project backlog is stored, highlighting each individual task broken down from the project epic.

### Risk Assessment
A risk assessment was created in order to monitor and plan for any potential risks that could jeaopardize the project. This proactive approach to implement the risk assessment could prevent the majority of incidents that could possibly occur during the project and minimises the likelihood and impact of those incidents. Below is the original risk assessment created during the planning stages of the project:
##### Original Risk Assessment

As I grew further into the project, I imporoved and added to the original risk assessment. It occured to me that there were certain areas within the project, especially its infrastructure that could greatly affect its success. 
##### Updated Risk Assessment

### Testing
#### Unit Testing
All testing for this project was carried out with Pytest. Unit testing was used to test each function within every route for every service. The tests were designed to verify whether the correct data is correctly inserted into the application whilst also checking if unexpected or incorrect values have been inserted. Furthermore, with the utilisation of Webhooks through Github, the unit tests were triggered automatically in Jenkins after each push to the project repository in Github. Upon completion of the tests built in Jenkins, a coverage report is also returned to the console with further information about the tests. See below for the unit tests for each service:


### Future Improvements

### Author
##### Tonny Allen Okech

### Acknowledgements
##### Harry Volker
##### Nathan Forester
