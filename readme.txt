For Librarian Admin Panel:
Username: adminac
Password: testing321

For Django Admin Panel:
Username: admin
Password: testing321

Footer.html:
Later add header references of Facebook , whatsapp , instagram and Twitter


forms.py : Add if you seek to include student enrollment and branch
class StudentExtraForm(forms.ModelForm):
   class Meta:
    model=models.StudentExtra
        fields=['enrollment','branch']