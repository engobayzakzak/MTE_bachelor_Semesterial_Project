from setuptools import find_packages, setup

package_name = 'comm_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
	    'heartbeat = comm_sim.heartbeat:main',
	    'pos_pub = comm_sim.pos_pub:main',
	    'lora_bridge = comm_sim.lora_bridge:main',
	    'prime_transmitter = comm_sim.prime_transmitter:main',
	    'sentinel_receiver = comm_sim.sentinel_receiver:main',
	    'motor_fault = comm_sim.motor_fault:main',
	    'motor_monitor = comm_sim.motor_monitor:main',
            'power_faults = comm_sim.power_faults:main',
            'prime_faults = comm_sim.prime_faults:main',
            'sentinel_faults = comm_sim.sentinel_faults:main',
            'prime_monitor = comm_sim.prime_monitor:main',
            'sentinel_heartbeat = comm_sim.sentinel_heartbeat:main',
        ],
    },
)
