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
        fields = ['name', 'content']

    content = forms.ModelMultipleChoiceField(
        queryset=content.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'class': 'input input--text', 'placeholder': 'course name'}
        )
        self.fields['content'].widget.attrs.update(
            {'style': 'list-style: none;'}
        )   


class ContentForm(forms.ModelForm):
    class Meta:
        model = content
        fields = ['des']

    def __init__(self, *args, **kwargs):
        super(ContentForm, self).__init__(*args, **kwargs)

        self.fields['des'].widget.attrs.update(
            {'class': 'input input--text', 'placeholder': 'description'}
        )

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = registration
        fields = ['courseID', 'studentID']
        labels = {
            'courseID': 'Course',
            'studentID': 'Student'
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text', 'placeholder': 'Add text'})
