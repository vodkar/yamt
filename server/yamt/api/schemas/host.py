from yamt.api.schemas.available_services import AvailableServices
from yamt.hosts.models.host import Host
from yamt.tcp_services.services.ssh.models import SSHPasswordAuthentication


class ExtendedHost(Host):
    available_services: AvailableServices
    ssh_creds: SSHPasswordAuthentication | None
