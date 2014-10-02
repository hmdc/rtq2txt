from setuptools import setup, find_packages
setup(name='rtq2txt',
      version='0.1',
      description='Reads tickets from an Request Tracker (RT) queue and outputs them in .txt',
      url='https://github.com/hmdc/rtq2txt',
      author='Evan Sarmiento',
      author_email='esarmien@g.harvard.edu',
      license='MIT',
      packages=['rtq2txt'],
      install_requires=['rt'],
      scripts=['scripts/rtq_mark_spam.sh', 'scripts/do_rtq2txt.py']
)
