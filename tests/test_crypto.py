import unittest

import crypto


class TestCrypto(unittest.TestCase):
    def test_compare_secret_and_dec_secret(self):
        """Compares the source text and the decrypted text."""

        password = 'super password'
        secret = 'super secret'
        enc_secret = crypto.encrypt(password, secret)
        dec_secret = crypto.decrypt(password, enc_secret)
        return self.assertEqual(secret, dec_secret)


if __name__ == '__main__':
    unittest.main()
