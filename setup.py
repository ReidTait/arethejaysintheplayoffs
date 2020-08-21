from setuptools import setup

setup(
    name='arethejaysintheplayoffs',
    version='0.1',
    py_modules=['arethejaysintheplayoffs'],
    install_requires=[
        'Click',
        'MLB-StatsAPI',
    ],
    entry_points='''
        [console_scripts]
        arethejaysintheplayoffs=arethejaysintheplayoffs:cli
    ''',
)
