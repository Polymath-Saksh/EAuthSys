import pyotp

class OTP:
    def __init__(self, secret=None):
        self.secret = secret or pyotp.random_base32()
        self.totp = pyotp.TOTP(self.secret)

    def generate_otp(self):
        return self.totp.now()

    def verify_otp(self, otp):
        return self.totp.verify(otp)
