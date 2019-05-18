from distutils.core import setup

setup(name='flight_status',
      version=1.0,
      packages=['bin'],
      package_data={'graphics': ['/*.gif']},
      scripts=['inter.py']
      )
