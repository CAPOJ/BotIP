def convert_subnet_mask_to_cidr(subnet_mask):
    """
    Преобразует маску подсети в формате 255.255.255.0 в формат /nn.
    """
    octets = [int(octet) for octet in subnet_mask.split('.')]
    cidr_prefix = sum([bin(octet).count('1') for octet in octets])
    return f'/{cidr_prefix}'


def convert_cidr_to_subnet_mask(cidr):
    """
    Преобразует маску подсети в формате /nn в формат 255.255.255.0.
    """
    prefix_length = int(cidr.replace('/', ''))
    subnet_mask = []
    for i in range(4):
        if i < prefix_length // 8:
            subnet_mask.append('255')
        elif i == prefix_length // 8:
            subnet_mask.append(str(256 - 2 ** (8 - (prefix_length % 8))))
        else:
            subnet_mask.append('0')
    return '.'.join(subnet_mask)