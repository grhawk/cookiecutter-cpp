# !/usr/bin/env python

from distutils.core import setup
setup(
    name='cookiecutter-c++',
    packages=[],
    version='0.1.0',
    description='Cookiecutter template for a C++ software with a lib and a console in separated folders/projects',
    long_description='Cookiecutter template for a C++ software with a lib and a console in separated folders/projects. The template includes also GoogleTest examples and the possibility to embed a logging system.',
    author='Riccardo Petraglia (forked from https://github.com/audreyr/cookiecutter-pypackage)',
    license='BSD',
    author_email='riccardo.petraglia@gmail.com',
    url='https://github.com/grhawk/cookiecutter-cpp.git',
    keywords=['cookiecutter', 'template', 'package', 'c++', 'cpp', 'gtest'],
    #python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
)
