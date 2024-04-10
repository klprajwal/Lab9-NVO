from openstack import connection

def create_instance(conn, name, vnet_name, image_name, flavor_name):
    vnet = conn.network.find_network(vnet_name)
    image = conn.compute.find_image(image_name)
    flavor = conn.compute.find_flavor(flavor_name)

    server_attrs = {
        'name': name,
        'networks': [{'uuid': vnet.id}],
        'flavor_id': flavor.id,
        'image_id': image.id
    }

    print(f"Creating instance: {name} in network: {vnet_name}")
    conn.compute.create_server(**server_attrs)

def main():
    auth_args = {
        'auth_url': 'http://198.11.21.50/identity',
        'project_name': 'admin',
        'username': 'admin',
        'password': 'secret',
        'domain_name': 'Default'
    }

    conn = connection.Connection(**auth_args)

    create_instance(conn, 'VM1', 'Vnet1', 'Mininet', 'ds4G')
    create_instance(conn, 'VM2', 'Vnet2', 'Mininet', 'ds4G')
    create_instance(conn, 'VM3', 'Vnet2', 'Mininet', 'ds4G')

if __name__ == '__main__':
    main()