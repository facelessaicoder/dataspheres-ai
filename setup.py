from setuptools import setup, find_packages

setup(
    name="dataspheres-ai",
    version="0.1.0",
    description="A library for managing real-time event streams and conversations for group chats involving humans and multiple AIs.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/dataspheres-ai",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "websockets"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
