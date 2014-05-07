from django.contrib import messages
from django.contrib.formtools.wizard.views import NamedUrlSessionWizardView
from django import forms
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .mixins import WizardConfirmationMixin, WizardConfirmAllAtFinalStepMixin
from ..forms import FooForm, BarForm, FooConfirmationForm, BarConfirmationForm

MIXIN_DEMO_WIZARD_STEP_URL_NAME = "demo-wizard-step"
MIXIN_DEMO_WIZARD_DONE_URL_NAME = "demo-wizard-done"

MIXIN_DEMO_WIZARD_CONFIRM_ALL_STEP_URL_NAME = "demo-wizard-confirm-all-step"
MIXIN_DEMO_WIZARD_CONFIRM_ALL_DONE_URL_NAME = "demo-wizard-confirm-all-done"

named_order_forms = (
    ("foo", FooForm),
    ("confirm-foo", FooConfirmationForm),
    ("bar", BarForm),
    ("confirm-bar", BarConfirmationForm),
)


class MixinDemoWizard(WizardConfirmationMixin, NamedUrlSessionWizardView):
    template_name = "django_formwizard_mixins/wizard.html"
    
    def done(self, form_list, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'Done!')
        return redirect(MIXIN_DEMO_WIZARD_DONE_URL_NAME)


class MixinConfirmAllDemoWizard(WizardConfirmAllAtFinalStepMixin, NamedUrlSessionWizardView):
    confirmation_step_url_name = 'final-confirmation'
    template_name = "django_formwizard_mixins/wizard.html"

    def done(self, form_list, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'Done!')
        return redirect(MIXIN_DEMO_WIZARD_DONE_URL_NAME)


mixin_demo_wizard_view = MixinDemoWizard.as_view(
    named_order_forms,
    url_name=MIXIN_DEMO_WIZARD_STEP_URL_NAME,
    done_step_name=MIXIN_DEMO_WIZARD_DONE_URL_NAME,
)

mixin_demo_wizard_confirm_all_view = MixinConfirmAllDemoWizard.as_view(
    named_order_forms,
    url_name=MIXIN_DEMO_WIZARD_CONFIRM_ALL_STEP_URL_NAME,
    done_step_name=MIXIN_DEMO_WIZARD_CONFIRM_ALL_DONE_URL_NAME,
)

class HomeDemoWizardView(TemplateView):
    template_name = "django_formwizard_mixins/base.html"

home_demo_wizard_view = HomeDemoWizardView.as_view()