from utils import find_port

class HiddenService(object):

    def __init__(self, port=None, key_file=None):
        if port is None:
            port = find_port()
        self.port = int(port)
        self.key_file = key_file
        self.__start_service()

    def __start_service(self):
        from os import path
        from stem.control import Controller
        # Create controller
        controller = Controller.from_port(address='127.0.0.1', port=9151)
        controller.authenticate(password='')
        options = {'await_publication': True}
        # Read key from file if file provided and exists
        if self.key_file is not None and path.exists(self.key_file):
            fp = open(self.key_file, 'r')
            key_parts = fp.read().split(':', 1)
            options['key_type'], options['key_content'] = key_parts
            fp.close()
        # Create hidden service
        service = controller.create_ephemeral_hidden_service(
            {80: self.port},
            **options
        )
        # Write key if a file is provided
        if self.key_file is not None:
            data = '{}:{}'.format(
                service.private_key_type,
                service.private_key,
            )
            fp = open(self.key_file, 'w')
            fp.write(data)
            fp.close()
        self.service = service
        self.onion = '{}.onion'.format(service.service_id)
