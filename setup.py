from setuptools import setup, find_packages

setup(
        name = 'klipperscreen',
        version = '0.1.6',
        description = 'Klipper Screen',
        author = 'Jordan Ruthe',
        author_email = 'jordan.ruthe@gmail.com',
        license = 'GPLv3',
        packages = find_packages(),
        install_requires = [
            'humanize==3.5.0',
            'jinja2==2.11.3',
            'matplotlib==3.4.1',
            'netifaces==0.10.9',
            'requests==2.25.1',
            'vext==0.7.6',
            'websocket-client==0.59.0'
            ],
        include_package_data = True,
        zip_safe = False)
