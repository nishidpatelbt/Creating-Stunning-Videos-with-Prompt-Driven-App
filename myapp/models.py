from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    pswd = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Onboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace_username = models.CharField(max_length=50)
    workspace_name = models.CharField(max_length=50)

    def __str__(self):
        return self.workspace_username


class WorkSpace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    generated_text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.message + " - " + self.user.name


class Uploadfiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE)
    segment_url_1 = models.URLField(blank=True, null=True)
    segment_url_2 = models.URLField(blank=True, null=True)
    segment_url_3 = models.URLField(blank=True, null=True)
    segment_url_4 = models.URLField(blank=True, null=True)
    segment_url_5 = models.URLField(blank=True, null=True)
    segment_url_6 = models.URLField(blank=True, null=True)
    segment_url_7 = models.URLField(blank=True, null=True)
    segment_url_8 = models.URLField(blank=True, null=True)
    segment_url_9 = models.URLField(blank=True, null=True)
    segment_text_1 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_2 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_3 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_4 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_5 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_6 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_7 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_8 = models.TextField(max_length=500, blank=True, null=True)
    segment_text_9 = models.TextField(max_length=500, blank=True, null=True)
    upload_video_1 = models.FileField(upload_to="videos/", blank=True, null=True)
    upload_video_2 = models.FileField(upload_to="videos/", blank=True, null=True)
    upload_video_3 = models.FileField(upload_to="videos/", blank=True, null=True)
    upload_video_4 = models.FileField(upload_to="videos/", blank=True, null=True)
    upload_video_5 = models.FileField(upload_to="videos/", blank=True, null=True)
    upload_video_6 = models.FileField(upload_to="videos/", blank=True, null=True)
    upload_video_7 = models.FileField(upload_to="videos/", blank=True, null=True)
    upload_video_8 = models.FileField(upload_to="videos/", blank=True, null=True)
    upload_video_9 = models.FileField(upload_to="videos/", blank=True, null=True)
    edited_video = models.FileField(upload_to="videos/", blank=True, null=True)

    def __str__(self):
        return self.workspace.message + " - " + self.user.name


class Admin_user(models.Model):
    email = models.EmailField()
    pswd = models.CharField(max_length=20)

    def __str__(self):
        return self.email
