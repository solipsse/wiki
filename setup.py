from setuptools import setup, find_packages

setup(
    name='mkdocs-preprocess-c-code',
    version='0.1',
    description='MkDocs plugin to preprocess C code blocks',
    keywords='mkdocs python markdown',
    packages=find_packages(include=['mkdocs_plugins', 'mkdocs_plugins.*']),  # Explicitly include the plugins package
    entry_points={
        'mkdocs.plugins': [
            'preprocess_c_code = mkdocs_plugins.preprocess_c_code:PreprocessCCodePlugin'
        ]
    },
    zip_safe=False
)
