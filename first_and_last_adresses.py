def find_network_addresses(ip_address, subnet_mask):
    ip_parts = [int(part) for part in ip_address.split('.')]
    mask_parts = [int(part) for part in subnet_mask.split('.')]

    # Вычисляем сетевой адрес
    network_address = [ip_part & mask_part for ip_part, mask_part in zip(ip_parts, mask_parts)]

    # Вычисляем широковещательный адрес
    broadcast_address = [network_address[i] | (255 - mask_part) for i, mask_part in enumerate(mask_parts)]

    # Вычисляем минимальный и максимальный IP-адреса
    min_ip = '.'.join(str(part) for part in [network_address[0], network_address[1], network_address[2], network_address[3] + 1])
    max_ip = '.'.join(str(part) for part in [broadcast_address[0], broadcast_address[1], broadcast_address[2], broadcast_address[3] - 1])

    return (min_ip, max_ip)
