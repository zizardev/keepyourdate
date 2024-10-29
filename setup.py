from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='keepyourdate',
  version='0.0.1',
  author='Mishalov_Bogdan',
  author_email='bogdanmissss@gmail.com',
  description='Simple daily event keeper.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/zizardev/datekeeper',
  packages=find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='calendar keep date',
  project_urls={
    'GitHub': 'https://github.com/zizardev/datekeeper'
  },
  python_requires='>=3.6'
)