from setuptools import setup, find_packages

setup(
    name="revolut_lookup",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'revolut-lookup = revolut_lookup.main:get_user_profile'
        ]
    },
    author="Your Name",
    description="A simple CLI tool to fetch Revolut web profiles using the public API.",
    python_requires='>=3.6',
)
