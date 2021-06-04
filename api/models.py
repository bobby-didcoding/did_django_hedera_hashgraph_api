from django.db import models
from django.contrib.auth.models import User

class Invoicing(models.Model):

	class Meta:
		verbose_name_plural = "Invoicing"
		ordering = ["-timestamp"]

	timestamp = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	tran_id = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	amount = models.IntegerField(verbose_name="Amount - tinybar (tℏ)")
	tran_fee = models.IntegerField(verbose_name="Transaction fee - tinybar (tℏ)")

	@property
	def AmountConversion(self):
		return self.amount / 100_000

	@property
	def TranFeeConversion(self):
		return self.tran_fee / 100_000
	
	
	def __str__(self):
		return f'{self.user}'