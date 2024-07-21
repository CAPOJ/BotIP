#ПРимер использования
#
# ip_address = "172.16.5.150"
# subnet_mask = "255.255.240.0"
#
# first_address, last_address = find_network_addresses(ip_address, subnet_mask)
#
# print(f"Первый адрес в подсети: {first_address}")
# print(f"Последний адрес в подсети: {last_address}")


from transform_mask import convert_subnet_mask_to_cidr, convert_cidr_to_subnet_mask
# temp1 = '224.0.0.0'
# temp2 = '/31'
# print(convert_subnet_mask_to_cidr(temp1))
# print(convert_cidr_to_subnet_mask(temp2))

from check_for_correct_mask import check_for
# temp1 = "178.141.67.193/32"
# ip, msk = check_for(temp1)

from is_right_ip import bitwise_multiply_ip_and_mask
tempip = '192.168.7.23'
tempadress = '/24'
result_ip = bitwise_multiply_ip_and_mask(tempip, tempadress)
print(result_ip)