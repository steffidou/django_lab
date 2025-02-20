from django.db import models
from django.contrib.auth.models import User

# Extend User model with additional fields
class CustomerProfile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    home_address = models.TextField(blank=True, null=True)
    reward_points = models.IntegerField(default=0)

    def __str__(self):
        return self.account.username

class Car(models.Model):
    CAR_CATEGORIES = [
        ('Compact', 'Compact'),
        ('Crossover', 'Crossover'),
        ('Premium', 'Premium'),
    ]

    model_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CAR_CATEGORIES)
    rental_rate = models.DecimalField(max_digits=10, decimal_places=2)
    energy_type = models.CharField(max_length=50)
    gearbox = models.CharField(max_length=50)
    extras = models.TextField(blank=True, null=True)  # Example: Sunroof, Bluetooth
    depot_location = models.CharField(max_length=100, default="Central Hub")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.model_name

class Reservation(models.Model):
    BOOKING_STATUS = [
        ('Awaiting Confirmation', 'Awaiting Confirmation'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    automobile = models.ForeignKey(Car, on_delete=models.CASCADE)
    return_spot = models.CharField(max_length=100, default="Same as pickup")
    pickup_spot = models.CharField(max_length=100, default="Central Hub")
    start_date = models.DateField()
    end_date = models.DateField()
    final_cost = models.DecimalField(max_digits=10, decimal_places=2)
    booking_status = models.CharField(max_length=25, choices=BOOKING_STATUS, default='Awaiting Confirmation')

    def __str__(self):
        return f"{self.customer.username} - {self.automobile.model_name}"

class Transaction(models.Model):
    PAYMENT_OPTIONS = [
        ('Debit Card', 'Debit Card'),
        ('Stripe', 'Stripe'),
        ('Mobile Pay', 'Mobile Pay'),
    ]

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50, choices=PAYMENT_OPTIONS)
    processed_at = models.DateTimeField(auto_now_add=True)
    reference_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Transaction for {self.reservation} - {self.total_amount}"

class Feedback(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    automobile = models.ForeignKey(Car, on_delete=models.CASCADE)
    score = models.IntegerField()
    review_text = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.automobile.model_name}"

class Alert(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    dispatched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for {self.recipient.username}"

class RewardsProgram(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    accumulated_points = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.participant.username} - {self.accumulated_points} Points"
