from django.test import TestCase
from .models import Profile, Projects
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.vale=User(username='vale')
        self.vale.save()

        self.vale=Profile(user=self.vale, bio="aluta continua", profile_pic="https://www.pinterest.com/pin/492649949221163/", contact="Nairobi, Kenya")
        self.vale.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.vale, Profile))

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_save_profile(self):
        self.vale.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        profiles=Profile.objects.all()

        self.vale.delete_profile()
        self.assertEqual(len(profiles), 0)

class ProjectTestClass(TestCase):
    def setUp(self):
        self.Amerigo=User(username="Amerigo")
        self.Amerigo.save()

        self.firstproject=Projects(profile=self.Amerigo, title="First Project", image="https://www.pinterest.com/pin/301319031323420209/", description="this is the first uploaded project", link="https://github.com/Alice-Githui/My-Pitch-App.git", design_rate=0, usability_rate=0, content_rate=0, average_review=0)
        self.firstproject.save_project()

    def testinstance(self):
        self.assertTrue(isinstance(self.firstproject, Projects))

    def test_save_project(self):
        self.firstproject.save_project()
        projects=Projects.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_project(self):
        projects=Projects.objects.all()

        self.firstproject.delete_project()
        self.assertEqual(len(projects), 0)