from django.db import models

class Blog(models.Model):
    """A general blog users may post to."""
    text = models.TextField(default=None)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return a simple string representing the blog."""
        return self.text

class Post(models.Model):
    """An indivisual blog a user has posted."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField(default=None)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return a simple string representing the post."""
        if self.text < 51:
            return self.text
        else:
            return f"{self.text[:50]}..."