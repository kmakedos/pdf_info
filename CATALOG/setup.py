import setuptools
if __name__ == '__main__':
    setuptools.setup(
        name='pdfcatalogue',
        version='0.1',
        packages=setuptools.find_packages(),
        entry_points={
            'console_scripts': {
                'pdfcatalogue = catalogue.pdfcatalogue:main'
            },
        },
        install_requires=[
        ],
        test_require = ['pytest'],
        description = 'PDF Catalogue Tool',
        author = 'Kostas Makedos',
        author_email = 'kostas.makedos@gmail.com',
        classifiers = [ 'Development Status :: 3 - Alpha'
                       'Intended Audience :: Developers',
                       'Topic :: Software Development :: API Tools',
                       'Programming Language :: Python :: 3'
                      ],
    )
