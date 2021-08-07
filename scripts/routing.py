routes = [
    [ "192.46.3.21", "/20", "Ganymede" ],
    [ "192.46.10.218", "/16", "Callisto" ],
    [ "79.26.179.45", "/24", "Europa" ],
    [ "79.163.93.129", "/32", "Io" ],
    [ "0.0.0.0", "/0", "Jupiter" ],
]

lookups = [
    "79.26.179.16",
    "192.46.154.89",
    "79.163.93.97",
    "79.163.93.129",
    "192.46.9.72"
    # "",
    # "",
]



from rich import print
from rich.pretty import pprint

def b(num):
    return format(num, "b")
    
def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value) + "\n")
         
def prepare_routes(routes):
    _routes = []
    for route in routes:
        ip, pref, gate = route
        
        if "/" in pref:
            mask_bits = int(pref[1:])
            _addr = "1"*mask_bits + "0"*(32-mask_bits)
            block = ""
            addr = ""
            for bit in _addr:
                if len(block) == 8:
                    addr += str(int(block, 2) - 0) + "."
                    block = ""
                    
                block += bit
            
            addr += str(int(block, 2) - 0)
            # print(addr)
            pref = addr
            
        _routes.append([ip, pref, gate])
            
    return _routes

def ipv42int(addr: str) -> int:
    return sum([int(b) << ((3 - i) * 8) for i, b in enumerate(addr.split('.'))])

class RoutingTable(object):
    """
    Routing table for static routing.

    It holds a list of static routes that can be queried to find the gateway which can reach the destination.
    """

    ERROR_NO_ROUTE: int = -1
    table = []

    def add_route(self, network_prefix: int, subnet_mask: int, gateway: int) -> None:
        """
        Adds a route to the routing table.

        :param network_prefix: Network prefix
        :param subnet_mask: Subnet mask
        :param gateway: Gateway
        """

        self.table.append([network_prefix, subnet_mask, gateway])
        
    def lookup_route(self, address: int) -> int:
        """
        Queries the routing table to determine which gateway can reach the desired network the IP address belongs to.

        :param address: The IP address we want to route to.
        :return: The gateway that can reach the desired network,
        or ERROR_NO_ROUTE when no route to that network can be found.
        """
        for route in self.table:
            network_prefix, subnet_mask, gateway = route
            if network_prefix & subnet_mask == address & subnet_mask:
                return gateway
        
        return self.ERROR_NO_ROUTE
 



rt = RoutingTable()
res = {}

routes = prepare_routes(routes)
print('adding routes...', routes)

for route in routes:
    ip, mask, gate = route
    rt.add_route(ipv42int(ip), ipv42int(mask), gate)

for lookup in lookups:
    res[lookup] = rt.lookup_route(ipv42int(lookup))

print("\n--------\n")
pprint(res, expand_all=True)

