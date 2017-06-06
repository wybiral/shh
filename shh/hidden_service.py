import os.path
from stem.control import Controller
from .utils import find_port

class HiddenService(object):

    def __init__(
            self,
            ports=None,
            control_port=9051,
            key_raw=None,
            key_file=None,
            await_publication=True):
        if ports is None:
            ports = {80: find_port()}
        self.ports = ports
        self.control_port = control_port
        self._key = None
        self._key_file = key_file
        if key_raw is not None:
            # Read key from string
            self._key = key_raw.split(':', 1)
        elif key_file is not None and os.path.exists(key_file):
            # Read key from file if file exists
            fp = open(key_file, 'r')
            self._key = fp.read().split(':', 1)
            fp.close()
        self.__start_service(await_publication)

    def __start_service(self, await_publication):
        # Create controller
        controller = Controller.from_port(
            address='127.0.0.1',
            port=self.control_port
        )
        controller.authenticate(password='')
        options = {}
        options['await_publication'] = await_publication
        if self._key is not None:
            options['key_type'] = self._key[0]
            options['key_content'] = self._key[1]
        # Create hidden service
        service = controller.create_ephemeral_hidden_service(
            self.ports,
            **options
        )
        if self._key is None:
            self._key = (service.private_key_type, service.private_key)
        # Write key if a file is provided
        if self._key_file is not None and not os.path.exists(self._key_file):
            self.save_key(self._key_file)
        self.service = service
        self.onion = '{}.onion'.format(service.service_id)

    def get_key(self):
        return '{}:{}'.format(self._key[0], self._key[1])

    def save_key(self, filename):
        fp = open(filename, 'w')
        fp.write(self.get_key())
        fp.close()