from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from courses.models import Course
from .models import Note, StudentProfile


User = get_user_model()


class StudentNotesApiTests(APITestCase):
    def setUp(self):
        self.student = User.objects.create_user(username="s1", password="ComplexPass123", role="student")
        self.teacher = User.objects.create_user(username="t1", password="ComplexPass123", role="teacher")
        self.course_a = Course.objects.create(name="Class 6")
        self.course_b = Course.objects.create(name="Class 7")
        StudentProfile.objects.create(user=self.student, course=self.course_a, roll_number="12")

        Note.objects.create(course=self.course_a, title="A", file="notes/a.pdf", uploaded_by=self.teacher)
        Note.objects.create(course=self.course_b, title="B", file="notes/b.pdf", uploaded_by=self.teacher)

    def test_student_gets_only_assigned_course_notes(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.get(reverse("student-notes-list"))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "A")
