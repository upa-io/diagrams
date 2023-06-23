from diagrams import Cluster, Diagram
from diagrams.oci.compute import VirtualMachine
from diagrams.oci.network import LoadBalancer
from diagrams.oci.network import ServiceGateway

# Crear un nuevo diagrama llamado "Infraestructura en OCI"
with Diagram("Infraestructura en OCI", show=False):

    # Crear el grupo de componentes en la Public Subnet
    with Cluster("Public Subnet"):
        # Crear un API Gateway en la Public Subnet
        api_gateway = ServiceGateway("API Gateway")

    # Crear el grupo de componentes en la Private Subnet 1
    with Cluster("Private Subnet 1"):
        # Crear un Application Load Balancer en la Private Subnet 1
        app_lb = LoadBalancer("Application Load Balancer")

    # Crear el grupo de componentes en la Private Subnet 2
    with Cluster("Private Subnet 2"):
        # Crear las instancias de Virtual Machine en la Private Subnet 2
        vm1 = VirtualMachine("VM Instance 1")
        vm2 = VirtualMachine("VM Instance 2")

    # Crear el grupo de componentes en la Private Subnet 3
    with Cluster("Private Subnet 3"):
        # Crear un Internal Load Balancer en la Private Subnet 3
        internal_lb = LoadBalancer("Internal Load Balancer")

    # Crear el grupo de componentes en la Private Subnet 4
    with Cluster("Private Subnet 4"):
        # Crear las instancias de Virtual Machine en la Private Subnet 4
        vm3 = VirtualMachine("VM Instance 3")
        vm4 = VirtualMachine("VM Instance 4")

    # Establecer las relaciones entre los componentes
    api_gateway >> app_lb  # Conectar el API Gateway al Application Load Balancer
    app_lb >> vm1  # Conectar el Application Load Balancer a la VM Instance 1
    app_lb >> vm2  # Conectar el Application Load Balancer a la VM Instance 2
    vm2 >> internal_lb  # Conectar la VM Instance 2 al Internal Load Balancer
    vm3 >> internal_lb  # Conectar la VM Instance 3 al Internal Load Balancer
    internal_lb >> vm3  # Conectar el Internal Load Balancer a la VM Instance 3
