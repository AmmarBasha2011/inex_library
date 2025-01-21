from setuptools import setup, find_packages

setup(
    name='inex-library',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'fastapi>=0.68.0',  # Core FastAPI framework
        'uvicorn>=0.15.0',  # ASGI server for FastAPI
        'starlette>=0.14.0',  # Web framework toolkit
        'pydantic>=1.8.0',  # Data validation
        'flask>=2.0.0',  # Flask web framework
        'pycryptodome>=3.10.0',  # For AES and Blowfish encryption
        'cryptography>=3.4.0',  # For additional cryptographic operations
        'requests>=2.26.0',  # HTTP requests
        'openai>=1.0.0',
        'python-jose>=3.3.0',  # For JWT handling
        'passlib>=1.7.4',  # For password hashing
        'pyjwt>=2.1.0',  # For JWT operations
        'pynacl>=1.4.0',  # For cryptographic signing
        'python-multipart>=0.0.5',  # For handling form data in FastAPI
        'python-dotenv>=0.19.0',
        'aiofiles>=0.7.0',  # For async file operations
        'watchdog>=2.1.0',  # For file system monitoring
        'pathlib>=1.0.1',  # For path manipulation
        'pyotp>=2.6.0',  # For 2FA operations
        'python-ipaddress>=1.0.0',  # For IP validation
        'moviepy>=1.0.3',  # For video creation and editing
        'googletrans>=3.1.0a0',  # For text translation
        'pillow>=8.3.0',  # For image processing
        'web3>=5.24.0',  # For blockchain interactions
        'sqlalchemy>=1.4.0',  # For advanced database operations
        'alembic>=1.7.0',  # For database migrations
        'sqlcipher3>=0.4.5',  # For database encryption
        'twine>=3.4.2',  # For PyPI package distribution
        'wheel>=0.37.0',  # For building wheel distributions
        'setuptools>=57.0.0',  # For package setup
        'build>=0.7.0',  # For building Python packages
        'colorama>=0.4.4',  # For colored terminal output
        'termcolor>=1.1.0',  # For terminal text styling
        'rich>=10.12.0',  # For rich text and formatting
        'bcrypt>=3.2.0',  # For password hashing
        'pyOpenSSL>=20.0.0',  # For SSL/TLS operations
        'cryptography-vectors>=3.4.0',  # Test vectors for cryptography
        'python-magic>=0.4.24',  # For file type detection
        'redis>=4.0.0',  # For rate limiting and caching
        'bleach>=4.1.0',  # For input sanitization
        'validators>=0.18.0',  # For URL validation
        'gunicorn>=20.1.0',  # Production WSGI server
        'hypercorn>=0.11.0',  # Alternative ASGI server
        'werkzeug>=2.0.0',  # WSGI utilities
        'click>=8.0.0',  # Command line interface
        'jinja2>=3.0.0',  # Template engine
        'itsdangerous>=2.0.0',  # Data signing
        'psutil>=5.8.0',  # System and process utilities
        'pywin32>=300; platform_system == "Windows"',  # Windows system utilities
        'pyuac>=0.0.3; platform_system == "Windows"',  # Windows UAC support
        'elevate>=0.1.3',  # Cross-platform privilege elevation
        'opencv-python>=4.5.0',  # For video processing
        'numpy>=1.21.0',  # For numerical operations
        'ffmpeg-python>=0.2.0',  # For video encoding/decoding
        'beautifulsoup4>=4.9.0',  # For web scraping
        'selenium>=4.0.0',  # For web automation
        'playwright>=1.20.0',  # Modern web automation
        'urllib3>=1.26.0',  # HTTP client
        'aiohttp>=3.8.0',  # Async HTTP client
        'httpx>=0.23.0',  # Modern HTTP client
    ],
    extras_require={
        'dev': [
            'pytest>=6.2.0',
            'black>=21.7b0',
            'isort>=5.9.0',
            'flake8>=3.9.0',
            'httpx>=0.18.0',  # For FastAPI testing
            'pytest-asyncio>=0.15.0',  # For async tests
            'safety>=1.10.0',  # For security vulnerability checking
            'bandit>=1.7.0',  # For security linting
            'locust>=2.8.0',  # For load testing
            'coverage>=6.2',  # For code coverage
            'pytest-cov>=3.0.0',  # For pytest coverage
        ],
        'database': [
            'psycopg2-binary>=2.9.0',  # PostgreSQL support
            'pymysql>=1.0.0',  # MySQL support
            'sqlcipher3>=0.4.5',  # Database encryption
            'cryptography>=3.4.0',  # For database encryption
        ],
        'crypto': [
            'pyOpenSSL>=20.0.0',  # For SSL/TLS operations
            'cryptography-vectors>=3.4.0',  # Test vectors for cryptography
            'bcrypt>=3.2.0',  # For password hashing
            'pynacl>=1.4.0',  # For cryptographic signing
            'pyotp>=2.6.0',  # For 2FA operations
            'qrcode>=7.3.0',  # For 2FA QR codes
        ],
        'server': [
            'gunicorn>=20.1.0',  # Production WSGI server
            'hypercorn>=0.11.0',  # Alternative ASGI server
            'fastapi-utils>=0.2.0',  # Additional FastAPI utilities
            'fastapi-jwt-auth>=0.5.0',  # JWT authentication
            'fastapi-cache>=0.1.0',  # Response caching
            'fastapi-limiter>=0.1.5',  # Rate limiting
            'secure>=0.3.0',  # Security headers
            'flask-cors>=3.0.0',  # CORS support for Flask
            'flask-compress>=1.10.0',  # Response compression
            'flask-caching>=1.10.0',  # Flask caching
            'flask-limiter>=2.5.0',  # Flask rate limiting
            'flask-talisman>=0.8.0',  # Security headers for Flask
            'flask-seasurf>=0.3.0',  # CSRF protection
            'prometheus-flask-exporter>=0.18.0',  # Metrics
            'sentry-sdk>=1.5.0',  # Error tracking
            'supervisor>=4.2.0',  # Process management
            'nginx>=1.20.0',  # Reverse proxy
        ],
        'files': [
            'watchdog>=2.1.0',  # File system monitoring
            'pathlib>=1.0.1',  # Path manipulation
            'send2trash>=1.8.0',  # Safe file deletion
            'python-magic>=0.4.24',  # File type detection
            'aiofiles>=0.7.0',  # Async file operations
            'filetype>=1.0.0',  # File type validation
        ],
        'packaging': [
            'twine>=3.4.2',  # PyPI package distribution
            'wheel>=0.37.0',  # Wheel distribution building
            'build>=0.7.0',  # Python package building
            'check-manifest>=0.47.0',  # Package manifest verification
            'readme-renderer>=29.0',  # README rendering for PyPI
            'keyring>=23.0.1',  # Secure credential storage
        ],
        'styling': [
            'colorama>=0.4.4',  # Colored terminal output
            'termcolor>=1.1.0',  # Terminal text styling
            'rich>=10.12.0',  # Rich text and formatting
            'blessed>=1.19.0',  # Terminal styling
            'prompt-toolkit>=3.0.20',  # Interactive prompts
        ],
        'security': [
            'cryptography>=3.4.0',  # Core cryptography
            'pycryptodome>=3.10.0',  # Additional crypto algorithms
            'python-jose>=3.3.0',  # JWT handling
            'passlib>=1.7.4',  # Password hashing
            'bcrypt>=3.2.0',  # Password hashing
            'pyotp>=2.6.0',  # 2FA
            'qrcode>=7.3.0',  # 2FA QR codes
            'redis>=4.0.0',  # Rate limiting
            'bleach>=4.1.0',  # Input sanitization
            'validators>=0.18.0',  # URL validation
            'python-ipaddress>=1.0.0',  # IP validation
            'secure>=0.3.0',  # Security headers
            'pyOpenSSL>=20.0.0',  # SSL/TLS
            'safety>=1.10.0',  # Vulnerability checking
            'bandit>=1.7.0',  # Security linting
        ],
        'system': [
            'psutil>=5.8.0',  # System and process utilities
            'pywin32>=300; platform_system == "Windows"',  # Windows system utilities
            'pyuac>=0.0.3; platform_system == "Windows"',  # Windows UAC support
            'elevate>=0.1.3',  # Cross-platform privilege elevation
            'distro>=1.6.0',  # Linux distribution info
            'py-cpuinfo>=8.0.0',  # CPU information
            'gputil>=1.4.0',  # GPU utilities
            'psutil>=5.8.0',  # Process and system utilities
            'pyusb>=1.2.0',  # USB device management
            'pyserial>=3.5',  # Serial port communication
            'netifaces>=0.11.0',  # Network interfaces
            'ifaddr>=0.1.7',  # Network interface addresses
        ],
        'translation': [
            'googletrans>=3.1.0a0',  # Google Translate API
            'translate>=3.6.1',  # Translation utilities
            'deep-translator>=1.8.3',  # Multiple translation services
            'langdetect>=1.0.9',  # Language detection
            'polyglot>=16.7.4',  # Natural language processing
            'pycld2>=0.41',  # Compact Language Detector
            'langid>=1.1.6',  # Language identification
            'mtranslate>=1.8',  # Microsoft Translator API
            'textblob>=0.17.1',  # Text processing and translation
            'lingua>=4.15.0',  # Language detection
        ],
        'video': [
            'moviepy>=1.0.3',  # Video editing
            'opencv-python>=4.5.0',  # Video processing
            'numpy>=1.21.0',  # Numerical operations
            'ffmpeg-python>=0.2.0',  # Video encoding/decoding
            'pillow>=8.3.0',  # Image processing
            'imageio>=2.9.0',  # Image I/O
            'imageio-ffmpeg>=0.4.5',  # FFmpeg support
            'scikit-image>=0.18.0',  # Image processing
            'scipy>=1.7.0',  # Scientific computing
            'av>=9.0.0',  # PyAV for fast video processing
            'python-vlc>=3.0.0',  # VLC bindings
            'pims>=0.5.0',  # Video frame access
        ],
        'web': [
            'beautifulsoup4>=4.9.0',  # Web scraping
            'selenium>=4.0.0',  # Web automation
            'playwright>=1.20.0',  # Modern web automation
            'requests>=2.26.0',  # HTTP requests
            'urllib3>=1.26.0',  # HTTP client
            'aiohttp>=3.8.0',  # Async HTTP client
            'httpx>=0.23.0',  # Modern HTTP client
            'html5lib>=1.1',  # HTML parser
            'lxml>=4.9.0',  # XML/HTML processing
            'webdriver-manager>=3.5.0',  # Webdriver management
            'pyppeteer>=1.0.0',  # Headless Chrome/Chromium
            'requests-html>=0.10.0',  # HTML parsing
            'mechanize>=0.4.0',  # Stateful programmatic web browsing
            'scrapy>=2.5.0',  # Web crawling
            'pyquery>=1.4.0',  # jQuery-like HTML parsing
        ],
        'video': [
            'moviepy>=1.0.3',  # Video editing
            'opencv-python>=4.5.0',  # Video processing
            'numpy>=1.21.0',  # Numerical operations
            'ffmpeg-python>=0.2.0',  # Video encoding/decoding
            'pillow>=8.3.0',  # Image processing
            'imageio>=2.9.0',  # Image I/O
            'imageio-ffmpeg>=0.4.5',  # FFmpeg support
            'scikit-image>=0.18.0',  # Image processing
            'scipy>=1.7.0',  # Scientific computing
            'av>=9.0.0',  # PyAV for fast video processing
            'python-vlc>=3.0.0',  # VLC bindings
            'pims>=0.5.0',  # Video frame access
        ],
        'translation': [
            'googletrans>=3.1.0a0',  # Google Translate
            'deep-translator>=1.9.0',  # Multiple translation services
            'langdetect>=1.0.9',  # Language detection
            'polyglot>=16.7.4',  # Natural language processing
            'textblob>=0.17.1',  # Text processing
            'mtranslate>=1.8',  # Microsoft Translator API
            'textblob>=0.17.1',  # Text processing and translation
            'lingua>=4.15.0',  # Language detection
        ],
    },
    description='A comprehensive Python library for AI integration, web development with FastAPI/Flask, advanced encryption, secure database management, file operations, library development, text styling, system management, translation services, video creation, web automation, and cryptocurrency token analysis. Features include JWT handling, password management, rate limiting, input sanitization, and more.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='INEX Team',
    author_email='pbstzidr@ywp.freewebhostmost.com',
    url='https://github.com/AmmarBasha2011/inex_library',
    project_urls={
        'Documentation': 'https://pypi.org/project/inex',
        'Source': 'https://github.com/AmmarBasha2011/inex_library',
        'Tracker': 'https://github.com/AmmarBasha2011/inex_library/issues',
        'Download': 'https://pypi.org/project/inex#files',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Security :: Cryptography',
        'Topic :: Database',
        'Topic :: System :: Systems Administration',
        'Topic :: Text Processing :: General',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',
        'Topic :: Text Processing :: General',
        'Topic :: Utilities',
        'Natural Language :: English',
        'Natural Language :: Arabic',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: French',
        'Natural Language :: German',
        'Natural Language :: Italian',
        'Natural Language :: Japanese',
        'Natural Language :: Korean',
        'Natural Language :: Portuguese',
        'Natural Language :: Russian',
        'Natural Language :: Spanish',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Framework :: FastAPI',
        'Framework :: Flask',
    ],
    python_requires='>=3.7',
    keywords='ai, gemini, chatgpt, deepseek, web development, fastapi, asgi, server, cors, uvicorn, encryption, aes, blowfish, base64, secure database, sqlite, sqlcipher, flask, crypto, security, blockchain, binance, ethereum, cryptocurrency, file management, file operations, library development, package distribution, text styling, terminal output, jwt, password, rate limiting, input sanitization, 2fa, authentication, wsgi, asgi, gunicorn, nginx, system management, process control, hardware monitoring, translation, language detection, nlp, video creation, video editing, multimedia, web automation, web scraping, browser control',
)
