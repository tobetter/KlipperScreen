from setuptools import setup, find_packages

setup(
        name = 'klipperscreen',
        version = '0.1.3',
        description = 'Klipper Screen',
        author = 'Jordan Ruthe',
        author_email = 'jordan.ruthe@gmail.com',
        license = 'GPLv3',
        packages = find_packages(),
        install_requires = [
            'requests==2.25.1',
            'vext==0.7.4',
            'websocket-client==0.57.0',
            'humanize==3.2.0',
            'jinja2>=2.11.2'
            ],
        include_package_data = True,
        zip_safe = False)
