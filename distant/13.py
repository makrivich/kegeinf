from ipaddress import ip_network
a=[]
for m in range(256):
    n=ip_network(f'84.23.84.23/255.255.255.{m}',0)
    if str(n.network_address)=='84.23.84.0':
        a.append(255+m)
print(max(a))
