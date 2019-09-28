from django.db import models, transaction


class Organization(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

    class Meta:
        unique_together = ("user", "name")

    def __str__(self) -> str:
        return self.name


class Shelf(models.Model):
    organization = models.ForeignKey("Organization", on_delete=models.CASCADE)
    size = models.PositiveSmallIntegerField()
    available_size = models.PositiveSmallIntegerField(editable=False)

    def __str__(self) -> str:
        return f"{self.organization} - Shelf {self.pk}"

    def save(self, *args, **kwargs) -> None:
        with transaction.atomic():
            self._update_available_size()
            super().save(*args, **kwargs)

    def _update_available_size(self) -> None:
        self.available_size = self.size - self.box_set.count() - 1


class Box(models.Model):
    shelf = models.ForeignKey("Shelf", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.shelf} - Box {self.pk}"

    def save(self, *args, **kwargs) -> None:
        with transaction.atomic():
            self.shelf.save()
            super().save(*args, **kwargs)
