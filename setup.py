from setuptools import setup

setup(
    name="UofG Timetable CLI",
    version="0.1",
    py_modules=['extractor'],
    install_requires = [
        'Click',
        'requests',
        'pytz'
    ],
    entry_points='''
        [console_scripts]
        timetable_2=extractor:cli
    ''',
)