from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Card(models.Model):
    CARD_TYPE_CHOICES = (
        ('PERSON', 'Person'),
        ('PLACE', 'Place'),
        ('WEAPON', 'Weapon')
    )
    card_type = models.CharField(max_length=6,
                            choices=CARD_TYPE_CHOICES,
                            blank=False)
    name = models.CharField(max_length=200)
    deck = models.ForeignKey('Deck',
                             on_delete=models.CASCADE,
                             related_name='cards')

    def __str__(self):
        return '%s: %s' % (self.get_card_type_display(), self.name)


