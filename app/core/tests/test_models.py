from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    
    def test_create_user_with_email_successful(self):
        """Test creating a new user with email successful"""
        email = 'liutongl5@gmail.com'
        password = 'Password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        
        self.assertEqual( user.email, email )
        self.assertTrue( user.check_password(password) )
        
    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'liutonglt@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'Password')
        
        self.assertEqual( user.email, email.lower() )
        
    def test_new_user_invalid_email(self):
        """Test Creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Password')
            
    def test_create_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'liutongl5@gmail.com',
            'Password'
        )
        
        self.assertTrue( user.is_superuser )
        self.assertTrue( user.is_staff )
        
