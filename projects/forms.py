from django import forms
from .models import student, course, content, registration


class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'age', 'studentNumber', 'student_image']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text'})


class CourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = '__all__'


class ContentForm(forms.ModelForm):
    class Meta:
        model = content
        fields = '__all__'


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = registration
        fields = '__all__'
