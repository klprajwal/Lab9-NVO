# Lab9-NVO: 
--> Run main1.py it will create the Vnets and spin up the instances along with the customized NSG rules.

--> Use the below commands to run the docker file
#To build Docker images from these Dockerfiles, we can use the docker build command. 
docker build -t frr_container -f Dockerfile_frr .
docker build -t sdn_controller_container -f Dockerfile_sdn_controller .

#Run these containers using the docker run command:
docker run --name frr_container -d frr_container
docker run --name sdn_controller_container -d sdn_controller_container

--> Once the above two containers are up and running, execute "frr_sdn_container.py" file to configure the containers and form a BGP neighbourship
