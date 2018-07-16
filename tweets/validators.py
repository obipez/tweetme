from django.core.exceptions import ValidationError

def validate_content(value):
	content = value
	profanities = ["Damn", "shoot", "darn"]
	for each in profanities:
		if content.lower() == each:
			raise ValidationError("No profanities. Please enter somethign else.")
	return value