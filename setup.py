from setuptools import setup, find_packages
import customadmin

setup(
    name='twentytab-customadmin',
    version=customadmin.__version__,
    description='A django app to customize your admin interface with icons for applications and models and other stuffs',
    author='20tab S.r.l.',
    author_email='info@20tab.com',
    url='https://github.com/20tab/twentytab-customadmin',
    license='MIT License',
    install_requires=[
        'Django >=1.6',
        'Pillow >=2.3',
        'django-imagekit >=3.2',
        'django-colorful >=1.0.1',
        'twentytab-utils',
        'twentytab-sortable',
        'django-rosetta >=0.7.3',
        'twentytab-inspectmodel',
        'twentytab-image-ui'
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.html', '*.css', '*.js', '*.gif', '*.png', ],
}
)
