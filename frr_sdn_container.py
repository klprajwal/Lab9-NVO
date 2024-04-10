from netmiko import ConnectHandler
import time

def configure_frr_ssh():
    # FRR SSH configuration
    frr_device = {
        'device_type': 'linux',
        'host': '172.24.4.11',
        'username': 'mininet',
        'password': 'mininet'
    }

    # SSH into the VM1
    ssh_conn = ConnectHandler(**frr_device)

    # Configure FRR BGP
    frr_config_commands = [
        'sudo vtysh',  # Enter FRR shell
        'configure terminal',
        'router bgp 100',  # Replace with your FRR BGP ASN
        'neighbor 172.17.0.2 remote-as 200',  # Configure BGP peering with SDN controller
        'exit',  # Exit router bgp configuration
        'exit',  # Exit configuration terminal
        'write memory'  # Save configuration
    ]

    # Send commands to configure FRR BGP
    output = ssh_conn.send_config_set(frr_config_commands)

    # Print the output for verification
    print(output)

    # Disconnect SSH session
    ssh_conn.disconnect()

def configure_sdn_controller_ssh():
    # SDN Controller SSH configuration
    sdn_controller_device = {
        'device_type': 'linux',
        'host': '172.24.4.11',
        'username': 'mininet',
        'password': 'mininet'
    }

    # SSH into the VM1
    ssh_conn = ConnectHandler(**sdn_controller_device)

    # Configure SDN Controller BGP
    sdn_controller_config_commands = [
        'sudo ryu-manager bgp_enable_controller.py',  # Command to enable BGP on SDN controller
        'configure terminal',
        'bgp 200',  # Replace with your SDN Controller BGP ASN
        'neighbor 172.24.4.11 remote-as 100',  # Configure BGP peering with FRR
        'exit',  # Exit bgp configuration
        'exit',  # Exit configuration terminal
        'write memory'  # Save configuration
    ]

    # Send commands to configure SDN Controller BGP
    output = ssh_conn.send_config_set(sdn_controller_config_commands)

    # Print the output for verification
    print(output)

    # Disconnect SSH session
    ssh_conn.disconnect()

def main():
    # Configure FRR BGP peering
    configure_frr_ssh()

    # Wait for a few seconds before configuring SDN Controller to ensure FRR is up and running
    time.sleep(5)

    # Configure SDN Controller BGP peering
    configure_sdn_controller_ssh()

if __name__ == "__main__":
    main()