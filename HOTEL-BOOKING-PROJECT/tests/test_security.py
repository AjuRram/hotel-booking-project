import pytest
from src.security import SecurityManager

@pytest.fixture
def security_manager():
    return SecurityManager()

def test_hash_password(security_manager):
    password = "securepassword123"
    hashed_password, salt = security_manager.hash_password(password)
    
    assert isinstance(hashed_password, str)
    assert isinstance(salt, bytes)
    assert len(salt) == 16  # Salt should be 16 bytes
    assert len(hashed_password) > 0  # Hash should not be empty

def test_hash_password_with_salt(security_manager):
    password = "securepassword123"
    salt = b"\x00" * 16  # Fixed salt for testing
    hashed_password1, _ = security_manager.hash_password(password, salt)
    hashed_password2, _ = security_manager.hash_password(password, salt)
    
    assert hashed_password1 == hashed_password2  

def test_encrypt_sensitive_data(security_manager):
    sensitive_data = "SuperSecretData"
    encrypted_data = security_manager.encrypt_sensitive_data(sensitive_data)
    
    assert isinstance(encrypted_data, bytes)
    assert len(encrypted_data) > 0  

def test_log_security_event(security_manager, caplog):
    security_manager.log_security_event("Unauthorized access attempt")
    
    assert "Security Event: Unauthorized access attempt" in caplog.text  # log message is captured