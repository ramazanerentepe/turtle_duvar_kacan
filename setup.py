from setuptools import find_packages, setup

package_name = 'turtle_duvar'

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
    maintainer='ramazanerentepe',
    maintainer_email='teperamazaneren@gmail.com',
    description='Duvardan kacan kaplumbaga (turtlesim) dugumu',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'duvar_kacan = turtle_duvar.duvar_kacan:main'
        ],
    },
)
