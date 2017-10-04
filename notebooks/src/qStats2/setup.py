from setuptools import setup, find_packages

setup( name='qStats',
        version='0.1',
        description='Moab queue stat report generator',
        author='Albert DeFusco',
        license='MIT',
        packages=['qstats', 'qstats.tests'],

        package_data= {
            'qstats.tests' : ['data/*']
            },

        entry_points = {
            'scripts':'qstats = qstats.__main__:main'
            }

        )

