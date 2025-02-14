from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    cuisine_type = models.CharField(
        max_length=100,
        choices=(
            ("ukrainian", "Ukrainian"),
            ("italian", "Italian"),
            ("mexican", "Mexican"),
            ("japanese", "Japanese"),
            ("thai", "Thai"),
            ("georgian", "Georgian"),
        ),
    )

    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name="menus", on_delete=models.CASCADE)
    date = models.DateField()
    dishes = models.TextField()

    @property
    def upvote_count(self):
        return self.votes.filter(vote_value=True).count()

    def __str__(self):
        return f"Menu for {self.restaurant.name} on {self.date}"


