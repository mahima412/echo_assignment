Q4) I can define a field in a django form in the following 2 ways:
    class MyForm(forms.Form):
        myfield = forms.ChoiceField(choices=[(u.id, u.username) for u in User.objects.filter(type="TYPE1")])

    AND also as

    class MyForm(forms.Form):
        pass

        def __init__(self, *args, **kwargs):
            super(MyForm, self).__init__(*args, **kwargs)
            self.fields['myfield'] = forms.ChoiceField(choices=[(u.id, u.username) for u in User.objects.filter(type="TYPE1")])

    What is the difference between the two approaches (if any)?


ANS:



In the first case,

when the module is imported, and will stay the same for the process lifetime.



In the second case,

The choices list is created afresh each time the form is instanciated,
so it's safe - and is of the course the right way to set dynamic choices.