from insta.models import Image, Profile
from django.contrib.auth.models import User
from django.test import TestCase

class ImageTestClass(TestCase):
    """

    test class for Image model unit tests.

    """
    def setUp(self):
        self.user = User.objects.create_user("username", "password")
        self.new_profile = Profile(profile_photo='IG.png',bio="SOCIAL",user=self.user)
        self.new_profile.save()
        self.new_image = Image(image='IG.png',image_caption="image", profile=self.new_profile)

    def test_instance_true(self):
        self.new_image.save()
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1)

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()

class ProfileTestClass(TestCase):
    '''
    test class for Profile model unit tests.
    '''
    def setUp(self):
        self.user = User.objects.create_user("username", "password")
        self.profile_test = Profile(profile_photo='IG.png',bio="SOCIAL",user=self.user)
        self.profile_test.save()

    def test_instance_true(self):
        self.profile_test.save()
        self.assertTrue(isinstance(self.profile_test, Profile)) 

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()  