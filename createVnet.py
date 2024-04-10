from openstack import connection

def create_network(conn, name, subnet_name, cidr):
    network_attrs = {
        'name': name,
        'shared': True
    }
    print(f"Creating network: {name}")
    network = conn.network.create_network(**network_attrs)

    subnet_attrs = {
        'network_id': network.id,
        'name': subnet_name,
        'cidr': cidr,
        'ip_version': 4  # Add ip_version attribute
    }
    print(f"Creating subnet: {subnet_name} for network: {name}")
    subnet = conn.network.create_subnet(**subnet_attrs)

def connect_router_to_networks(conn, router_name, vnet_names):
    router = conn.network.find_router(router_name)

    for vnet_name in vnet_names:
        vnet = conn.network.find_network(vnet_name)
        subnet_ids = vnet.subnet_ids
        for subnet_id in subnet_ids:
            conn.network.add_interface_to_router(router, subnet_id=subnet_id)

def main():
    auth_args = {
        'auth_url': 'http://198.11.21.50/identity',
        'project_name': 'admin',
        'username': 'admin',
        'password': 'secret',
        'domain_name': 'Default'
    }

    conn = connection.Connection(**auth_args)

    create_network(conn, 'Vnet1', 'subnet1', '10.1.1.0/24')
    create_network(conn, 'Vnet2', 'subnet2', '10.2.2.0/24')

    router_name = 'myrouter'
    connect_router_to_networks(conn, router_name, ['Vnet1', 'Vnet2'])

if __name__ == '__main__':
    main()