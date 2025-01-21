from cryptography.fernet import Fernet
from jose import JWTError, jwt
from passlib.context import CryptContext
import secrets
import base64
from datetime import datetime, timedelta
import hashlib
import re
import os
import string
import random
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from typing import Union, List, Tuple
import ipaddress
import urllib.parse

class Security:
    """
    Provides comprehensive security features including encryption, hashing, JWT handling, password management,
    key management, certificate operations, and various security utilities.
    """

    def __init__(self, secret_key: str = None):
        """Initialize the Security class with optional secret key."""
        self.secret_key = secret_key or secrets.token_urlsafe(32)
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.fernet = Fernet(base64.b64encode(self.secret_key.encode()[:32].ljust(32, b'0')))
        self._initialize_rsa_keys()

    def _initialize_rsa_keys(self):
        """Initialize RSA key pair for asymmetric encryption."""
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()

    def hash_password(self, password: str) -> str:
        """Hash a password using bcrypt."""
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash."""
        return self.pwd_context.verify(plain_password, hashed_password)

    def create_jwt_token(self, data: dict, expires_delta: timedelta = None) -> str:
        """Create a JWT token with optional expiration."""
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.secret_key, algorithm="HS256")

    def verify_jwt_token(self, token: str) -> dict:
        """Verify and decode a JWT token."""
        try:
            return jwt.decode(token, self.secret_key, algorithms=["HS256"])
        except JWTError as e:
            raise e

    def encrypt_data(self, data: str) -> str:
        """Encrypt data using Fernet symmetric encryption."""
        encrypted_data = self.fernet.encrypt(data.encode())
        return base64.b64encode(encrypted_data).decode()

    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt Fernet-encrypted data."""
        try:
            decrypted_data = self.fernet.decrypt(base64.b64decode(encrypted_data))
            return decrypted_data.decode()
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")

    def generate_secure_token(self, length: int = 32) -> str:
        """Generate a cryptographically secure token."""
        return secrets.token_urlsafe(length)

    def hash_file(self, file_path: str, algorithm: str = "sha256") -> str:
        """Calculate file hash using specified algorithm."""
        hash_obj = getattr(hashlib, algorithm)()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()

    def create_api_key(self, prefix: str = "sk") -> tuple:
        """Generate a secure API key with prefix."""
        raw_key = secrets.token_urlsafe(32)
        api_key = f"{prefix}_{raw_key}"
        hashed_key = hashlib.sha256(api_key.encode()).hexdigest()
        return api_key, hashed_key

    def verify_api_key(self, api_key: str, stored_hash: str) -> bool:
        """Verify an API key against its stored hash."""
        hashed_key = hashlib.sha256(api_key.encode()).hexdigest()
        return secrets.compare_digest(hashed_key, stored_hash)

    def generate_password(self, length: int = 16, include_special: bool = True) -> str:
        """
        Generate a secure password with specified requirements.
        
        Args:
            length: Length of the password
            include_special: Whether to include special characters
        """
        chars = string.ascii_letters + string.digits
        if include_special:
            chars += string.punctuation
        
        while True:
            password = ''.join(random.choice(chars) for _ in range(length))
            if (any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                (not include_special or any(c in string.punctuation for c in password))):
                return password

    def validate_password_strength(self, password: str) -> Tuple[bool, List[str]]:
        """
        Validate password strength against security requirements.
        
        Returns:
            Tuple of (is_valid, list_of_failures)
        """
        failures = []
        if len(password) < 8:
            failures.append("Password must be at least 8 characters long")
        if not any(c.islower() for c in password):
            failures.append("Password must contain lowercase letters")
        if not any(c.isupper() for c in password):
            failures.append("Password must contain uppercase letters")
        if not any(c.isdigit() for c in password):
            failures.append("Password must contain digits")
        if not any(c in string.punctuation for c in password):
            failures.append("Password must contain special characters")
        
        return len(failures) == 0, failures

    def encrypt_asymmetric(self, data: str) -> str:
        """
        Encrypt data using RSA asymmetric encryption.
        
        Returns:
            Base64 encoded encrypted data
        """
        encrypted = self.public_key.encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return base64.b64encode(encrypted).decode()

    def decrypt_asymmetric(self, encrypted_data: str) -> str:
        """
        Decrypt RSA encrypted data.
        
        Args:
            encrypted_data: Base64 encoded encrypted data
        """
        try:
            encrypted = base64.b64decode(encrypted_data)
            decrypted = self.private_key.decrypt(
                encrypted,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return decrypted.decode()
        except Exception as e:
            raise ValueError(f"Asymmetric decryption failed: {str(e)}")

    def generate_key_pair(self) -> Tuple[str, str]:
        """
        Generate RSA key pair and return as PEM strings.
        
        Returns:
            Tuple of (private_key_pem, public_key_pem)
        """
        private_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode()
        
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode()
        
        return private_pem, public_pem

    def derive_key(self, password: str, salt: bytes = None) -> Tuple[bytes, bytes]:
        """
        Derive a key from a password using PBKDF2.
        
        Args:
            password: Password to derive key from
            salt: Optional salt bytes, generated if not provided
            
        Returns:
            Tuple of (key, salt)
            
        Raises:
            ValueError: If password is empty or invalid
        """
        if not password:
            raise ValueError("Password cannot be empty")
            
        try:
            salt = salt or os.urandom(16)
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
            )
            key = kdf.derive(password.encode())
            return key, salt
        except Exception as e:
            raise ValueError(f"Key derivation failed: {str(e)}")

    def sanitize_input(self, input_str: str, allow_html: bool = False) -> str:
        """
        Sanitize input string to prevent XSS and injection attacks.
        
        Args:
            input_str: Input string to sanitize
            allow_html: Whether to allow safe HTML tags
            
        Returns:
            Sanitized string
        """
        if not isinstance(input_str, str):
            raise ValueError("Input must be a string")
            
        if not input_str:
            return ""
            
        # First pass: remove all HTML tags if not allowed
        if not allow_html:
            input_str = re.sub(r'<[^>]*>', '', input_str)
        
        # Second pass: escape special characters
        input_str = input_str.replace('&', '&amp;')
        input_str = input_str.replace('<', '&lt;')
        input_str = input_str.replace('>', '&gt;')
        input_str = input_str.replace('"', '&quot;')
        input_str = input_str.replace("'", '&#x27;')
        input_str = input_str.replace('/', '&#x2F;')
        input_str = input_str.replace('\\', '&#x5C;')
        
        # Third pass: remove potentially dangerous patterns
        input_str = re.sub(r'javascript:', '', input_str, flags=re.IGNORECASE)
        input_str = re.sub(r'data:', '', input_str, flags=re.IGNORECASE)
        input_str = re.sub(r'vbscript:', '', input_str, flags=re.IGNORECASE)
        
        return input_str

    def rate_limit_check(self, key: str, max_requests: int, time_window: int) -> Tuple[bool, int]:
        """
        Check if request should be rate limited.
        
        Args:
            key: Identifier for the rate limit (e.g., IP address)
            max_requests: Maximum number of requests allowed
            time_window: Time window in seconds
            
        Returns:
            Tuple of (is_allowed, remaining_requests)
            
        Note:
            This is a basic in-memory implementation. For production use,
            implement this using Redis or a similar distributed cache.
        """
        if not hasattr(self, '_rate_limit_store'):
            self._rate_limit_store = {}
            
        current_time = int(datetime.utcnow().timestamp())
        
        # Clean up expired entries
        if key in self._rate_limit_store:
            requests = [(ts, count) for ts, count in self._rate_limit_store[key] 
                       if current_time - ts < time_window]
        else:
            requests = []
            
        # Count total requests in window
        total_requests = sum(count for _, count in requests)
        
        # Update store
        if total_requests < max_requests:
            requests.append((current_time, 1))
            self._rate_limit_store[key] = requests
            return True, max_requests - total_requests - 1
            
        return False, 0

    def validate_url(self, url: str, allowed_schemes: List[str] = None) -> bool:
        """
        Validate URL for security concerns.
        
        Args:
            url: URL to validate
            allowed_schemes: List of allowed URL schemes
        """
        if allowed_schemes is None:
            allowed_schemes = ['http', 'https']
            
        try:
            parsed = urllib.parse.urlparse(url)
            return (
                parsed.scheme in allowed_schemes and
                parsed.netloc and
                not any(c in url for c in '<>"\'{}|\\^`')
            )
        except Exception:
            return False

    def validate_ip(self, ip: str, allowed_ranges: List[str] = None) -> bool:
        """
        Validate IP address and check if it's in allowed ranges.
        
        Args:
            ip: IP address to validate
            allowed_ranges: List of allowed IP ranges in CIDR notation
        """
        try:
            ip_obj = ipaddress.ip_address(ip)
            if allowed_ranges is None:
                return True
                
            return any(
                ip_obj in ipaddress.ip_network(cidr)
                for cidr in allowed_ranges
            )
        except ValueError:
            return False

    def generate_nonce(self, length: int = 16) -> str:
        """Generate a secure nonce for cryptographic operations."""
        return secrets.token_hex(length)

    def hash_data(self, data: Union[str, bytes], algorithm: str = "sha256") -> str:
        """
        Hash data using specified algorithm.
        
        Args:
            data: Data to hash (string or bytes)
            algorithm: Hash algorithm to use
        """
        hash_obj = getattr(hashlib, algorithm)()
        if isinstance(data, str):
            data = data.encode()
        hash_obj.update(data)
        return hash_obj.hexdigest()

    def generate_session_id(self) -> str:
        """Generate a secure session ID."""
        return f"sess_{secrets.token_urlsafe(32)}"

    def validate_file_type(self, filename: str, allowed_extensions: List[str]) -> bool:
        """
        Validate file type based on extension.
        
        Args:
            filename: Name of the file
            allowed_extensions: List of allowed file extensions
        """
        return any(
            filename.lower().endswith(ext.lower())
            for ext in allowed_extensions
        )

    def generate_backup_code(self, length: int = 8, num_codes: int = 10) -> List[str]:
        """
        Generate backup codes for 2FA recovery.
        
        Args:
            length: Length of each code
            num_codes: Number of codes to generate
        """
        codes = set()
        while len(codes) < num_codes:
            code = ''.join(
                random.choice(string.ascii_uppercase + string.digits)
                for _ in range(length)
            )
            codes.add(code)
        return sorted(list(codes))
