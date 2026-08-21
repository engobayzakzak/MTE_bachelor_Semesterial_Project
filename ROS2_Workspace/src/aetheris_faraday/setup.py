from setuptools import setup

package_name = 'aetheris_faraday'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/config', ['config/faraday_params.yaml']),
        ('share/' + package_name + '/launch', ['launch/faraday_manager.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='Faraday protection manager (logical indicator for protected sensors)',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'faraday_manager = aetheris_faraday.faraday_manager:main',
        ],
    },
)
#COMMENTED||EOF
