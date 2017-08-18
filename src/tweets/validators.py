from django.core.exceptions import ValidationError


#=============== Direct validation function for the field itself (inline validation)
# can be used to block low quality tweets   
def validate_content(value):
	content = value
	if content == "":
		raise ValidationError("Content cannot be blank")
	return value 