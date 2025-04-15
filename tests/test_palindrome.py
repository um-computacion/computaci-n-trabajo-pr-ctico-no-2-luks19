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

    def test_frases_no_palindromas(self):
        self.assertFalse(is_palindrome("El cielo es azul"))
        self.assertFalse(is_palindrome("La luna es blanca"))
        self.assertFalse(is_palindrome("El sol brilla"))

    def test_casos_edge(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("como 'te'va"))
        self.assertTrue(is_palindrome("HoLa"))
        self.assertTrue(is_palindrome("123431"))

if __name__ == '__main__':
     unittest.main()




    
       
