from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'CoffeeBot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # Path to the launch file
        (os.path.join('share', package_name,'launch'), glob('launch/*.launch.py')),
        # Path to the maze sdf file
        (os.path.join('share', package_name,'models/coffeeShop/'), glob('./models/coffeeShop/*')),
        # Path to the world file
        (os.path.join('share', package_name,'worlds/'), glob('./worlds/*')),
        # Include config (.yaml) files
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.*yaml*'))),
        # Include map (.yaml and .pgm) files
        (os.path.join('share', package_name, 'maps'), glob(os.path.join('maps', '*.[yp][ag][m]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='harveywalker500@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
