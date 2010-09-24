import random
from paste.script.templates import Template, var
from paste.script.command import NoDefault

class OdeskAppTemplate(Template):

    _template_dir = 'templates_dir/odesk_app/'
    summary = 'Template for basic oDesk-based app'
    required_templates = []
    use_cheetah = False

    def __init__(self, name):
        super(OdeskAppTemplate, self).__init__(name)
        secret_key = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
        self.vars += [
            var('secret_key', 'Secret key for Django settings', default=secret_key),
            var('media_dir', 'Name of the media directory', default='media'),
            var('templates_dir', 'Directory to hold base templates', default='templates'),
            var('odesk_admin', 'Enter your oDesk username, so you could access the admin', default=NoDefault),
        ]
