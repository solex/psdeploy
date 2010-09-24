from setuptools import setup, find_packages

setup(
    name='psdeploy',
    version="0.0.1",
    description='Paster scripts and templates for PS deployments',
    author='Oleksiy Solyanyk',
    author_email='solex@odesk.com',
    license = "BSD",
    keywords = "django paster",
    install_requires=[
        'setuptools',
        'PasteScript>=1.3',
    ],
    packages = find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points="""
        [paste.paster_create_template]
        odesk_app=psdeploy.templates:OdeskAppTemplate
    """,
)
