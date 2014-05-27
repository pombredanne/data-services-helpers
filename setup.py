from distutils.core import setup
setup(name='dshelpers',
      version='1.0.4',
      description="Provides some helpers functions used by the ScraperWiki Data Services team.",
      long_description="Provides some helpers functions used by the ScraperWiki Data Services team.",
      classifiers=["Development Status :: 5 - Production/Stable",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: POSIX :: Linux",
                   "Programming Language :: Python",
                   ],
      author="ScraperWiki Limited",
      author_email='dataservices@scraperwiki.com',
      url='http://scraperwiki.com',
      license='BSD',

      py_modules=['dshelpers'],
      install_requires=['requests',
                        'requests_cache',
                        'mock',
                        'nose',
                        'scraperwiki'],
     )
