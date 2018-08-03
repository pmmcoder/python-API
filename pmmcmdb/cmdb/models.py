from django.db import models

# Create your models here.
class Question(models.Model):
	user_id = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
	question_text = models.CharField(max_length=200)
	question_text_2 = models.CharField(max_length=200)
	pub_data = models.DateTimeField('date published')

	def save(self, *args, **kwargs):
	    """
	    Use the `pygments` library to create a highlighted HTML
	    representation of the code snippet.
	    """
	    super(Question, self).save(*args, **kwargs)

	def __str__(self):
		return self.question_text


class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choic_text = models.CharField(max_length=201)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choic_text