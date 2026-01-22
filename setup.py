"""
Setup script for Agri-agent
"""
from setuptools import setup, find_packages

setup(
    name="agri-agent",
    version="1.0.0",
    description="AI-powered web platform for smart and sustainable agriculture",
    author="Agri-agent Team",
    author_email="contact@agri-agent.com",
    url="https://github.com/yourusername/agri-agent",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.28.1",
        "pandas>=2.0.3",
        "numpy>=1.24.3",
        "scikit-learn>=1.3.2",
        "torch>=2.0.1",
        "torchvision>=0.15.2",
        "pillow>=10.0.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "langchain>=0.0.340",
        "langchain-openai>=0.0.0",
        "openai>=1.3.6",
        "transformers>=4.35.0",
        "plotly>=5.17.0",
        "seaborn>=0.13.0",
        "matplotlib>=3.7.2",
        "sqlalchemy>=2.0.21",
        "pydantic>=2.5.0",
        "beautifulsoup4>=4.12.2",
        "lxml>=4.9.3",
        "flask>=3.0.0",
        "flask-cors>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.9.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "agri-agent=main:main",
        ]
    },
)
