def bitwise_multiply_ip_and_mask(ip_address, cidr_mask):
    """
    Выполняет побитовое умножение IP-адреса и маски подсети.

    Args:
        ip_address (str): IP-адрес в формате "a.b.c.d".
        cidr_mask (str): Маска подсети в формате "/n".

    Returns:
        str: Результат побитового умножения IP-адреса и маски подсети в формате "a.b.c.d".
    """
    # Преобразуем IP-адрес в двоичное представление
    ip_octets = [int(octet) for octet in ip_address.split('.')]
    ip_bin = ''.join(f"{octet:08b}" for octet in ip_octets)

    # Извлекаем длину префикса из маски подсети
    prefix_length = int(cidr_mask.replace('/', ''))

    # Создаем маску подсети в двоичном формате
    mask_bin = '1' * prefix_length + '0' * (32 - prefix_length)

    # Выполняем побитовое умножение IP-адреса и маски подсети
    result_bin = bin(int(ip_bin, 2) & int(mask_bin, 2))[2:]

    # Добавляем ведущие нули, чтобы получить 32-битное двоичное представление
    while len(result_bin) < 32:
        result_bin = '0' + result_bin

    # Преобразуем результат в формат "a.b.c.d"
    result_octets = [str(int(result_bin[i:i + 8], 2)) for i in range(0, 32, 8)]
    result_ip = '.'.join(result_octets)

    return result_ip