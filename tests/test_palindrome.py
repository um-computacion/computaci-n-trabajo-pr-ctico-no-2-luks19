import unittest 
# from scr.palindrome import is_palindrome 

# Test cases for the is_palindorme function
class TestPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("salas"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("hamburguesa"))
    def test_frases_palindormes(self):
        self.assertTrue(is_palindrome("Anita lava la tina"))
        self.assertTrue(is_palindrome("Amo la pacífica paloma"))
        self.assertTrue(is_palindrome("La ruta natural"))
        


if __name__ == '__main__':
     unittest.main()




    
       
