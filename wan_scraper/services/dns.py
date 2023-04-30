from dns import resolver
import random
import logging

class DNSService:
    tlds = []
    servers = []
    resolver = None
    root_servers = []
    root_server = None
    domains = []
    ipv4s = []

    def __init__(
        self,
        tlds = ['com', 'net', 'org', 'info', 'biz', 'name', 'pro', 'mobi', 'io'],
        servers = ['8.8.8.8', '8.8.4.4']
    ):
        self.tlds = tlds
        self.servers = servers
        self.resolver = resolver.Resolver()
        self.resolver.nameservers = self.servers
        self.root_servers = self.get_root_servers()
        self.root_server = random.choice(self.root_servers)
        self.domains = self.get_random_domains()

    def get_root_servers(self):
        tlds = self.resolver.query('.', 'NS')
        return [str(tld.target)[:-1] for tld in tlds]

    def get_random_domains(self, n = 10):
        domains = []
        for i in range(n):
            # generate a random string of 10 characters
            subdomain = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
            domain = subdomain + random.choice(self.tlds)

            try:
                # query the DNS server for the domain's IP address
                answers = resolver.query(domain)
                self.ipv4s.append(str(answers))
                # if we get here, the domain exists and we can add it to the list
                domains.append(domain)
            except Exception as e:
                # if the domain doesn't exist, ignore it and try again
                logging.error(e)
                pass
        return domains

    def dump(self):
        logging.info(f'--- DNS Service State ---')
        for attr, value in vars(self).items():
            if not callable(value):
                logging.info(f"{attr}: {value}")
        logging.info(f'--- EOF DNS Service ---')
