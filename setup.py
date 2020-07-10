from setuptools import setup

setup(name='MyWiFi',
      description='WiFi module in Python for Windows',
      #long_description=long_description,
      version='3.0.1',
      url='https://github.com/ShakilShaikh/MyWiFi',
      author='Shakil Ibne Shaikh',
      author_email='kingshakil55@gmail.com',
      license='Apache2',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 2.7',
          'Operating System :: Microsoft :: Windows :: Windows 7',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Security',
          'Topic :: System',
          'Topic :: Utilities',
      ],
      packages=['MyWiFi'],
      #data_files=[('lib\\site-packages\\',["MyWiFi.inf"])],
      entry_points={
          'console_scripts': [
              #'MyWiFi=WiFi.main:run'
          ],
      }
)
