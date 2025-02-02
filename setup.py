from setuptools import setup

setup(name='monzo',
      version='0.10.0',
      description='A python SDK for interacting with the Monzo API.',
      url='https://github.com/babolivier/monzo-python',
      author='Brendan Abolivier',
      author_email='hello@brendanabolivier.com',
      license='GPLv3',
      packages=['monzo'],
      install_requires=[
          'requests==2.20.0',
          'requests-oauthlib==1.0.0',
          'python-dotenv==0.5.1'
      ],
  )
