from openstack import connection

def create_security_group(conn, name):
    security_group = conn.network.create_security_group(name=name)
    return security_group

def create_security_group_rule(conn, security_group_id):
    rule_attrs = {
        'direction': 'ingress',
        'ethertype': 'IPv4',
        'remote_ip_prefix': '0.0.0.0/0',
        'security_group_id': security_group_id,
    }
    print(f"Creating security group rule for security group: {security_group_id}")
    conn.network.create_security_group_rule(**rule_attrs)

def main():
    auth_args = {
        'auth_url': 'http://198.11.21.50/identity',
        'project_name': 'admin',
        'username': 'admin',
        'password': 'secret',
        'domain_name': 'Default'
    }

    conn = connection.Connection(**auth_args)

    sg = create_security_group(conn, 'nsg_for_vnet1_vnet2')
    create_security_group_rule(conn, sg.id)

if __name__ == '__main__':
    main()