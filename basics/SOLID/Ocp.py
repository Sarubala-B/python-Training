class PaymentProcessor:
    def process_payment(self, payment_type):
        if payment_type == "credit":
            print("Processing credit card payment")
        elif payment_type == "paypal":
            print("Processing PayPal payment")


from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def pay(self):
        print("Processing credit card payment")

class PayPalPayment(Payment):
    def pay(self):
        print("Processing PayPal payment")

# ✅ Easily extendable without modifying existing code
def process_payment(payment: Payment):
    payment.pay()
