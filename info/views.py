from django.views.generic import TemplateView
import os
from mysite import settings


class AboutTemplateView(TemplateView):
    template_name = "about.html"
    another_template_name = "another_about_if_first_one_is_missing.html"

    def get_template_names(self):
        template_names = super(AboutTemplateView, self).get_template_names()
        if len(template_names) > 0 and self.check_template_existance(template_names[0]):
            pass
        else:
            template_names = [self.another_template_name, ]
        return template_names

    @staticmethod
    def check_template_existance(template_name):
        for template_path in settings.TEMPLATES[0]['DIRS']:
            if os.path.exists(template_path + '/' + template_name):
                return True
        return False
