from setuptools import setup, find_packages

setup(
    name='mcp_projects',
    version='1.0.0',
    author='jiangmingming',
    author_email='jiangmingming@sensetime.com',
    packages=find_packages(),
    install_requires=[
        'arxiv',
        'dotenv',
        'anthropic',
    ],
    python_requires='>=3.5',
)