from setuptools import setup


with open('README.md', encoding='utf-8') as fp:
    long_description = fp.read()


setup(
    name='scia',
    version='1.0.2',
    packages=['scia', 'scia.handlers'],
    url='https://github.com/crogeo/scia',
    license='MIT License',
    author='crogeo.org',
    author_email='',
    description='Python logging extension',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
