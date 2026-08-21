from setuptools import setup

package_name = 'aetheris_dummy_sensors'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your@email.com',
    description='Dummy IMU and GPS publishers for testing',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dummy_imu = aetheris_dummy_sensors.dummy_imu:main',
            'dummy_gps = aetheris_dummy_sensors.dummy_gps:main',
        ],
    },
)
