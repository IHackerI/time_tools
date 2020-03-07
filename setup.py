from setuptools import setup, find_packages

setup(
    name="time_tools",
    version='0.0.1',
    description="Easy work for python timer",
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3'  ,
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='time python',
    author='Hacker',
    author_email='bulat.shaekhov@gmail.com',
    url='https://github.com/IHackerI/time_tools',
    packages=find_packages(),
    install_requires=
        open('requirements.txt').read().split('\n\r|\n')
    ,
    include_package_data=True,
    zip_safe=False,
)